---
name: seo-audit
description: Audit SEO issues, traffic drops and site readiness with evidence and prioritized fixes. Do NOT use for recurring harvests (seo-quick-wins) or link implementation (internal-linking).
---

# SEO Audit

Run a technical SEO audit using the existing [audit procedure](references/audit-procedure.md). It contains the tool-selection workflow, audit sections, report template, execution batches, and optional stack-specific fixes.

## Before running

- Reuse inputs already provided. Identify the domain, available data sources, conversion goal, and audit scope.
- Verify platform facts, tool schemas, crawler behavior, thresholds, and structured-data eligibility against current documentation. The procedure's tool names and examples may need adaptation.
- Distinguish measured first-party data from third-party estimates and missing evidence. Do not report an unchecked section as a pass.
- Treat numerical CTR ranges, traffic projections, and impact scenarios as assumptions. Prefer the site's own comparable data and state the basis for any estimate.
- Only add statistics, ratings, prices, or other factual markup that the page and evidence support.

## Triage and priorities

- Name the business conversion goal before traffic or rankings. Separate new-customer acquisition from returning-user activity where relevant.
- For a new SEO program, assess search demand, readiness, editorial or unique-data value, a plausible commercial opportunity, and a bounded test with keep/stop criteria. Return INVEST, TEST, HYGIENE ONLY or HAND OFF with evidence. Unknown demand stays unknown.
- Social discovery does not rule out useful education about how to use, store or choose a product. Support questions justify research; they do not prove search volume.
- For established programs, prioritize confirmed crawl/indexation blockers, technical issues, on-page relevance, content quality and authority. After a core or quality update decline, put content usefulness first in both summary and action plan. Timing alone does not establish causation.
- Match technical work to demonstrated problems and site scale. A small site's lab score alone does not justify a large performance project.
- Distinguish changes to existing ranking pages from new-page launches when discussing timelines. Give conditional estimates, never promised recovery dates.

## Evidence limits

These rules apply throughout the linked procedure, including optional fixes and execution batches.

- Use first-party Search Console or analytics for the site's measured clicks, sessions and conversions; keep those measures separate. Modelled third-party traffic is an estimate, not the site's measured baseline. Verify returned geography and language scope.
- Work from supplied exports when tools or access are missing. Produce the supported findings and drafts now; identify the missing evidence for each unresolved check. Do not ask for data already supplied or invent tool results.
- Static HTML can miss JavaScript-injected structured data. Absence in a text fetch is not proof of missing schema. Use rendered-page inspection, a JavaScript-rendered export or Google's Rich Results Test before making that finding.
- Zero inlinks in an incomplete crawl does not prove a page is orphaned. Verify coverage and source pages before proposing link changes.
- A lab performance score does not establish field Core Web Vitals status or explain ranking loss. Keep unmeasured field metrics unknown.
- For multilingual sites, check reciprocal and self-referencing hreflang, correct language codes, consistent annotations, canonical conflicts and genuinely localized main content. Repair a cross-language canonical together with useful localized content; do not infer Google's selected canonical from a declared tag alone.
- A same-language regional duplicate can use a preferred canonical where appropriate; do not apply the cross-language rule blindly. Treat fallback annotations as a separate decision.

## Deliver

Use the procedure's report format:

1. Executive summary: scope, conversion goal, overall assessment, highest-priority issues, supported quick wins, conditional timeline and any investment verdict.
2. Findings: Issue, Impact, Evidence, Fix and Priority for each supported technical, on-page or content finding. Distinguish observed defects from hypotheses and unavailable checks.
3. Ordered action plan: proposed owners, dependencies, reviewable drafts or diffs, and a concrete verification check for each change.
4. Measurement: preserve the baseline, reporting windows and filters; compare business outcomes as well as search visibility. State what remains unresolved.

Do not fill revenue-opportunity, health-score or uplift fields without defensible inputs. State the missing evidence instead.

Prepare recommendations and drafts now, but explicitly require user approval before any live edit, publication, deletion or consolidation, automated rollout, or paid action. An audit request authorizes analysis, not these actions; never claim they ran without execution evidence. Respect existing explicit authorization for the specific action; request any missing approval only after preparing a reviewable result. Keep a diff, rollback path and readback verification for approved implementation.

## Follow-on work

- `seo-quick-wins`: existing-page opportunities and priorities.
- `internal-linking`: contextual links and target verification.
- `seo-ops`: research, content, metadata, schema and AI-search citation review procedures.
- `verified-seo-article-writing`: a sourced article from an approved brief.
