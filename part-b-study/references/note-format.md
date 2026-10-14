# Note format: the user's house style

These rules come from comparing Claude's original civil litigation output with what the user actually kept, rewrote or cut in their own notes. Where this file conflicts with an older instruction (e.g. "verbatim first, then simplified"), **this file wins**: it reflects what the user does in practice.

The user copies the output from chat into Google Docs by hand. Write in Markdown that pastes cleanly: headings, bold, bullets, block quotes and simple tables. Don't use HTML, footnotes or nested tables.

---

## 1. Heading hierarchy

| Level | Use | Example |
|---|---|---|
| `#` | The lecture, in CAPS | `# INTRO, PRE-ACTION CONSIDERATIONS, STARTING THE ACTION, & INITIAL STEPS AFTER STARTING THE ACTION` |
| `##` | A syllabus or slide section | `## Pre-Action Production: O 11 r 11` |
| `###` | A topic, written as "Topic: provision" | `### Which mode? : O 6 r 1`, `### Validity and renewal: O 6 r 3 (applies to both OC and OA)` |
| `####` | A case (see §4) | `#### (-) pre-action production only if necessary \| No SG nexus …: Dorsey …` |

- **No § numbers or "slides 4–6" labels** in headings.
- **Define abbreviations where they first appear,** e.g. Supreme Court of Judicature Act 1969 ("SCJA"), Rules of Court 2021 ("ROC2021"). Don't put an abbreviations list at the top.

## 2. Bullets and gist labels

- Every substantive bullet starts with a **bold gist label** that captures the point at a glance, followed by a colon: `**Offer terms:** offers must be in writing, open for at least 14 days, and kept secret from the court until costs are decided.`
- In fact patterns, the label is the key fact or thing: `**The trust deed:**`, `**The breach:**`, `**Voice-logs:**`, `**The clues:**`.
- Keep bullets short and plain. One idea per bullet.
- Use a `TLDR:` line to simplify a long provision or list, e.g. "TLDR: The court gets jurisdiction over a defendant in only three ways –" followed by a numbered list.
- Show sequences of steps with arrows: `(1) is there a cause of action? > (2) is the action time barred? > (3) amicable resolution > …`

## 3. Statutes, Rules of Court and Practice Directions

**Always verbatim, from the current official text** (see `research.md`). Never paraphrase from senior's notes and present it as the rule.

**Pattern A: a provision with several sub-rules.** Put each **gist first, then its own verbatim sub-rule straight underneath**. Don't put all the quotes first and all the simplified points after.

```markdown
- **"Must" isn't absolute:** even a "must" in the ROC can be departed from in the interests of justice.
  - **O 3 r 2(1)** "Unless the context otherwise requires and subject to any other written law, all requirements in these Rules are subject to the Court's discretion to order otherwise in the interests of justice, even if they are expressed using imperative words such as "must", "is to" or "shall"."
- **Gaps in the rules:** where the rules are silent, the court can do what justice requires, as long as it's consistent with the Ideals.
  - **(2)** "Where there is no express provision in these Rules or any other written law on any matter, the Court may do whatever …"
```

**Pattern B: one long provision read as a whole** (e.g. SCJA s 16, O 3 r 1, O 6 r 1, O 11 r 11). Put the verbatim text in a **block quote** (the user turns it into a boxed table in Google Docs), then a `TLDR:` line or gist bullets underneath.

```markdown
> **SCJA s 16(1)** "The General Division has jurisdiction to hear and try any action in personam where —
> (a) the defendant is served with an originating claim or any other originating process — …"

TLDR: The court gets jurisdiction over a defendant in only three ways –
1. **Service in Singapore**, done properly under the ROC2021;
2. **Service out of Singapore**, done properly and authorised under Order 8;
3. **Submission**, where the defendant voluntarily accepts the court's jurisdiction.
```

- **Abridge with "…"** where parts of the provision aren't relevant, but never change the words that remain.
- **Bracket a short descriptor** where the quote would otherwise lack context: `**s 24A(2)** [negligence/nuisance/breach of duty with personal injuries] "shall not be brought …"`
- **Copy instructor slide tables in full,** keeping their wording: e.g. the "Instructor's Table for which mode to use" decision table.

## 4. Cases

### Case heading (H4): the rule first, the case name last

```
#### (±) <rule or proposition, in the user's shorthand> | <the fact that decided it>: <Case name> <citations> (<pinpoint>)
```

Examples taken from the user's notes:
- `#### (-) pre-action production allowed when theres good cause of action | applicant already had required info for their action: Ching Mun Fong v Standard Chartered Bank [2012] 4 SLR 185; [2012] SGCA 38`
- `#### (-) pre-action discovery only if proceedings might commence in SG / SG nexus, but not forum conveniens | abuse of process found: ED&F Man Capital Markets Ltd v Straits (Singapore) Pte Ltd [2020] 2 SLR 695; [2020] SGCA 64 (at [34]–[36])`
- `#### (+) saving cost good reason for extension | writ valid but limitation expired: Lim Hong Kan v Mohd Sainudin bin Ahmad [1992] 1 SLR(R) 108; [1992] SGCA 8`

**(+)** means the rule applies, the application succeeds, or the point favours the applicant or claimant. **(−)** means it's refused, doesn't apply, or cuts against. **(+ / −)** means it can go either way (e.g. a list of factors). Add a one-line italic note under the heading only when it matters, e.g. *(A High Court Registrar's decision; persuasive, not binding.)*

### The four parts

```markdown
**1. The Ratio**
- **(+) <gist label>:** "<verbatim sentence or clause> …
  <next clause on its own line> …" (at [n])
- **(-) <gist label>:** "<verbatim>" (at [n])

**2. Factual Matrix (key facts)**
- **<Key fact label>:** <one or two plain sentences>.

**3. Legal Analysis: Holding + Hooks vs. Red Herrings**
- **Holding:** <outcome and why, with pinpoints>.
- **(+)**
  - **Hook: <fact pattern that triggers the rule>:** <explanation, example, pinpoint>.
- **(-)**
  - **Red herring: <tempting but wrong argument or fact>:** <why it fails, pinpoint>.

**4. Academic and Judicial Significance**   ← only when it has substance (see below)
- **<gist label>:** <point>.

Sources: [[2012] SGCA 38](https://www.elitigation.sg/gd/s/2012_SGCA_38) · [later case](link)
```

Rules for each part:
- **Ratio:** use the judgment's own words, with pinpoints. **Split long quotes onto separate lines at clause or principle boundaries.** For numbered principles (e.g. *Kleinwort*'s five), give each one its own line. Put a (+) or (−) on each ratio bullet where it clearly cuts one way.
- **Order by usefulness:** the test or threshold the user will apply in a hypothetical comes first. Background ("same rationale as under ROC 2014") comes after.
- **Factual matrix:** only the facts that made the rule bite, 3–5 bullets. Bold the critical facts within the sentence.
- **Hooks and red herrings:** these are the core of the notes for open-book hypotheticals. A hook is a fact pattern in a future problem that should make the user reach for this case. A red herring is a fact or argument that looks relevant but isn't. Give a pinpoint wherever the judgment supports the point. Instructor tips about applying the case go here too, with a source tag.
- **Part 4: include it only if there is real substance:**
  - a later case applying, extending, distinguishing or doubting it (with what it held);
  - tension between an old-rules case and the current rules, ending with "Argue both sides in an exam" where that's the honest position;
  - an academic criticism **you actually read**.
  - If none of these exist, **leave Part 4 out**. Don't add a filler "leading authority" line or list "further reading" you haven't checked.
- **Sources:** one short line per case. Use the eLitigation link plus any later case or commentary actually relied on.

## 5. Source tags, instructor points, corrections, untested items

- **Tag where each non-slide point came from,** inside or right after the gist label: `(CS1)`, `(CS1, Instructor)`, `(Zoom Q&A)`, `(senior's 2025 notes)`, `(CS1 + O 21 r 4)`.
- **Group several instructor remarks** under a plain `Instructor:` line or a `Zoom Q&A points:` line, with bulleted points beneath.
- **Corrections** go on their own bracketed line:
  - `[Correction to CS1: with a generally endorsed OC, the SOC is due 14 days after the OC is served (r 5(5)). The CS1 transcript says "after filing"; the rule says otherwise.]`
  - `[⚠ Your slides and senior's notes still say 3 months across the board].`
  - `Senior's 2025 notes: cites "O 6 R 11(13)". The correct reference is O 6 r 13.`
- **[untested]** goes at the very start of the bullet, followed by why: `[untested] Pre-action protocols (e.g. medical negligence, PD para 163 and Appendix H): "Background information only" (Syllabus [19]).`
- Keep [untested] items **brief**, but include them.

## 6. Exam hooks and templates: keep only the specific ones

The user kept:
- **Fact triggers that lead to concrete steps:** `**Exam hook:** "the limitation period expires in 10 days" in a hypothetical signals two things: (1) a generally endorsed OC is permitted; (2) you have reasonable grounds to skip the pre-action amicable offer. Then serve the SOC within 14 days of serving the OC.`
- **Exam templates:** a model sentence or paragraph with [blanks] for the facts, e.g. the O 5 pre-action offer template.

The user cut:
- **Generic advice:** "cite O 3 r 2(1) whenever your client has missed a deadline", "frame every argument in terms of the Ideals", "whenever a foreign defendant is involved, ask which route applies".
- **Multi-step "checklists" that only restate the cases above them.**

## 7. Tables

- **Use tables to compare categories** (thresholds, time limits, OC vs OA, which court) and to copy instructor tables across.
- Keep them simple: a header row, short cells, no nested formatting beyond bold.

## 8. Leave these out of the notes body

- **Asides addressed to the user:** "Your slides miss this one", "just skim", "low priority", "I haven't checked the exact wording". Either verify the point, or mark it `[unverified]`. Corrections that matter go in the bracketed formats from §5.
- **Process narration** ("I'm now reading…"). Process notes belong in the short "Before we start" chat section, which isn't copied.
- **A separate "Section sources" list** at the end.
