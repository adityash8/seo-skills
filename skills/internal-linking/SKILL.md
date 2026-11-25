---
name: internal-linking
description: Plan, audit, review or measure internal links with verified placements, explicit approval for live changes, and evidence-based specialist handoffs.
---

# Internal Linking

Build useful paths between pages, then prove that the intended links were saved. For a broad technical audit, start with **seo-audit**. For a recurring, lightweight opportunity harvest, use **seo-quick-wins**. Site hierarchy changes need a separate architecture plan.

Do NOT use for broad technical audits (`seo-audit`), recurring opportunity harvests (`seo-quick-wins`), or article claim verification (`verified-seo-article-writing`). A new hierarchy needs a separate architecture design.

**Required handoff check:** before returning any mode's deliverable, include a `Skill or owner | Task | Required evidence | Status` table for work outside this skill. Name the applicable skill below, pass dated evidence and restrictions, and report `not run`. An unnamed editor does not replace an available skill route. Live-changing follow-ups must say `awaiting explicit user approval; not run` unless approval already covers that exact scope.

## Choose a mode

| Request | Mode |
|---|---|
| Find orphans, broken targets, or weak link coverage | Diagnose |
| Choose targets, donors, and placements | Plan |
| Add approved links or rewrite anchors | Implement |
| Check results after a linking change | Measure |
| Review an existing link proposal | Review |
| Link a new article into the existing site | Editorial loop |

## Required inputs

- Site and permitted URL scope.
- Fresh crawl or page export with published status, body links, canonicals, and indexability where available.
- Search or analytics data when ranking donors or measuring results.
- Target page priorities and any editorial restrictions.
- Permission scope: recommendations, draft edits, revisions, or approved live changes.

Missing data limits the result. Do not label a URL an orphan from a sitemap alone, or claim technical verification from a search snippet.

## Guardrails

1. Draft plans, diagnosis, readouts and handoffs may proceed. Require explicit user approval before live edits, publication, consolidation/deletion, redirect or navigation changes, tracking repairs, rollback or bulk expansion unless that exact scope is already approved. This applies to next actions and handoffs too: a threshold breach proposes rollback and never authorizes it. New content stays Draft or Pending Review until publication is approved.
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
12. Every metric names its source and date range. Label dated exports, live checks, calculated results and assumptions distinctly. Without per-URL referring-domain evidence, write `authority: unknown`; label impressions used for donor ordering `proxy: GSC impressions`. Never invent authority figures or mix estimated vendor traffic with measured search clicks.
13. Exclude no-touch pages and pages with conflicting scheduled changes as donors, targets and experiment controls. Missing edges in a partial graph remain provisional; do not invent donors or targets to meet a link quota.
14. Separate hygiene repairs and sitewide modules from a contextual-link experiment. Hygiene has **no ranking claim**. Count a link as verified only when its ordinary anchor and href exist in raw page HTML; a JavaScript-only link remains a finding.


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

## Review

Test the proposal against current evidence. If access is unavailable, use dated exports and label live checks unavailable. Report correctness gaps in `Plan says | Problem | Evidence | Fix`, followed by a verdict: ready, ready after fixes, or rework.

Reject fabricated context, no-touch donors, redirecting or unverified targets, duplicate body edges and controls connected to treatment pages or donors. Shared query rankings are a reason for diagnosis, not automatic consolidation. Keep hierarchy changes and hygiene separate from the measured wave. Provide the relevant specialist handoffs below.

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

For a controlled readout, register the target/query cohorts, comparable untouched controls, equal whole-week baseline/post windows, noise estimate, success/failure thresholds, donor guardrails and edit freeze before treatment. Exclude controls linked to or from targets or donors. Keep sitewide changes outside the measured wave and record their dates.

Keep the registered metric fixed. For position difference-in-differences, calculate target position change minus median control change, with each change equal to post minus baseline. Negative means improvement; apply the registered thresholds and preserve an inconclusive verdict when neither pass nor fail applies. Without enough comparable controls or search volume, say `measurement: underpowered, directional only` and claim no ranking effect.

Broken conversion tracking excludes conversions from the readout; it does not replace the registered metric. Missing donor clicks or impressions mean the donor guardrail is unassessed. Any proposed tracking repair or donor-link rollback requires explicit approval. Extend observation only as the registered procedure permits; do not retrospectively invent a registration or choose favorable windows.

If a repeated insertion rule performs poorly or introduces irrelevant links, stop expansion and review the pattern before proposing more changes.

## Output contract

Return the edge queue plus:

- Scope, evidence dates, and coverage limits.
- Counts: proposed, rejected, staged, published, and verified edges.
- Verification per applied edge: target checks, body href, anchor, page status, and readback result.
- Remaining blockers and the next measurement date.

Use distinct states: **proposed**, **staged**, **published**, **verified**, or **blocked**. Report an unavailable check explicitly. Never report a staged revision as a live result.

## Required handoffs

Include only relevant rows, with the concrete URLs, task, dated evidence, restrictions and execution status. Do not claim another skill has run without its output.

| Skill or owner | Task | Required evidence | Status |
|---|---|---|---|
| `seo-ops` | Later approved page/link edits | Edge queue, exact context, current HTML, target checks, no-touch list and exact approval scope | not run; live changes awaiting explicit user approval |
| `verified-seo-article-writing` | Article claim verification | Full draft, claim list, supporting sources and link context | not run |
| `seo-audit` | Diagnose possible cannibalization before any consolidation decision | Dated page-query exports, both pages, intent, canonical/indexing and redirect history | not run; live changes awaiting explicit user approval |
| Architecture specialist | Design a new hierarchy/navigation separately | URL inventory, current graph, proposed user paths, no-touch list and experiment windows | not run; live changes awaiting explicit user approval |
| Analytics specialist | Diagnose broken conversion tracking and propose repair | Dated event history, property/event configuration, signup flow and experiment freeze | not run; live repair awaiting explicit user approval |

The last two rows are human roles; this public collection has no dedicated skills for those specialties. Diagnosis and design may proceed without authorizing implementation.

