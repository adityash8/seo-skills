# SEO Skills 🔎

**Find what’s costing you search traffic. See what to fix first.**

Give your agent a site, a search export, or an article brief. Get a ranked fix list, page edits you can review, or a draft with sources beside the claims that matter.

## Pick your starting point

| Skill | What you get |
|---|---|
| [`seo-audit`](skills/seo-audit/SKILL.md) | A ranked report on crawling, indexing, page speed, and structured data. [See the report format.](examples/sample-report.md) |
| [`seo-quick-wins`](skills/seo-quick-wins/SKILL.md) | A queue of existing pages that could earn more clicks, with specific title, content, or link changes. |
| [`internal-linking`](skills/internal-linking/SKILL.md) | A link plan down to the source sentence and destination, backed by crawl or page exports. |
| [`seo-ops`](skills/seo-ops/SKILL.md) | The brief, snippet, markup, or batch plan you asked for, not just a prompt for writing it. |
| [`verified-seo-article-writing`](skills/verified-seo-article-writing/SKILL.md) | A sourced article and a record of what was corrected, attributed, or left out. |

## Install and try it ⚡

These are [Agent Skills](https://agentskills.io/), not a plugin for one client. From the project where you want to use them, clone this collection once:

```bash
git clone https://github.com/adityash8/seo-skills.git ../seo-skills
```

Copy the whole skill folders so their references stay together. The block uses `.agents/skills` for Codex and Amp. Change `SKILLS_DIR` to `.claude/skills` for Claude Code or to the directory documented by your agent.

```bash
(
  SKILLS_DIR=.agents/skills
  for source in ../seo-skills/skills/*; do
    target="$SKILLS_DIR/${source##*/}"
    if [ -e "$target" ] || [ -L "$target" ]; then
      printf 'Install stopped: %s already exists.\n' "$target" >&2
      exit 1
    fi
  done
  mkdir -p "$SKILLS_DIR" && cp -R ../seo-skills/skills/* "$SKILLS_DIR/"
)
```

If any skill name conflicts, nothing is copied. To replace installed skills, move the conflicting folders to a backup location outside the skills directory, then rerun the copy block. Open the project in your agent and ask:

```text
Use seo-audit to audit example.com with public evidence. Rank the fixes and mark what you couldn't check.
```

Public pages are enough to start a technical audit if your agent can fetch them. For quick wins, bring Search Console or comparable search data. For link coverage, bring an authorized crawl or page export. Connect Ahrefs, Semrush, or a CMS only if the job needs it. The skills include no credentials and require your approval before live changes.

From the cloned repo, run `python3 scripts/check.py` to check skill metadata, local links, and common private-data patterns.

[MIT License](LICENSE)
