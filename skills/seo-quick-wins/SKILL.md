---
name: seo-quick-wins
description: Use when harvesting recurring SEO opportunities from existing search data, including low CTR, content decay, and weak internal linking.
---

# SEO Quick Wins

Turn existing search and crawl evidence into one ranked action queue. Use **seo-audit** for a broad technical diagnosis, **internal-linking** for a full link project, and **seo-ops** for focused page work.

## Required inputs

- Site and permitted scope.
- GSC, Ahrefs, analytics, or exported CSV data with capture dates and comparison windows.
- Current page titles, descriptions, content, status, and canonicals for candidate pages.
- Crawl or body-link export for the linking program.
- Priority conversion pages, if known.
- Permission scope for recommendations, draft edits, and live changes.

Choose comparable windows with the same duration. Use year-over-year comparisons when seasonality matters, and record known tracking changes, migrations, campaigns, and releases.

No data source means no invented opportunity table. State the exact export needed, and complete only the checks the available evidence supports.

## Validate the data first

1. Confirm the site, date range, timezone, filters, and device or country scope.
2. Inspect the current connector schema before calling tools. Verify field names, accepted filter formats, pagination, and returned row counts.
3. Distinguish missing data, truncated results, and tool errors from genuine zeroes.
4. Keep query-level, page-level, and query-page datasets separate. Do not join independently aggregated exports as if they contained paired observations.
5. Normalize obvious URL variants using the verified canonical map. Do not merge pages just because their titles match.

If connectors are unavailable, use GSC performance exports for the chosen windows and a crawl export for internal links. A sitemap alone cannot establish body-link counts or orphan status.

## Program 1: CTR opportunities

Find pages with meaningful impressions, relevant queries, and weaker CTR than comparable pages or queries on the same site.

1. Set an impression floor and ranking range appropriate to the site's volume. Label these selection rules, not universal benchmarks.
2. Compare CTR within similar position, brand intent, device, country, and query types where data permits. Average position can hide a mixed query set.
3. Inspect the current search results. Ads, answer features, and other layout changes can affect clicks even when ranking holds.
4. Read the page and confirm that its title and description match the content and search intent.
5. Draft a clear title and description for each candidate. Avoid unsupported promises, stale dates, and keyword stuffing.

For prioritization, a scenario may use:

`potential additional clicks = impressions × max(0, comparison CTR - current CTR)`

Label the comparison source and uncertainty. This is a scenario, not promised lift. If there is no defensible comparison, use a qualitative priority instead of inventing a benchmark.

Search engines may choose different displayed titles or snippets. Verify current guidance against current docs before making platform-specific claims.

## Program 2: Content decay

Compare page clicks across the chosen windows, then investigate pages with meaningful losses.

1. Use both absolute lost clicks and relative decline. A large percentage change from a tiny baseline is rarely the first priority.
2. Compare impressions, query mix, position, indexing, and CTR before assigning a cause.
3. Classify the likely issue:
   - **Refreshable content:** facts, examples, intent coverage, or useful detail need work.
   - **Search-result change:** layout or answer features reduced click opportunity.
   - **Cannibalization:** multiple pages compete for overlapping intent. Confirm the query-page evidence before proposing consolidation.
   - **Demand change:** fewer searches for the topic or a seasonal shift.
   - **Technical problem:** indexing, redirects, rendering, or availability changed. Escalate through **seo-audit**.
4. Produce a page-specific refresh brief with supporting evidence. Replace weak sections with useful material rather than expanding word count for its own sake.
5. Estimate effort and rank recoverable losses by evidence strength and value. Do not equate every lost click with recoverable traffic.

Use **verified-seo-article-writing** when a substantial refresh needs claim verification. Search-result changes may need a separate visibility analysis rather than a content rewrite.

## Program 3: Internal-link opportunities

Use a current crawl and published URL inventory to find worthwhile orphan candidates and relevant pages with weak contextual coverage.

1. Keep body-link counts separate from navigation and modules.
2. Verify that candidate targets deserve discovery, return direct HTTP 200, are indexable, and have the intended canonical.
3. Prioritize useful conversion pages and relevant pages already showing search demand.
4. Read potential donors. Quote the exact insertion context, suggest a descriptive anchor, and skip existing body edges.
5. Return a bounded insertion queue. Use **internal-linking** for implementation safeguards and saved-state proof.

Do not prescribe fixed numbers of sibling links or connect every page to every hub. Relevance wins.

## Output contract

Start with one combined table:

| Priority | Page | Program | Evidence | Proposed fix | Impact basis | Effort | Confidence | State |
|---|---|---|---|---|---|---|---|---|

Then provide the concrete deliverables:

- Proposed titles and descriptions with current and suggested text.
- Refresh briefs with the exact sections, claims, or intent gaps to address.
- Link insertions with source, target, anchor, and quoted placement.
- Data scope, selection rules, limitations, and unresolved checks.
- A primary outcome metric, guardrail metrics, baseline, and follow-up date.

Use site evidence to rank impact. Avoid dated case-study percentages or invented expected gains. Keep proposed, staged, published, and verified work separate.

## Apply authorized changes

Read-only analysis does not authorize publication. Apply edits only within the stated permission scope. Keep new content in draft unless publishing is authorized; stage edits to published pages without unpublishing them.

Before saving, capture the prior state and a rollback path. After saving, read back the exact field or content change, publication status, and rendered output where applicable. A tool's success response alone is insufficient proof.

On high-value pages, avoid changing titles, content, and links at the same time when attribution matters. Choose a bounded change and record other work as a confounder.

## Recurrence and rollout

Agree on a repeat interval suited to site volume and release cadence. At each pass, review what shipped, what was verified, and whether the intended outcome improved.

For a repeated template change, record the primary metric, conversion guardrail, and read date before editing. If same-template pages have similar pre-change trends and enough traffic, assign a change group and an untouched group before editing and compare each group's change from its own baseline over matched windows. If either condition is missing, start with a small batch and report the direction of the change, not lift caused by the edit.

Pause expansion if clicks, relevant conversions, index coverage, or content quality worsen. Investigate before applying the same pattern more widely.
