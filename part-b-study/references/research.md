# Research: getting verbatim text and cases right

The user is preparing for an exam, so a wrong quote or an outdated rule does real harm. Every verbatim passage must come from a primary source you actually read in this session. Anything you couldn't verify is marked `[unverified]`, never filled in from memory or from senior's notes.

## Where to get each kind of source

| What | Source | How to access it |
|---|---|---|
| Singapore Acts and subsidiary legislation, incl. the Rules of Court 2021 | Singapore Statutes Online, `https://sso.agc.gov.sg` (ROC 2021 is `https://sso.agc.gov.sg/SL/SCJA1969-S914-2021`) | Scripted downloads are blocked, so open it in the **built-in browser** (`preview_start` with the URL, then `get_page_text`). Check the "as at" date and the amendment notes (e.g. `[S 780/2023 wef 01/12/2023]`). |
| Supreme Court Practice Directions 2021 | `https://epd2021-supremecourt.judiciary.gov.sg` | WebFetch or the browser. |
| Singapore judgments | eLitigation: the HTML judgment at `https://www.elitigation.sg/gd/s/<YYYY>_<COURT>_<N>` (e.g. `2012_SGCA_38`) | The PDF usually downloads with curl from `https://www.elitigation.sg/gd/gd/<YYYY>_<COURT>_<N>/pdf`. Save it to the scratchpad, run `pdftotext`, then grep. |
| Older or English cases | eLitigation (many old SGCA cases are there), BAILII, the National Archives' Find Case Law (`caselaw.nationalarchives.gov.uk`) | WebFetch or the browser. |
| Later cases and commentary | WebSearch, e.g. `"<case name>" applied OR distinguished site:elitigation.sg`, plus SAL Academy Publishing (SAcLJ, SAL Practitioner), law firm briefings | Cite a commentary only if you read it. |
| Paywalled sources (LawNet, Lexis, Westlaw) | — | **Don't** log in. If a source is only behind a paywall, tell the user and mark the point `[unverified]`. |

## Always check for amendments

The slides and senior's notes may be out of date (the date of the senior's notes is in `course-map.md`). For every rule you quote, check the current official version. Where it differs from the slides or senior's notes, flag it in the notes with `[⚠ …]` and mention it in "Before we start". Record it in the course map's "Amendments" list with the date you checked.

## Use helper agents for case research to keep the main context lean

Judgments are long. Reading them in the main conversation is the biggest cause of context bloat. For each case, or small group of related cases, start a `general-purpose` helper agent with a prompt like the template below. Start independent cases **in parallel in a single message**. While they run, you can draft the statute sections.

```
Research this Singapore case for a law student's exam notes. Return ONLY what is asked; do not return the judgment text.

Case: <name and citation>
Why it's in the course: <the proposition the instructor or slide uses it for>
Course context: <module, e.g. Singapore civil procedure under the Rules of Court 2021>

How to get it: eLitigation PDF via curl https://www.elitigation.sg/gd/gd/<YYYY_COURT_N>/pdf, save it to <scratchpad>, run pdftotext and grep. Fall back to WebFetch on https://www.elitigation.sg/gd/s/<YYYY_COURT_N>. For older or foreign cases, use BAILII or the National Archives' Find Case Law.

Return:
1. RATIO: the 2-5 passages that state the rule(s), quoted EXACTLY (copy, don't retype) with paragraph pinpoints. For each one, give a 3-6 word gist label and say whether it cuts for (+) or against (-) the applicant or claimant.
2. KEY FACTS: 3-5 bullets of only the facts that made the rule apply, each with a short label.
3. HOLDING: 1-2 sentences, with pinpoints.
4. HOOKS / RED HERRINGS: facts or arguments the court treated as decisive (hooks) or rejected as irrelevant or insufficient (red herrings), each with a pinpoint.
5. LATER TREATMENT: search for later Singapore cases (and under the current rules, if the case was decided under older rules) that applied, extended, distinguished or doubted it. Give the citation, what was held and the pinpoint. Say "none found" if so.
6. ACADEMIC CRITICISM: only commentary you actually opened and read, with a link. Say "none found" if so.
7. SOURCES: the URLs you used.

Mark anything you could not verify as [unverified]. Never fill gaps from memory.
```

When results come back, **spot-check one quote per case** against the source if anything looks off: a pinpoint that seems wrong, or wording that sounds paraphrased. Then write the case in the house style (`note-format.md` §4).

For statutes, a helper agent is worth it only when many provisions have to come from one long Act. For a handful of rules, get them yourself through the browser and quote only the sub-rules you need.

## Senior's notes and older rules

- **Senior's notes** are a guide to which cases matter and how earlier cohorts understood them. They are never a source of verbatim text. Check every citation in them, because they contain errors (e.g. "O 6 R 11(13)" for O 6 r 13, or "SCJA" for State Courts Act provisions).
- **Notes from before a rules change** (e.g. notes written under ROC 2014) are useful for case summaries only. Old-rules cases may still apply if the new provision is the same or materially similar. Say so, and cite a current-rules case or White Book paragraph that treats it as still applicable if one exists.
- **Use the current terminology** even when quoting an old-rules case in your own words (e.g. OC, not "writ"; production, not "discovery"; OA, not "OS"). Inside verbatim quotes, keep the original words.
