---
name: internal-linking
description: Use when planning, adding, auditing, or measuring contextual internal links, orphan recovery, hubs, or anchor rewrites.
license: MIT
---

# Internal Linking

Build useful paths between pages, then prove that the intended links were saved. For a broad technical audit, start with **seo-audit**. For a recurring, lightweight opportunity harvest, use **seo-quick-wins**. Site hierarchy changes need a separate architecture plan.

## Choose a mode

| Request | Mode |
|---|---|
| Find orphans, broken targets, or weak link coverage | Diagnose |
| Choose targets, donors, and placements | Plan |
| Add approved links or rewrite anchors | Implement |
| Check results after a linking change | Measure |
| Link a new article into the existing site | Editorial loop |

## Required inputs

- Site and permitted URL scope.
- Fresh crawl or page export with published status, body links, canonicals, and indexability where available.
- Search or analytics data when ranking donors or measuring results.
- Target page priorities and any editorial restrictions.
- Permission scope: recommendations, draft edits, revisions, or approved live changes.

Missing data limits the result. Do not label a URL an orphan from a sitemap alone, or claim technical verification from a search snippet.

## Guardrails

1. New content stays Draft or Pending Review unless publication is authorized.
2. Never change a published source to Draft to stage a link. Use a revision, staging copy, or authorized live edit.
3. Count contextual body links separately from navigation, breadcrumbs, related-content modules, and footer links. Before relying on an export's body-link counts, check a sample against rendered pages. A link inside `<main>` is not necessarily editorial.
4. Keep one planned body edge per source and target. Skip insertion if that body edge already exists, including a redirect or URL variant that resolves to the same canonical page.
5. Use ordinary crawlable links. Do not add internal `nofollow`, `sponsored`, or `ugc` attributes without a documented reason.
6. Verify the target returns a direct HTTP 200, is indexable, and has the intended canonical. Prefer linking directly to the canonical URL. If evidence is unavailable, mark the edge unverified and do not apply it.
7. Quote a real placement from the current source. If it has disappeared, find a genuinely equivalent passage or reject the row. Never invent a claim to justify a link.
8. Traffic alone does not make a good hub. Exclude off-topic, thin, duplicate, or unhelpful targets even when they receive visits.
9. Start with a bounded manual batch. Bulk insertion requires explicit scope, rollback, and a small checked sample before expansion.
10. Use evidence gathered after relevant canonical, redirect, or indexability fixes. Old exports may describe a problem that no longer exists.
11. Read back the saved content and publication status. A successful save response is not proof that the link exists.

## Diagnose

1. Define the crawl scope, capture date, and coverage limits. Combine crawl discovery with published URL inventories to find pages the crawl cannot reach.
2. Repair broken body targets and unnecessary redirect hops before adding more links.
3. Identify pages with no discovered inbound body links. Separate true discovery problems from pages that should remain excluded or unindexed.
4. Find relevant targets with search demand, reader value, or a conversion role. Use query and page data rather than position alone.
5. Find potential donors with topical relevance, useful traffic, external links, or strong existing internal coverage.

Use an authorized crawl or page export that covers the permitted URL scope. If it is missing, ask for it and continue only with checks the available evidence supports. A partial export cannot establish that a page has no inbound links.

Report counts for published URLs, unique body edges, orphan candidates, verified target issues, and coverage gaps. If a full crawl is unavailable, label the diagnosis partial.

## Plan

Choose the applicable play after hygiene:

- **Authority to opportunity:** relevant established donors link to useful pages that already show search visibility but need stronger internal discovery.
- **Traffic to conversion:** visited pages link to relevant conversion pages. Use observed conversion data when available; do not invent conversion rates.
- **New to old and old to new:** a new article links to established coverage, then older relevant pages are queued for links back to the new article.

Site search such as `site:example.com "topic phrase"` can discover candidates. It does not prove that a target is current, indexable, or relevant.

Rank edges by reader usefulness, target quality, strategic value, donor strength, and placement quality. Keep the first batch small enough to inspect every saved edit.

Return one row per unique edge:

| Source | Target | Play | Proposed anchor | Exact context quote | Placement | Evidence | Status |
|---|---|---|---|---|---|---|---|

Use concise descriptive anchors that fit the sentence. Avoid empty anchors, "click here", forced exact matches, and repeated target links. Spread links where they help the reader. A link count is not a quota.

## Implement

1. Fetch the current source and target. Confirm the correct page identity and editing permissions.
2. Recheck target status, indexability, canonical, existing body links, and the quoted placement.
3. Stage the smallest necessary change. Preserve surrounding claims and formatting.
4. Save through the permitted draft, revision, or live workflow.
5. Read back the saved body and confirm the exact href, visible anchor, and page status.
6. For staged changes to published pages, confirm the live page remains unchanged. For authorized live changes, inspect the rendered page and follow the link.
7. Record rejected edges with the reason. Stop the batch if saves alter unrelated content or publication status.

Suggestion plugins may help find candidates. Verify current capabilities against current docs and treat suggestions as leads, not evidence. Keep automatic insertion disabled unless the approved workflow explicitly includes it.

## Editorial loop

For each new article:

- Add relevant links to established coverage, including a useful hub when one exists.
- Verify each target and keep the copy readable. Do not pad with weak links.
- Queue relevant older pages for inbound links after the new target is available and verified.
- Keep older-page edits within the same published-source safety rules.

Use **verified-seo-article-writing** when the article also needs source and claim verification.

## Measure

Before implementation, record the target and donor URLs, any comparable untouched pages, the primary metric, and the baseline and follow-up windows. Keep repair work such as redirects separate from the measured link changes. Check that the new links are live and have been recrawled before starting the follow-up window.

Record unique body inlinks, impressions, clicks, query mix, position, and relevant conversions. When the groups tracked similarly before the change, compare the change on the targets with the change on the untouched pages over equal-length windows. If using search position, compare the same query set in both windows and weight position by impressions. Track donor clicks separately so a target gain cannot hide harm to donors. If there is no credible comparison, label the result directional.

If a repeated insertion rule performs poorly or introduces irrelevant links, stop expansion and review the pattern before changing more pages.

## Output contract

Return the edge queue plus:

- Scope, evidence dates, and coverage limits.
- Counts: proposed, rejected, staged, published, and verified edges.
- Verification per applied edge: target checks, body href, anchor, page status, and readback result.
- Remaining blockers and the next measurement date.

Use distinct states: **proposed**, **staged**, **published**, **verified**, or **blocked**. Report an unavailable check explicitly. Never report a staged revision as a live result.
