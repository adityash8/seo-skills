---
name: seo-ops
description: Use when you need an SEO execution workflow, research table, content brief, metadata variants, structured data, citation review, or bulk content plan.
---

# SEO Ops

Turn an SEO request into a finished, evidence-backed deliverable. This is an execution toolbox for operators with a defined site, audience, and goal.

## Operating contract

- Execute the requested operation when inputs and access are sufficient. Return a reusable prompt only when the user asks for one.
- Confirm the target URL or keyword, audience, market, language, deliverable, and permitted actions. Ask only for missing inputs that affect the result.
- Inspect the actual page and available search data. Distinguish observed findings from hypotheses and unavailable data.
- Use current official documentation for changing platform behavior, rich-result eligibility, crawler controls, and measurement definitions. Record the verification date.
- Every statistic needs a named source, date, and relevant context. Never invent a number, quote, testimonial, credential, or observation.
- Mark unresolved evidence as `[VERIFY: evidence needed]` in working material. Resolve or remove it before calling a deliverable ready for publication.
- Preserve uncertainty and source attribution. A vendor's claim is a claim, not independent proof.
- Use plain sentences, natural headings, and no em dashes in generated copy.
- Reading and drafting do not authorize publishing, changing settings, outreach, or bulk edits. Respect existing authorization and prepare a reviewable result before requesting any missing approval.

## Choose the operation

Read only the reference needed for the current job.

| Job | Reference | Related workflow |
|-----|-----------|------------------|
| Search results, question demand, keyword clusters, content scope | [Research prompts](references/research-prompts.md) | seo-audit for a broader diagnosis |
| AI answer citations and search-surface priorities | [Research prompts](references/research-prompts.md) | Use observed citations, not promised lift |
| Article, comparison, definition, or expert brief | [Content prompts](references/content-prompts.md) | verified-seo-article-writing for a sourced draft |
| Snippet rewrite, content refresh, or link plan | [Content prompts](references/content-prompts.md) | internal-linking for implementation detail |
| Answer summaries and citation-friendly rewrites | [Citation prompts](references/geo-prompts.md) | Separate citations from recommendations |
| Titles, descriptions, CTR review, schema, or image specifications | [Metadata and schema prompts](references/metadata-schema-prompts.md) | seo-quick-wins for site-wide prioritization |
| Full workflow, bulk processing, or pre-publication review | [Workflow prompts](references/workflow-prompts.md) | Keep batches reversible and measurable |

## Evidence and measurement guardrails

- A search result is a dated observation for a query, location, language, device, and session. Do not present one result as universal.
- Label generated questions and keywords as hypotheses unless demand is observed in search results or supplied data.
- Benchmark content by useful facts and answered questions. Do not turn competitor word counts, keyword density, or link counts into targets.
- Separate valid schema vocabulary from a search platform's current display eligibility. Validate both before promising a rich result.
- Do not present a citation, recommendation, referral, or conversion as interchangeable evidence.
- Inspect snippet directives and crawler policies before changing them. Search crawling, training access, and user-triggered retrieval can have different controls. Verify the relevant product's current docs.
- Treat proposed metadata as drafts until the deployed HTML and canonical URL are checked. A saved field does not prove what the public page serves.
- Keep a baseline, changed-URL cohort, untouched comparison cohort where useful, and rollback copy for bulk work.
- Never apply blind body-copy replacements to title or description fields. Preview structured fields separately and sample the rendered output.
- Keep hostname and canonical distinctions during analysis. Aggregate rows only after verifying they represent the same page, and sum metrics instead of overwriting rows.
- Falling impressions with stable position can have several causes. Inspect query mix, demand, tracking, and search features before deciding to rewrite.

## Output contract

Return:

1. Scope and evidence: inputs, sources, observation dates, limits, and assumptions.
2. Finished artifact: the table, brief, copy, markup, or plan requested.
3. Verification: checks completed, unresolved items, and any deployment boundary.
4. Next action: one concrete recommendation, owner if known, success measure, and regression guardrail.

Do not add a schema block, FAQ, statistic, product mention, or extra page merely to fill a template. Keep only what serves the reader and is supported.
