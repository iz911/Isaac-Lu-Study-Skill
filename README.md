# part-b-study: a Claude Code skill for Singapore law exam prep

A study-partner skill for [Claude Code](https://claude.com/claude-code). It acts as a Singapore law professor and walks you through one lecture at a time (Part B / bar course modules such as civil litigation, criminal litigation, ethics, conveyancing, corporate practice). It produces copy-ready study notes with:

- verbatim statute and Rules of Court text, checked against the current official version
- verbatim case ratios with pinpoints, key facts, **hooks and red herrings** for open-book hypotheticals
- `[untested]` labels for syllabus items marked background-only
- source tags and `[Correction …]` / `[⚠ …]` flags where slides or seniors' notes are out of date

It also keeps a per-module `course-map.md` so each lecture can be done in a fresh chat.

## Install

Copy the `part-b-study` folder into your Claude Code skills directory:

```bash
# macOS / Linux
cp -r part-b-study ~/.claude/skills/

# Windows (PowerShell)
Copy-Item -Recurse part-b-study $env:USERPROFILE\.claude\skills\
```

Then run `/part-b-study` inside your module folder, or just say "take me through Lecture 1".

## What's inside

| File | Purpose |
|---|---|
| `part-b-study/SKILL.md` | The workflow: intake, convert sources, research, write notes, update course map |
| `part-b-study/references/note-format.md` | The note house style (headings, gist labels, 4-part case format, verbatim rules) |
| `part-b-study/references/research.md` | Where to get verbatim text (SSO, eLitigation, Practice Directions) and the helper-agent prompt |
| `part-b-study/templates/course-map.md` | Template for the per-module progress index |
| `part-b-study/scripts/extract_text.py` | Converts PDF / DOCX / PPTX / transcripts to text so Claude can grep instead of reading whole files |

## Requirements

- Claude Code
- Python 3 with `pymupdf` (or `pypdf`) for PDFs, `python-docx` for Word files, optionally `python-pptx`:
  `pip install pymupdf python-docx python-pptx`

## Using this outside Claude Code

The skill is a standard `SKILL.md` folder (name and description header, plus reference files and a script), the same layout as the open Agent Skills format. Recent reports say ChatGPT now accepts skills in that format, under its Plugins area in a Skills tab, but availability depends on your plan and workspace settings. Check OpenAI's help centre for the current steps. If upload is blocked or marked "Needs Review", the fallback is to paste `SKILL.md` and the two files in `references/` into a Custom GPT's instructions or a ChatGPT Project.

Things that may not carry over:
- **Parallel case research:** the helper-agent step is a Claude Code feature. Ask the assistant to research one case at a time instead.
- **Fetching Singapore Statutes Online / eLitigation:** this relies on browsing tools. If they fail, paste the verbatim text yourself and have the assistant mark anything else `[unverified]`.
- **`scripts/extract_text.py`:** needs a local Python environment. Elsewhere, upload text or PDFs and ask for slide or page references.
- **Course map:** progress tracking relies on writing `course-map.md` into your module folder, which a chat-only setup can't do. Paste the map in at the start of each chat.

## Customising

The note style in `references/note-format.md` is one student's preferences. Fork it and edit to suit yours. The skill can also learn differences from your old notes and records them in the course map.

## Disclaimer

This is a study aid, not legal advice. Always verify quotes and citations against the primary source before relying on them in an exam or in practice. You are responsible for respecting the copyright and terms of your own course materials: this repo contains no course content.

## License

MIT
