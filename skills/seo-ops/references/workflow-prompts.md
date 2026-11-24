# Workflow Prompts

## Full SEO workflow

Inputs: topic or query, audience, market, business goal, source material, existing URL inventory, and permitted actions.

1. Inspect current search results and the existing site. Record access limits.
2. Map reader intent, observed questions, competing coverage, and available evidence.
3. Review AI answer citations only if those products matter to the goal and can be observed.
4. Create one brief with the angle, required facts, outline, sources, and success measure.
5. Present the brief or outline for approval when the agreed workflow requires it.
6. Produce the sourced draft with verified-seo-article-writing.
7. Prepare metadata, relevant structured data, image specifications, and an internal-linking plan.
8. Run the publication checklist below.
9. Publish only within existing authorization. Verify saved state and public output separately.
10. Set a review date based on topic volatility and the measurement window.

Return the article or brief, metadata, source ledger, relevant supporting assets, link plan, verification results, unresolved blockers, and review measure. Do not call a draft published or an unverified page live.

## Bulk content planning

Inputs: keyword list, current page inventory, source data, templates, business priority, and permitted batch scope.

- Cluster shared intent before proposing pages. Multiple keyword variants do not automatically justify separate URLs.
- Require useful, distinct information for each proposed page.
- Separate research hypotheses from measured demand and competition.
- Define a scoring method and label its inputs. Do not present heuristic scores as forecasts.
- Start with a small reviewable sample before expanding.
- Output planning records, not automatic publication instructions.

Suggested CSV fields:

```text
keyword,intent,existing_url,proposed_url,content_type,title,description,outline,evidence_needed,priority_reason,status
```

Use a CSV writer when generating files. Preserve newlines, quotes, commas, and spreadsheet safety for text that could be interpreted as a formula.

## Bulk edit guardrails

Before an authorized bulk rewrite:

1. Export the original content and structured fields so each changed page can be restored.
2. Capture page and query metrics for a named baseline period. Exclude the pages with the most clicks or conversion value from unattended rewrites; review them individually before including them in a batch.
3. Define an explicit changed-URL cohort and, where useful, an untouched comparison cohort.
4. Keep titles, descriptions, slugs, and body copy as separate fields. Review field-specific transformations separately.
5. Preview a representative sample, including edge cases and high-impact pages.
6. Check for repeated replacements, broken grammar, invalid markup, lost facts, and unexpected URL changes.
7. Apply the approved bounded batch, then verify saved fields and rendered pages.
8. Compare the changed cohort with the untouched cohort over matched windows. If no comparison cohort exists, label the result directional. Check whether a few high-volume pages drive the aggregate before deciding what to do about the whole batch.

Pitfall: repeated replacement rules can match earlier replacements and corrupt short metadata fields. A successful script exit is not editorial approval.

Pitfall: exports can contain separate rows for host variants or other dimensions. Preserve dimensions and verify canonical equivalence before aggregating. Sum eligible rows instead of overwriting them.

Stop and restore or re-plan if facts change, URL identity changes unexpectedly, a rollback cannot be completed, or the verified sample exposes systematic damage. Do not expand a failing batch.

## Pre-publication checklist

### Content and evidence

- [ ] The page answers the intended reader task.
- [ ] Names, numbers, quotes, credentials, product claims, and dates have appropriate evidence.
- [ ] Verification markers are resolved or the unsupported text is removed.
- [ ] The title and description describe the actual page.
- [ ] Headings and keywords read naturally.
- [ ] Attribution, limitations, and relevant disclosures are visible.
- [ ] The displayed update date reflects a real reviewed change.

### Links and images

- [ ] Internal destinations exist and match the intended canonical pages.
- [ ] Incoming links from existing pages are planned where context supports them.
- [ ] Primary-source links work and support the associated claim.
- [ ] Images are accurate, permitted for use, and have appropriate alt treatment.
- [ ] Dimensions and loading behavior have been checked on the target page.

### Technical delivery

- [ ] Status, canonical, indexability, and rendering match the intended publication state.
- [ ] Snippet and crawler directives match the owner's policy and current product docs.
- [ ] Structured data describes visible content and passes applicable validation.
- [ ] Mobile layout, accessibility, and relevant performance checks pass.
- [ ] CMS fields and public HTML have been verified after any authorized save.
- [ ] Rollback material and a measurement baseline are retained.

A checklist does not authorize a public write. Report which checks were run, which were not, and what still blocks publication.
