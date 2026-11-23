# SEO Skills 🔎

Five SEO skills for Claude and other Agent Skills clients. They do the work, check it, and show their evidence, so you don't get a confident list of "best practices" from 2019.

## The skills

| Skill | Use it when you want to... |
|---|---|
| `seo-audit` | Audit a site end to end: indexing, canonicals, Core Web Vitals, schema, links, CTR gaps and AI search visibility. You get a prioritized report with fixes. |
| `seo-quick-wins` | Find wins in the traffic you already have: pages ranking 4 to 15 with weak CTR, decaying posts, and money pages nobody links to. |
| `internal-linking` | Add or audit contextual internal links, rescue orphan pages, build hubs, and fix lazy anchors. Checks every target URL before linking to it. |
| `seo-ops` | Get ready-made workflows for SERP gap research, content briefs, meta variants, schema, AI-citable rewrites and bulk keyword work. |
| `verified-seo-article-writing` | Turn a brief, press release or pile of notes into a publish-ready article where every claim is checked against a source. |

They hand off to each other. An audit finds the problems, quick wins ranks what to fix first, internal linking and SEO ops do the fixing, and the article writer ships new pages.

## Install

Grab the whole repo, then copy the skills you want. Each skill is a folder: keep the `references/` next to `SKILL.md`, since the big procedures live there.

```bash
git clone https://github.com/adityash8/claude-seo-skills.git
cp -R claude-seo-skills/.claude/skills/* ~/.claude/skills/
```

The same folders work anywhere that reads Agent Skills, for example Claude Code, Claude Desktop, Codex or Cursor. Put them wherever your client looks for skills.

## Use

Just ask in plain English:

```text
Run an SEO audit for example.com
Find quick wins in my Search Console data
Plan internal links for /pricing
Write a verified article from this press release
```

## Data sources

All five skills run on public web data alone. Plug in more sources and they get sharper:

- **Google Search Console** for real clicks, impressions and CTR
- **Ahrefs or Semrush** (via their MCP servers) for keywords, backlinks and site audits
- **Your CMS** if you want fixes applied rather than drafted

No credentials ship with this repo. Bring your own.

## House rules

- Evidence over vibes. Measured data, estimates and unknowns are kept apart.
- Platform facts age fast. The skills tell your agent to check current docs before trusting a rule.
- An audit means analysis only. Nothing gets published, deployed or changed on your site unless you say so.

## Check the repo

```bash
python3 scripts/check.py
```

This validates skill metadata, links and symlinks, and scans for anything that looks private.

## License

MIT. Use it, fork it, ship it. A star is always nice. ⭐
