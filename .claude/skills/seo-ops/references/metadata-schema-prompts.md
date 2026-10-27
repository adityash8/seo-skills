# Metadata, Schema, and Image Prompts

## Title and description variants

Inputs: URL, current HTML title and description, visible page content, primary intent, audience, brand rules, and optional query-performance data.

1. Fetch the page and confirm its canonical URL, indexability, H1, and actual rendered offer or answer.
2. Identify the reader's reason to click. Keep promises within what the page delivers.
3. Write distinct title and description variants with a short rationale for each.
4. Check uniqueness, readability, factual support, and truncation risk with an appropriate preview.
5. Verify platform guidance against current docs. Character counts and pixel previews are aids, not guarantees of displayed text.

Return:

| URL | Current title | Proposed title | Proposed description | Intent and rationale | Verification |
|-----|---------------|----------------|----------------------|----------------------|--------------|

- Put the important idea early without forced keyword repetition.
- Do not invent dates, prices, rankings, urgency, or numerical benefits.
- Keep a record of current fields for rollback.
- After an authorized update, read back the saved fields and inspect public HTML. Check cache behavior before calling the change deployed.

## Organic CTR review

Inputs: query and page export, date range, comparison period, market, device, search appearance, and current metadata.

- Compare like-for-like cohorts and inspect query mix, position, impressions, and relevant search features.
- Treat low CTR as a diagnostic signal. Avoid universal CTR benchmarks or a presumed metadata cause.
- Separate a ranking change, demand change, display change, and copy hypothesis.
- Use seo-quick-wins for broader opportunity triage.
- Recommend a small, reversible test with a baseline and success metric.

Return a prioritized URL list with evidence, proposed copy, confounders, review date, and rollback condition. Do not promise a lift or assume the search engine will display the submitted copy.

## Schema generation

Inputs: URL, page type, visible content, current markup, and implementation constraints.

1. Fetch the page and inventory existing markup before adding more.
2. Select types that describe the actual content and entities.
3. Verify current official documentation for supported search features and eligibility.
4. Distinguish schema vocabulary validity from eligibility for a particular rich result.
5. Generate valid JSON-LD using only verified values. Omit unsupported properties.
6. Check for conflicting duplicate entities or plugin-generated markup.
7. Validate syntax and vocabulary, then use the relevant search platform's test where applicable.
8. After an authorized deployment, inspect rendered markup and available indexing or enhancement reports.

| Content | Possible vocabulary to assess | Required checks |
|---------|-------------------------------|-----------------|
| Organization information | Organization, WebSite | Real entity details and stable identifiers |
| Article | Article, BlogPosting, Person | Visible authorship and truthful dates |
| Product or offer | Product, SoftwareApplication, Offer | Current visible features, pricing, and availability |
| Reviews | Review, AggregateRating | Genuine visible reviews and current platform policy |
| Navigation | BreadcrumbList | Matches the visible site hierarchy |
| Location or event | LocalBusiness, Event | Verified location, time, status, and eligibility |
| Definition or Q&A | DefinedTerm, FAQPage | Vocabulary fit and current display eligibility |

Return the markup, evidence map, implementation location, validation results, and honest expected benefit. Do not fabricate reviews or dates, imply all vocabulary earns a search feature, or promise AI citations from markup.

## Image specifications

Inputs: article or page, visual purpose, brand constraints, rights requirements, and delivery environment.

| Placement | Reader benefit | Image brief | Alt treatment | Caption or source | Delivery requirements |
|-----------|----------------|-------------|---------------|-------------------|-----------------------|

- Use accurate diagrams or data visuals when they explain the topic. Do not turn generated imagery into documentary evidence.
- Describe informative images in alt text; use empty alt text for purely decorative images where appropriate.
- Do not insert keywords that do not describe the image.
- Specify dimensions, responsive variants, format, compression, and reserved layout space.
- Assess loading priority for the main visible image before applying lazy loading.
- Verify current performance guidance and measure the actual page after changes.
- Confirm rights, provenance, captions, and factual accuracy before publication.
