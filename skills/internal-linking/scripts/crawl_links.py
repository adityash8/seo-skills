#!/usr/bin/env python3
"""Internal-link graph crawler for the internal-linking skill (stdlib only).

Fetches raw HTML (no JavaScript), which is what AI crawlers and Google's first
pass see. Seeds from the start URL plus the XML sitemap, follows internal
<a href> links breadth-first, and writes:

  pages.csv    one row per crawled URL (status, depth, inbound/outbound counts)
  links.csv    one row per internal link edge (source, target, anchor, region)
  issues.csv   one row per finding (type, url, target, detail)
  summary.json counts per issue type plus crawl metadata

Usage:
  python3 crawl_links.py https://www.example.com/ --out ./crawl [--max-pages 500]
"""
import argparse
import codecs
import csv
import json
import os
import re
import sys
import threading
import urllib.error
import urllib.request
import urllib.robotparser
import xml.etree.ElementTree as ET
import zlib
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from urllib.parse import quote, urljoin, urlsplit, urlunsplit

UA = "internal-linking-audit/1.0"
TEMPLATE_TAGS = {"header", "footer", "aside"}
BODY_TAGS = {"main", "article"}
INF = float("inf")
MAX_BODY = 50 * 1024 * 1024  # bytes per response after gunzip; the sitemap protocol's own cap
UNSAFE = re.compile(r"[^\x21-\x7e]")  # non-ASCII, space and control characters
# <meta charset>, <meta http-equiv content="...; charset=..."> or an XML declaration's encoding
DECLARED = re.compile(rb"""<meta[^>]*?charset\s*=\s*["']?\s*([\w.:-]+)|<\?xml[^>]*?encoding\s*=\s*["']([\w.:-]+)""", re.I)
LINKS_PER_PAGE = 5000  # <a href> kept per page; the rest are counted, not stored
CANONICALS_PER_PAGE = 50  # rel=canonical declarations kept per page; more than one is already a conflict


def _escape(s):
    """Percent-encode UNSAFE characters as UTF-8; existing %XX escapes are left alone."""
    return UNSAFE.sub(lambda m: quote(m.group(), safe=""), s)


def normalize(url):
    """Canonical form for comparing and fetching URLs: an IDNA host and a percent-encoded path and
    query, since urllib only sends ASCII. Raises ValueError on a malformed URL (e.g. a bad port)."""
    parts = urlsplit(url.strip())
    scheme, host = parts.scheme.lower(), (parts.hostname or "").lower()
    if not host.isascii():
        host = host.encode("idna").decode("ascii")  # UnicodeError is a ValueError
    if ":" in host:  # IPv6 literal: hostname drops the brackets the netloc needs
        host = f"[{host}]"
    if parts.port and not ((scheme == "http" and parts.port == 80) or (scheme == "https" and parts.port == 443)):
        host = f"{host}:{parts.port}"
    return urlunsplit((scheme, host, _escape(parts.path) or "/", _escape(parts.query), ""))


def host_twin(host):
    return host[4:] if host.startswith("www.") else "www." + host


def absolute(base, href):
    """normalize(urljoin(base, href)), or None when href is malformed (bad port, broken IPv6)."""
    try:
        return normalize(urljoin(base, href))
    except ValueError:
        return None


def in_scope(url, hosts):
    """True for an http(s) URL on one of the audited hosts."""
    if not url:
        return False
    parts = urlsplit(url)
    return parts.scheme in ("http", "https") and parts.netloc in hosts


class _ScopedRedirect(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to an http(s) URL on the allowed hosts; refuse it otherwise."""

    def __init__(self, hosts):
        self.hosts = hosts

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not in_scope(absolute(req.full_url, newurl), self.hosts):
            return None
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _read_body(resp):
    """Response bytes, gunzipped, at most MAX_BODY. Raises on a corrupt, truncated or oversized body."""
    raw = resp.read(MAX_BODY + 1)
    if raw[:2] == b"\x1f\x8b":
        z = zlib.decompressobj(16 + zlib.MAX_WBITS)
        raw = z.decompress(raw, MAX_BODY + 1)
        if not z.eof and len(raw) <= MAX_BODY:
            raise EOFError("truncated gzip")
    if len(raw) > MAX_BODY:
        raise ValueError("body over MAX_BODY")
    return raw


def _decode(raw, header_charset):
    """Body text, in the HTML spec's order: a byte-order mark, the Content-Type charset, then a
    declaration in the first 1024 bytes, then UTF-8. An unknown label falls through to the next."""
    for bom, enc in ((b"\xef\xbb\xbf", "utf-8-sig"), (b"\xff\xfe", "utf-16"), (b"\xfe\xff", "utf-16")):
        if raw.startswith(bom):
            return raw.decode(enc, "replace")
    m = DECLARED.search(raw[:1024])
    declared = (m.group(1) or m.group(2)).decode("ascii") if m else None
    for i, label in enumerate((header_charset, declared)):
        try:
            enc = codecs.lookup(label).name
            if i and enc.startswith(("utf-16", "utf-32")):
                enc = "utf-8"  # the declaration was readable as ASCII, so the document isn't UTF-16
            if enc in ("ascii", "iso8859-1"):
                enc = "cp1252"  # what browsers decode these labels as
            return raw.decode(enc, "replace")
        except (LookupError, TypeError):  # absent, unknown or not a text encoding
            continue
    return raw.decode("utf-8", "replace")


def fetch(url, timeout=15, follow_hosts=frozenset(), site_file=False):
    """Return (status, location, content_type, body_text). status 0 = network error or an
    unreadable body (corrupt, truncated, or over MAX_BODY).

    Page fetches follow no redirects, so each hop is recorded, and read only text/XML bodies.
    robots.txt and sitemaps (site_file=True) follow redirects within follow_hosts only: an
    apex->www (or http->https) redirect must not hide them, and a hostile file must not steer
    the crawler at loopback, private-network or cloud-metadata URLs. Their bodies are read
    whatever the media type, since sitemaps are often served as application/gzip."""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
    try:
        resp = urllib.request.build_opener(_ScopedRedirect(follow_hosts)).open(req, timeout=timeout)
    except urllib.error.HTTPError as e:
        e.close()
        return e.code, e.headers.get("Location"), e.headers.get("Content-Type", "").lower(), ""
    except Exception:  # DNS, TLS, timeout
        return 0, None, "", ""
    ctype = resp.headers.get("Content-Type", "").lower()  # media types are case-insensitive
    body = ""
    try:
        if site_file or ctype.startswith("text/") or "xml" in ctype:
            body = _decode(_read_body(resp), resp.headers.get_content_charset())
    except Exception:  # truncated, corrupt or oversized body
        return 0, None, "", ""
    finally:
        resp.close()
    return resp.status, None, ctype, body


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = defaultdict(int)
        self.has_main = False
        self.links, self.canonicals, self.base = [], [], None
        self.n_links = 0  # every <a href>, including those past LINKS_PER_PAGE
        self.noindex = self.nofollow = False
        self._a = None

    def handle_starttag(self, tag, attrs):
        if tag == "template":
            self.depth[tag] += 1
        if self.depth["template"]:  # <template> content is inert until a script clones it
            return
        a = {k: (v or "") for k, v in attrs}
        if tag in BODY_TAGS:
            self.has_main = True
        if tag in BODY_TAGS or tag in TEMPLATE_TAGS or tag == "nav":
            self.depth[tag] += 1
        if tag == "base" and "href" in a:
            if self.base is None:  # browsers use the first <base href>, even an empty one
                self.base = a["href"]
        elif tag == "link" and "canonical" in a.get("rel", "").lower().split():
            href = a.get("href", "").strip()
            if len(self.canonicals) < CANONICALS_PER_PAGE and href not in self.canonicals:
                self.canonicals.append(href)  # duplicate declarations must not crowd out a conflict
        elif tag == "meta" and a.get("name", "").lower() in ("robots", "googlebot"):
            directives = set(re.split(r"[\s,]+", a.get("content", "").lower()))
            self.noindex = self.noindex or bool(directives & {"noindex", "none"})  # none = noindex, nofollow
            self.nofollow = self.nofollow or bool(directives & {"nofollow", "none"})
        elif tag == "a" and "href" in a:
            self.n_links += 1
            if len(self.links) >= LINKS_PER_PAGE:  # a 50 MB page could hold millions
                return
            in_body = any(self.depth[t] for t in BODY_TAGS)
            # nav/header/footer/aside win over main/article: a sidebar or footer nested in <main> is still template
            template = any(self.depth[t] for t in TEMPLATE_TAGS | {"nav"})
            self._a = {"href": a["href"], "rel": a.get("rel", "").lower(), "text": [],
                       "in_body": in_body, "template": template}
        elif tag == "img" and self._a is not None and a.get("alt"):
            self._a["text"].append(a["alt"])

    def handle_endtag(self, tag):
        if self.depth["template"] and tag != "template":
            return
        if tag in self.depth and self.depth[tag]:
            self.depth[tag] -= 1
        if tag == "a" and self._a is not None:
            self._a["text"] = " ".join(" ".join(self._a["text"]).split())
            self.links.append(self._a)
            self._a = None

    def handle_data(self, data):
        if self._a is not None and not self.depth["template"]:
            self._a["text"].append(data)


def sitemap_budget(max_pages):
    """Discovery limits tied to the crawl size: sitemap files fetched and page URLs kept."""
    return {"files": max(20, max_pages // 25), "urls": max(1000, 4 * max_pages), "truncated": False}


def sitemap_urls(root, robots_txt, hosts, seen=None, budget=None):
    """Return (page URLs listed in the origin's XML sitemaps, sitemap URLs skipped as off-site).

    robots.txt and sitemap indexes are site-controlled, so only sitemaps on the audited hosts
    are fetched, and their redirects are followed only within those hosts. Pass the same
    `seen` set and `budget` (see sitemap_budget) across origins so a sitemap both declare is
    fetched once and the limits cover the whole crawl. When the budget runs out, the rest is
    left unread and budget["truncated"] is set."""
    seeds = re.findall(r"(?im)^\s*sitemap:\s*(\S+)", robots_txt) or ["/sitemap.xml"]
    found, skipped, seen = [], [], set() if seen is None else seen
    budget = {"files": INF, "urls": INF, "truncated": False} if budget is None else budget
    queue = [(s, 0) for s in seeds]
    while queue:
        href, level = queue.pop(0)
        url = absolute(root, href)
        if not in_scope(url, hosts):
            skipped.append(href)
            continue
        if url in seen or level > 2:
            continue
        if budget["files"] <= 0 or budget["urls"] <= 0:
            budget["truncated"] = True
            break
        budget["files"] -= 1
        seen.add(url)
        status, location, _, body = fetch(url, follow_hosts=hosts, site_file=True)
        target = absolute(url, location) if location else None
        if location and not in_scope(target, hosts):  # a redirect fetch() refused to follow
            skipped.append(target or location)
        if status != 200 or not body or "<!ENTITY" in body:  # no entity expansion from remote XML
            continue
        try:
            tree = ET.fromstring(body.encode("utf-8"))
        except ET.ParseError:
            continue
        is_index = tree.tag.endswith("sitemapindex")
        # Only the <loc> directly under each <url>/<sitemap> entry: image:loc, video:content_loc
        # and the like sit deeper and are media, not pages.
        for loc in (c for entry in tree for c in entry if c.tag.rsplit("}", 1)[-1] == "loc"):
            if not loc.text:
                continue
            if is_index:
                queue.append((loc.text.strip(), level + 1))
            else:
                page = absolute(url, loc.text)
                if not in_scope(page, hosts):
                    continue
                if budget["urls"] <= 0:
                    budget["truncated"] = True
                    break
                budget["urls"] -= 1
                found.append(page)
    return found, skipped


class Robots:
    """robots.txt rules per origin (scheme, host and port), each fetched once.

    Rules apply only to the origin that serves the file, so the www/apex twin and the
    http/https variants each get their own. Status handling follows RFC 9309 and Google: a
    4xx (401 and 403 included) or an unfollowed redirect means no rules, while a 5xx, 429 or
    network error means the file is unreachable and the whole origin is disallowed."""

    def __init__(self, hosts):
        self.hosts, self.rules, self.status, self.lock = hosts, {}, {}, threading.Lock()

    @staticmethod
    def _origin(url):
        parts = urlsplit(url)
        return f"{parts.scheme}://{parts.netloc}"

    def _load(self, url):
        origin = self._origin(url)
        with self.lock:
            if origin not in self.rules:
                status, _, _, text = fetch(origin + "/robots.txt", follow_hosts=self.hosts, site_file=True)
                parser = urllib.robotparser.RobotFileParser()
                if 200 <= status < 300:
                    parser.parse(text.splitlines())
                elif 300 <= status < 500 and status != 429:
                    text, parser.allow_all = "", True
                else:  # unreachable: 5xx, 429 or network error
                    text, parser.disallow_all = "", True
                self.rules[origin], self.status[origin] = (parser, text), status
            return self.rules[origin]

    def text(self, url):
        return self._load(url)[1]

    def origins(self):
        """Origins whose robots.txt has been read so far."""
        with self.lock:
            return set(self.rules)

    def reachable(self, url):
        """False when the origin's robots.txt was a 5xx, 429 or network error (the origin is off limits)."""
        self._load(url)
        status = self.status[self._origin(url)]
        return 0 < status < 500 and status != 429

    def allowed(self, url):
        return self._load(url)[0].can_fetch(UA, url)


def link_budget(max_pages):
    """Internal links kept across the whole crawl, so a few link-stuffed pages can't exhaust memory."""
    return max(100_000, 500 * max_pages)


def crawl(start, max_pages=500, workers=4, max_links=100):
    start = normalize(start)
    origin = urlsplit(start)
    hosts = {origin.netloc, host_twin(origin.netloc)}
    robots = Robots(hosts)
    in_sitemap, skipped_sitemaps, scanned, sitemaps_seen = set(), [], set(), set()
    budget = sitemap_budget(max_pages)
    links_left, links_truncated = link_budget(max_pages), False

    def read_sitemaps():
        """Sitemaps of every origin reached so far (the www/apex twin, http/https), each once."""
        for o in sorted(robots.origins() - scanned):
            scanned.add(o)
            if not robots.reachable(o + "/"):  # robots.txt unavailable: fetch nothing, sitemaps included
                continue
            found, skipped = sitemap_urls(o + "/", robots.text(o + "/"), hosts, sitemaps_seen, budget)
            in_sitemap.update(found)
            skipped_sitemaps.extend(s for s in skipped if s not in skipped_sitemaps)

    def visit(url):
        if not robots.allowed(url):
            return url, {"status": -1, "location": None, "parser": None}
        status, location, ctype, body = fetch(url)
        parser = None
        if status == 200 and "html" in ctype:
            parser = LinkParser()
            parser.feed(body)
        return url, {"status": status, "location": location, "parser": parser}

    # Click depth is a shortest path where a link costs 1 and a redirect costs 0 (a redirect is
    # not a click). Each batch fetches the shallowest queued URLs, so a URL's depth is final
    # before it is fetched. Sitemap URLs the link graph never reached are orphan candidates:
    # they are crawled last, along with whatever they link or redirect to, with no depth. Each
    # time the queue runs dry, origins reached since the last pass add their sitemaps.
    pages, edges = {}, []
    dist, queued = {start: 0}, {start: None}  # dict as an ordered set
    with ThreadPoolExecutor(max_workers=workers) as pool:
        while len(pages) < max_pages:
            if not queued:
                read_sitemaps()
                for u in sorted(in_sitemap - pages.keys()):
                    dist[u] = INF
                    queued[u] = None
            if not queued:
                break
            d = min(dist[u] for u in queued)
            batch = [u for u in queued if dist[u] == d][: max_pages - len(pages)]
            for u in batch:
                del queued[u]
            for url, rec in pool.map(visit, batch):
                pages[url] = rec
                outs = _out_links(url, rec, hosts)
                if rec["parser"]:
                    links_truncated |= rec["parser"].n_links > len(rec["parser"].links) or len(outs) > links_left
                    rec["parser"].links = []  # now in edges; n_links keeps the count
                outs = outs[:links_left]
                links_left -= len(outs)
                edges.extend(outs)
                steps = [(o["target"], 1) for o in outs]
                target = absolute(url, rec["location"]) if rec["location"] else None
                if in_scope(target, hosts):
                    steps.append((target, 0))
                for t, cost in steps:
                    if t in pages or (t in dist and dist[t] <= dist[url] + cost):
                        continue
                    if t not in dist:
                        queued[t] = None
                    dist[t] = dist[url] + cost
    read_sitemaps()  # a crawl cut short by max_pages still reports the sitemap URLs it left
    depth = {u: d for u, d in dist.items() if d != INF}
    unfetched = len((queued.keys() | in_sitemap | {e["target"] for e in edges}) - pages.keys())
    summary_extra = {"sitemap_truncated": budget["truncated"], "links_truncated": links_truncated,
                     "skipped_sitemaps": skipped_sitemaps,
                     "robots_txt_status": dict(sorted(robots.status.items()))}
    return _report(start, hosts, pages, edges, depth, in_sitemap, max_links, unfetched, summary_extra)


def _doc_base(url, parser):
    """The URL that relative links and canonicals resolve against: <base href> when present."""
    if parser.base:
        try:
            return urljoin(url, parser.base)
        except ValueError:
            pass
    return url


def _out_links(url, rec, hosts):
    parser = rec["parser"]
    if parser is None:
        return []
    base = _doc_base(url, parser)
    out = []
    for link in parser.links:
        href = link["href"].strip()
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
            continue
        target = absolute(base, href)
        if not in_scope(target, hosts) or target == url:
            continue
        if link["template"]:
            region = "template"
        elif link["in_body"] or not parser.has_main:
            region = "body"
        else:
            region = "other"
        out.append({"source": url, "target": target, "anchor": link["text"], "region": region,
                    "nofollow": parser.nofollow or "nofollow" in link["rel"].split()})
    return out


def _chain(url, pages, hosts):
    """Follow recorded redirects; returns (hops, final_url, loop). final_url is None when a
    Location header is malformed."""
    hops, seen, cur = 0, {url}, url
    while cur in pages and pages[cur]["location"]:
        cur = absolute(cur, pages[cur]["location"])
        hops += 1
        if cur is None:
            break
        if cur in seen:
            return hops, cur, True
        seen.add(cur)
        if not in_scope(cur, hosts):
            break
    return hops, cur, False


def _report(start, hosts, pages, edges, depth, in_sitemap, max_links, unfetched, summary_extra):
    inbound_all, inbound_body, anchors = defaultdict(set), defaultdict(set), defaultdict(set)
    out_all, out_body, inbound_nofollow = defaultdict(set), defaultdict(set), defaultdict(set)
    for e in edges:
        out_all[e["source"]].add(e["target"])
        if e["region"] == "body":
            out_body[e["source"]].add(e["target"])
        if e["nofollow"]:  # a nofollow link passes nothing, so it doesn't count as a way in
            inbound_nofollow[e["target"]].add(e["source"])
            continue
        inbound_all[e["target"]].add(e["source"])
        if e["region"] == "body":
            inbound_body[e["target"]].add(e["source"])
        if e["anchor"]:
            anchors[e["target"]].add(e["anchor"].lower())

    issues = []

    def add(kind, url, target="", detail=""):
        issues.append({"type": kind, "url": url, "target": target, "detail": detail})

    listed = in_sitemap | {_chain(u, pages, hosts)[1] for u in in_sitemap} - {None}
    hops, final, loop = _chain(start, pages, hosts)
    roots = {start, final}  # the crawl root, and where it redirects
    root = pages.get(final) if final else None
    why = ("redirect loop" if loop else "malformed Location" if final is None
           else f"redirects off-site to {final}" if not in_scope(final, hosts)
           else "not fetched" if root is None
           else "blocked by robots.txt" if root["status"] == -1
           else f"status {root['status']}" if root["status"] != 200
           else "not HTML" if root["parser"] is None else "")
    if why:  # whatever the sitemap says, a root that never reaches an HTML 200 means the crawl found nothing
        add("start_failed", start, final if hops and final else "", why)
    for e in edges:
        rec = pages.get(e["target"])
        if rec is None:
            continue
        st = rec["status"]
        if st == 0 or st >= 400:
            add("broken_link", e["source"], e["target"], f"status {st}; {e['region']} link")
        elif 300 <= st < 400:
            hops, final, loop = _chain(e["target"], pages, hosts)
            final_st = pages[final]["status"] if final in pages else None
            if final is None:
                add("broken_link", e["source"], e["target"], f"status {st} to a malformed Location; {e['region']} link")
            elif loop:
                add("broken_link", e["source"], e["target"], f"redirect loop; {e['region']} link")
            elif final_st is not None and 300 <= final_st < 400:  # the chain ends at a 3xx with no Location
                where = f" at {final}" if hops else ""
                add("broken_link", e["source"], e["target"],
                    f"status {final_st} with no Location{where}; {e['region']} link")
            elif final_st is not None and (final_st == 0 or final_st >= 400):
                add("broken_link", e["source"], e["target"],
                    f"redirects to {final} (status {final_st}); {e['region']} link")
            elif in_scope(final, hosts) or urlsplit(final).scheme in ("http", "https"):
                # another host is reported but never fetched; a mailto:/tel: vanity redirect is not a defect
                where = "" if in_scope(final, hosts) else " off-site"
                add("link_via_redirect", e["source"], e["target"],
                    f"redirects{where} to {final} ({hops} hop{'s' if hops != 1 else ''}); {e['region']} link")
        if e["nofollow"]:
            src = pages[e["source"]]["parser"]
            add("internal_nofollow", e["source"], e["target"],
                e["region"] + ("; page meta robots nofollow" if src.nofollow else ""))
        if e["source"].startswith("https://") and e["target"].startswith("http://"):
            add("http_link", e["source"], e["target"])

    rows = []
    for url, rec in sorted(pages.items()):
        st, parser = rec["status"], rec["parser"]
        if 300 <= st < 400:
            hops, final, loop = _chain(url, pages, hosts)
            if loop:
                add("redirect_loop", url, final)
            elif hops > 1:
                add("redirect_chain", url, final or "", f"{hops} hops")
        if url in in_sitemap and st != 200:
            add("sitemap_non_200", url, detail="blocked by robots.txt" if st == -1 else f"status {st}")
        canonicals = list(dict.fromkeys(  # ordered, de-duplicated in O(n)
            c for c in (absolute(_doc_base(url, parser), href) if href.strip() else None
                        for href in (parser.canonicals if parser else [])) if c))
        canonical = " ".join(canonicals)  # several = conflicting signals, which never reads as self-canonical
        noindex = bool(parser and parser.noindex)
        if st == 200 and parser:
            if url in in_sitemap and noindex:
                add("sitemap_noindex", url)
            if len(canonicals) > 1:
                add("canonical_conflict", url, detail=f"{len(canonicals)} different rel=canonical: {canonical}")
            if url in in_sitemap and canonical and canonical != url:
                add("sitemap_non_canonical", url, canonical)
            n_in, n_body = len(inbound_all[url]), len(inbound_body[url])
            if url not in roots and not noindex:  # a noindex page needs no followed inbound links
                if n_in == 0:
                    nf = len(inbound_nofollow[url])
                    detail = f"only nofollow links, from {nf} page(s)" if nf else ""
                    if url in listed:
                        detail = "in sitemap, " + (detail or "no internal links")
                    add("orphan", url, detail=detail)
                elif n_in == 1:
                    add("single_inbound", url, next(iter(inbound_all[url])))
                if n_in > 0 and n_body == 0:
                    add("no_body_inbound", url, detail=f"{n_in} template/other links only")
            d = depth.get(url)
            if d is not None and d > 3:
                add("deep_page", url, detail=f"depth {d}")
            if parser.n_links > max_links:
                add("too_many_links", url, detail=f"{parser.n_links} <a href> on page (heuristic cap {max_links})")
        rows.append({"url": url, "status": st, "depth": depth.get(url, ""), "in_sitemap": url in in_sitemap,
                     "canonical": canonical, "noindex": noindex,
                     "inbound_all": len(inbound_all[url]), "inbound_body": len(inbound_body[url]),
                     "distinct_anchors": len(anchors[url]),
                     "outbound_all": len(out_all[url]), "outbound_body": len(out_body[url])})

    counts = defaultdict(int)
    for i in issues:
        counts[i["type"]] += 1
    summary = {"start": start, "hosts": sorted(hosts), "pages_crawled": len(pages),
               "html_200_pages": sum(1 for r in pages.values() if r["status"] == 200 and r["parser"]),
               "sitemap_urls": len(in_sitemap), "internal_edges": len(edges),
               "unfetched_urls": unfetched,
               "truncated": unfetched > 0 or summary_extra.get("sitemap_truncated", False)
               or summary_extra.get("links_truncated", False),
               **summary_extra,
               "renderer": "raw HTML (no JavaScript)",
               "issues": dict(sorted(counts.items()))}
    return rows, edges, issues, summary


def _cell(v):
    """Defuse spreadsheet formulas: anchors and details are site-controlled text."""
    return "'" + v if isinstance(v, str) and v[:1] in ("=", "+", "-", "@", "\t", "\r") else v


def write(out_dir, rows, edges, issues, summary):
    os.makedirs(out_dir, exist_ok=True)
    for name, data, fields in [
        ("pages.csv", rows, list(rows[0].keys()) if rows else ["url"]),
        ("links.csv", edges, ["source", "target", "anchor", "region", "nofollow"]),
        ("issues.csv", issues, ["type", "url", "target", "detail"]),
    ]:
        with open(os.path.join(out_dir, name), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows({k: _cell(v) for k, v in r.items()} for r in data)
    with open(os.path.join(out_dir, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("start_url")
    ap.add_argument("--out", default="crawl")
    ap.add_argument("--max-pages", type=int, default=500)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--max-links", type=int, default=100, help="flag pages with more <a href> than this (heuristic)")
    args = ap.parse_args(argv)
    rows, edges, issues, summary = crawl(args.start_url, args.max_pages, args.workers, args.max_links)
    write(args.out, rows, edges, issues, summary)
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
