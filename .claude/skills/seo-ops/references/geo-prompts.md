# Citation-Friendly Content Prompts

Use these to improve clarity and verifiability. No wording or markup guarantees inclusion in an AI answer.

## Answer-summary block

Inputs: source page or draft, primary question, audience, verified differentiators, and output format.

1. Read the full source and identify its direct answer.
2. Write a short standalone summary that preserves important conditions and limitations.
3. Include a statistic only if it materially helps and has a named source, date, units, and context.
4. Add an audience or use-case sentence only when supported.
5. Attribute the source and actual verification date. Do not equate the run date with a content update.

Return the summary in the requested format, a source map, and a short validation note.

Check that:

- The opening answers the question without surrounding context.
- Every claim is supported by the source.
- No statistic, comparison, or superlative has been invented.
- The summary does not erase a condition that changes the answer.
- HTML is semantic and escaped correctly if requested.

Optional: use a small table for a real comparison or visible Q&A for unresolved reader questions. Do not add statistics, FAQs, or schema solely to satisfy a template.

## Citation-friendly rewrite

Inputs: existing content, query or reader task, source material, tone, and allowed scope.

- Lead with the direct answer, then explain evidence and practical detail.
- Make attribution easy to follow with primary-source links near claims.
- Preserve the source's scope, qualifiers, units, and uncertainty.
- Include expert quotations only when the words, speaker, credentials, and source can be verified.
- Use tables for actual comparisons and numbered lists for ordered processes.
- Replace vague claims with supported specifics. If evidence is missing, flag the gap in working notes or remove the claim.
- Keep normal paragraphs and coherent sections. Avoid keyword stuffing, fragment piles, and artificial quote bait.
- Separate editorial judgment, product claims, and established facts.
- Keep the requested voice without adding sales claims.

Return:

1. Rewritten copy.
2. A concise change log explaining material edits.
3. Standalone passages that summarize supported claims.
4. Sources and unresolved verification items.

For a live page, inspect current indexability, snippet directives, rendering, and relevant crawler policies. Verify each product's current docs before interpreting those controls. Do not change access policies without authorization.

## SEO and citation outcome tracking

Inputs: query set, URLs, products or modes to observe, market, business goal, baseline, and review cadence.

Keep a stable observation method and record changes to it.

| Measure | Baseline | Target and rationale | Current evidence | Observation date | Limits |
|---------|----------|----------------------|------------------|------------------|--------|
| Search visibility for intended queries | | | | | |
| Organic clicks and qualified actions | | | | | |
| Citation or source link in an answer | | | | | |
| Brand mention | | | | | |
| Explicit product recommendation | | | | | |
| Measurable referral and downstream action | | | | | |

Verification rules:

- Save the exact query, product or mode, language, market, session context, answer, and citation URLs where available.
- Mark untested surfaces as untested.
- Separate a mention, a citation, a recommendation, and a measured visit.
- Explain attribution limits in analytics, including missing or ambiguous referral data.
- Compare repeated observations and a suitable review window. One answer is not a stable market-wide result.
- Track reader or business outcomes alongside visibility.
- Do not infer revenue or conversion quality from citation counts.

If results are weak, identify the evidenced bottleneck: page accessibility, answer quality, source credibility, audience fit, distribution, or measurement. Recommend one bounded next action and a stop condition. Avoid unsupported industry multipliers and guaranteed uplift claims.
