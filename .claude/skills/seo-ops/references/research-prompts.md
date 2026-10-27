# Research Prompts

Use these as execution contracts. Replace bracketed inputs with supplied or verified information. If live search access is unavailable, say so and analyze the supplied evidence only.

## SERP gap analysis

Inputs: query, market, language, device, target audience, target page, and business goal.

1. Observe the current results and record the date and search context.
2. Read the relevant ranking pages, not just their snippets. Note inaccessible pages.
3. Compare intent, unique facts, section coverage, evidence, format, and reader task.
4. Record observed search features separately from ordinary results.
5. Recommend gaps the target can answer with real expertise or evidence.

Return:

| Page | Intent | Facts and topics covered | Distinct angle | Missing reader need | Evidence |
|------|--------|--------------------------|----------------|---------------------|----------|

List common coverage, meaningful gaps, and one recommended angle. Do not copy competitors' phrasing or equate length with quality.

## Question-demand mining

Inputs: topic, audience, market, and available search or community data.

- Collect actual questions from search results, site search, support material, or relevant public discussions.
- Preserve the source URL or dataset and observation date.
- Separate observed questions from generated question ideas.
- Cluster by intent and merge duplicates without erasing meaningful distinctions.
- Recommend an inline answer, section, table, or visible FAQ only where useful.

Return:

| Question | Observed or proposed | Source | Intent | Answer format | Priority reason |
|----------|----------------------|--------|--------|---------------|-----------------|

Pitfall: plausible question wording is not proof of search demand. A visible FAQ does not imply eligibility for a special search display. Verify current official docs before making that claim.

## Keyword expansion

Inputs: seed, audience, market, product or service, and available keyword data.

Produce primary clusters, related topics, specific variants, and terms to exclude. Record source, date range, geography, units, and whether each metric is measured or estimated.

| Keyword | Parent intent | Demand evidence | Competition evidence | Proposed page | Business relevance |
|---------|---------------|-----------------|----------------------|---------------|--------------------|

- Keep generated query expansions labeled as hypotheses.
- Map keywords with the same intent to one useful page where appropriate.
- Do not infer conversion rate from query shape alone.
- Prioritize reader value and business relevance alongside measured demand.
- If strategic prioritization is needed, use a keyword-research skill if available, or state the prioritization method directly.

## Depth and scope benchmarking

Read representative ranking pages and compare:

| URL | Reader task | Topics | Unique facts | Original evidence | Missing explanation |
|-----|-------------|--------|--------------|-------------------|---------------------|

Recommend the facts, examples, and explanations required to satisfy the reader. Length estimates are planning aids, not ranking goals. Do not require more facts than competitors when fewer well-supported facts answer the question.

## AI citation analysis

Inputs: query set, relevant answer products, target market, and observed or accessible answer sessions.

For each accessible product:

1. Record the exact query, product or mode, date, language, and session conditions.
2. Capture the answer and citation URLs. Mark unavailable products as untested.
3. Read cited pages and distinguish direct citations from brand mentions or recommendations.
4. Compare source format, evidence, authorship, freshness, and first-party versus third-party ownership.
5. Identify a useful contribution the target can substantiate.

Return:

| Product or mode | Query | Cited URL | Citation context | Source type | Mention or recommendation | Observation date |
|-----------------|-------|-----------|------------------|-------------|---------------------------|------------------|

End with a content or distribution opportunity and the evidence for it. Do not invent citation text, rely on remembered answer behavior, or claim that observed patterns guarantee future inclusion.

## Search-surface prioritization

Inputs: query set, business objective, existing page performance, available answer observations, and effort constraints.

| Surface | Observed opportunity | Data confidence | Reader action available | Required work | Priority reason |
|---------|----------------------|-----------------|-------------------------|---------------|-----------------|

Recommend a primary surface and a testable action. Treat scores as decision aids with an explicit method, not forecasts. If data is missing, state what observation would change the recommendation. Avoid assumed click-through or conversion multipliers.
