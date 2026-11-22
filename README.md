# SEO Skills 🔎

**Five skills. One job. Get found.** 🎯

SEO advice today is noise. Checklists from 2019. "Best practices" nobody has tested. Reports that tell you everything and change nothing.

We thought there had to be a better way. 💡

So we built five skills that do the work, check the work, and show you the proof. Give your agent a site, a search export or an article brief. Get a ranked fix list, page edits you can review, or a draft with a source beside every claim that matters.

## 🧩 The five

| | Skill | What you get |
|---|---|---|
| 🩺 | [`seo-audit`](skills/seo-audit/SKILL.md) | A ranked report on crawling, indexing, page speed and structured data. [See the report format.](examples/sample-report.md) |
| ⚡ | [`seo-quick-wins`](skills/seo-quick-wins/SKILL.md) | A queue of pages that could earn more clicks, with the exact title, content or link change for each. |
| 🔗 | [`internal-linking`](skills/internal-linking/SKILL.md) | A link plan down to the source sentence and the destination, backed by crawl or page exports. |
| 🛠️ | [`seo-ops`](skills/seo-ops/SKILL.md) | The brief, snippet, markup or batch plan you asked for. Not a prompt for writing it. The thing itself. |
| ✍️ | [`verified-seo-article-writing`](skills/verified-seo-article-writing/SKILL.md) | A sourced article, plus a record of what was corrected, attributed or left out. |

Alone, each one is useful. Together, they're a system. 🔄

The audit finds the problems. Quick wins tells you what to fix first. Internal linking and SEO ops fix it. The article writer builds what's next.

## 🚀 Install

These are [Agent Skills](https://agentskills.io/). Not a plugin for one app. They work in Claude Code, Codex, Amp, Cursor and any agent that reads skills. 🤝

Clone once, from the project where you want them:

```bash
git clone https://github.com/adityash8/seo-skills.git ../seo-skills
```

Then copy the whole skill folders, so their references stay together. The block uses `.agents/skills` for Codex and Amp. Change `SKILLS_DIR` to `.claude/skills` for Claude Code, or to the folder your agent uses.

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

If any skill name is already taken, nothing is copied. To replace installed skills, move the old folders to a backup outside the skills folder, then run the block again.

## 💬 Use it

No commands to learn. Just ask.

```text
Use seo-audit to audit example.com with public evidence. Rank the fixes and mark what you couldn't check.
Find quick wins in my Search Console export.
Plan internal links for /pricing from this crawl.
Write a verified article from this press release.
```

It just works. ✨

## 📡 Make it sharper

Public pages are enough to start an audit, if your agent can fetch them. Bring more, and the skills see more:

- 📊 **Search Console** or similar search data for quick wins
- 🕸️ **An authorized crawl or page export** for link coverage
- 🔍 **Ahrefs, Semrush or your CMS**, only when the job needs them

No credentials ship with this repo. Bring your own. 🔐

## 🧭 What we believe

- **Evidence beats opinion.** Measured data, estimates and unknowns never get mixed up.
- **Facts expire.** Search changes fast, so the skills check current docs before trusting a rule.
- **You stay in control.** An audit only looks. Nothing live changes until you say yes.

## ✅ Check the repo

```bash
python3 scripts/check.py
```

Checks skill metadata, local links, and common private-data patterns.

## 📜 License

[MIT](LICENSE). Use it. Fork it. Make it better.

And if it helps you get found, a star helps too. ⭐
