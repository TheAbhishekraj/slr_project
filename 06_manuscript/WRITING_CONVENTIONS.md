# WRITING_CONVENTIONS.md

**Authority:** Subordinate to `_FRESH_SESSION_PROMPT.md` and
`00_scope/MASTER_REFERENCE_BIBLE.md`. Where this file and either of those
conflict, the higher document governs, and the conflict is logged (R4).
This file consolidates writing rules; it does not create new ones.

**Scope:** Manuscript prose and presentation only. Not extraction, not
scoring, not prompt governance.

**Author of record:** Human. Mechanical rules drafted by agent from existing
sources; voice and tone section authored or approved by human.

**Status:** Phase 12 write-list amendment. Frozen once Phase 12 begins.

**Write-list status:** Not in the canonical write list as of 2026-10-03.
Writing this file requires a logged amendment in `_AUDIT/rules_log.md`.

---

## 1. Purpose

This file is the single reference for how the manuscript is written. Before
Phase 12, the rules lived in four places: `_FRESH_SESSION_PROMPT.md` §5 and
§10, `MASTER_REFERENCE_BIBLE.md` R1–R7, `AUDIT_PROMPT.md` §8, and decisions
made in session. Anyone opening the project later can read this file and know
how the prose, tables, and figures are supposed to look.

---

## 2. Historical evolution of this project

Recorded here so future sessions understand why certain rules exist. This is
not manuscript content; it does not appear in `MANUSCRIPT.md`.

### 2.1 Corpus chain (frozen 2026-10-02, Decision B)

2,000 raw records → 1,716 unique → 501 screened → 291 full-text →
4 excluded → **287 included**. Master: `04_master/MASTER_EVIDENCE.csv`,
287 × 28, SHA256
`88F94A9EB023E12502D2F12342FD658D0878C6DAA66A99986CC8F151D0D888BA`.

Excluded IDs that must never appear in any output: REC_0053, REC_0693,
REC_0866, REC_1688.

### 2.2 The governance problem

Three prompt files existed on disk. None was `_FRESH_SESSION_PROMPT.md`.
Phases 10 and 11 ran under `tools/AUTO_AGENT_COMPLETE.md`, which lacked the
gate-report requirements, PDCA structure, "no pooling" rule, and write list
of the prompt later used to audit those phases. This session resolved the
divergence by declaring `_FRESH_SESSION_PROMPT.md` canonical and reconciling
the write lists.

Lesson recorded as a rule: **one canonical prompt on disk, hashed, with a
reconciliation table showing which prompt governed which phase.**

### 2.3 Incidents and corrections

| Incident | What happened | Correction |
|---|---|---|
| Incident D-Q | Prior QA artifact (`10A726…`, tiers 143/125/19, mean 7.9756) overwritten without backup. Prior rubric not on disk. | Unrecoverable. `07_certificates/CERTIFICATE_QA_SCORING.md` retained unmodified as sole evidence. |
| Action-log append violation | A row was replaced instead of appended in `_AUDIT/action_log.md`. | Logged as deviation; append-only discipline enforced going forward. |
| Figure DPI drift | F1–F9 certified at 130 DPI, below IEEE submission minimum. | Regenerated at 300 DPI (F1 line art 600 DPI) before Gate E report; prior figure-state noted as superseded. |
| `LOCKED_NUMBERS.md` SHA drift | File changed after Gate E report (`2D14463A…` → `A783E3CC…`). | Logged; prior Gate E SHA recorded as superseded. |
| `MASTER_EVIDENCE.md` defects | §5 placeholders unfilled; §8 references non-existent `tools/build_master.py`. | Recorded. Not a manuscript artifact; do not cite. |

### 2.4 Rules derived from these incidents

1. Every number traces to a source (REC ID + file + page). No untraceable
   figures in prose, tables, or captions.
2. Every artifact has a SHA256 recorded at certification. Drift is logged.
3. Gates are human-approved. Agents produce reports; humans type passes.
4. Write lists are explicit. Anything outside is a violation.
5. Voice is human. The rules exist so the prose does not read as machine
   output.

---

## 3. Manuscript structure

Section order, target length, and content rules. Lengths are targets for
IEEE Access; adjust if the venue changes.

### 3.1 Problem statement

The opening claim of the paper, stated once, clearly. What gap does the
review fill? Why now? This is not a separate section; it is the first two
paragraphs of the Introduction and the backbone of the Abstract.

Rules:
- Name the operational setting (GPS-denied UAV navigation).
- Name the review type (systematic literature review, PRISMA).
- State the corpus size (287 included studies) once here.
- Do not open with "Unmanned aerial vehicles have become..." — that is an
  AI-tell opening. Open with the operational problem.

### 3.2 Abstract

- **Length:** ≤ 250 words. Hard cap.
- **Content:** problem (1 sentence), method (1–2 sentences: PRISMA, corpus
  size, date range), key findings (2–3 sentences with ranges, not pooled
  values), contribution (1 sentence).
- **Forbidden:** citations, figure references, undefined acronyms, hedges
  ("may potentially suggest").
- **No banned words** (§5).

### 3.3 Introduction

- **Length:** ~1,000–1,500 words.
- **Must contain RQ1–RQ4** stated as explicit research questions.
- **Must end** with a paragraph stating the paper's contributions and a
  roadmap sentence.
- Cite the problem-statement literature; do not cite the 287-corpus papers
  here unless a specific one anchors a claim.

### 3.4 Related Work

- **Length:** ~800–1,200 words.
- Prior reviews and surveys only. Distinguish this review from them
  (coverage, method, recency).
- No overlap with Methods.
- Do not re-list the 287-corpus papers here; they belong in Results.

### 3.5 Methods

- **Length:** ~1,200–1,800 words.
- PRISMA chain stated as a sequence: raw, unique, screened, full-text,
  excluded, included. Numbers must match `LOCKED_NUMBERS.md`.
- Search strategy, inclusion/exclusion criteria, extraction process, QA
  scoring rubric. Rubric stated so a reader could replicate.
- QA tier thresholds (Q-High / Q-Medium / Q-Low) defined here, not in
  Results.
- **Figure F1** (PRISMA flow) belongs here.

### 3.6 Results

- **Length:** ~2,000–3,000 words.
- Organized by RQ, in order RQ1 → RQ4.
- Every statistic cites `NUMBER_TRACE.md` (see §7).
- **Ranges, not pooled values.** If three studies report 12 m, 18 m, 25 m,
  write "12–25 m across three studies" and cite each. Do not average.
- **Strong claims name the QA tier.** "In Q-High studies, X was observed"
  rather than "X was observed."
- Tables and figures referenced in text by ID. Every table and figure is
  cited at least once.
- Figures F2–F8 belong here.
- **F9** (summary/dashboard) may close Results or open Discussion.

### 3.7 Discussion

- **Length:** ~1,500–2,200 words.
- Interpret findings; do not restate Results.
- Compare against Related Work.
- Name disagreements in the literature; do not paper over them.
- Each interpretive claim back-references the Results section that supports
  it.

### 3.8 Limitations

- **Length:** ~500–800 words.
- State corpus scope (287 studies), date range, language filter, QA tier
  distribution, and any waived cells (REC_1432, REC_1435 ablation — never
  cited as numbers).
- State method limitations (single-reviewer extraction? inter-rater
  agreement?).
- State what the review does not cover.

### 3.9 Conclusion

- **Length:** ~400–600 words.
- Restate the problem (1 sentence), the method (1 sentence), the headline
  findings (2–3 sentences, as ranges), and the takeaway.
- No new citations. No new figures. No new claims.
- Do not open with "In conclusion" (banned, §5).

### 3.10 Future Work

- **Length:** ~300–500 words.
- Concrete, not aspirational. Name specific gaps the review surfaced, not
  "further research is needed."
- Each direction ties to a specific finding from Results.
- May cite corpus papers to anchor a gap.

---

## 4. Voice and tone

This section is authored and approved by the human author. It records how the
manuscript should sound.

- **Person:** first-person plural ("we screened," "we extracted," "this
  review finds"). Do not use "the authors" or "this paper" as a self-
  reference.
- **Tense:** past for what was done (screening, extraction, scoring); present
  for what the review shows and for established facts.
- **Register:** formal academic English. No contractions. No rhetorical
  questions.
- **Sentence length:** vary. A run of short sentences reads as machine output
  as much as a run of long ones.
- **Paragraph openings:** do not open consecutive paragraphs with the same
  word or structure. Do not open with "Moreover," "Furthermore," or
  "Additionally."
- **Hedging:** use only where the evidence requires it. "Suggests" and
  "indicates" are fine when warranted; stacked hedges ("may potentially
  suggest") are not.
- **Emphasis:** no bold or italic for emphasis in body prose. Emphasis is
  carried by position and structure.
- **Numbers in prose:** spell out one through nine, use numerals for 10 and
  above, except in ranges, measurements, and statistics, where numerals
  always apply.

---

## 5. Banned words and phrases

Never appear in any manuscript output. This list is the **superset** of
`MASTER_REFERENCE_BIBLE.md` R7 and `AUDIT_PROMPT.md` §8. The stricter list
applies.

**Banned outright:**
- delve
- landscape (as metaphor)
- crucial
- pivotal
- state-of-the-art (unless a named baseline follows in the same sentence)
- It is important to note
- It should be noted
- In conclusion
- very
- really

**Banned as paragraph openers:**
- Moreover
- Furthermore
- Additionally

**Banned in Abstract and Conclusion:**
- All of the above
- Any hedge stack (e.g., "may potentially suggest")

---

## 6. Spelling

American English throughout. Common pairs to enforce:

| Use | Do not use |
|---|---|
| analyze | analyse |
| behavior | behaviour |
| color | colour |
| modeling | modelling |
| center | centre |
| defense | defence |
| optimize | optimise |
| recognize | recognise |

Acronyms: spell out on first use, define in text, then use the acronym.
Do not redefine in each section.

---

## 7. Numbers and claims

**Traceability rule.** Every number in prose, tables, figures, and captions
must appear in `06_manuscript/NUMBER_TRACE.md` with:
`value | source file | REC ID or column | quote or page reference`.

**No pooling.** Report ranges across studies, never averages across studies
unless a study itself pooled. Applies to prose, tables, figures, and
captions.

**QA tier.** Any strong claim names the QA tier of the studies it rests on.
"Q-High studies report X" is acceptable. "Studies report X" is not, when the
tier matters.

**Waived cells.** REC_1432 and REC_1435 ablation fields are waived. Never
cite them as numbers. May be mentioned as "waived in extraction" if needed.

**NOT_REPORTED.** Absent fields are written `NOT_REPORTED`. Never invent,
never interpolate, never infer a value.

**Excluded IDs.** REC_0053, REC_0693, REC_0866, REC_1688 must never appear in
any manuscript output.

---

## 8. Text format

- **Headings:** Title Case for H1 and H2. Sentence case for H3 and below.
- **Section numbering:** decimal (1, 1.1, 1.1.1). Matches IEEEtran.
- **Citations in text:** IEEE style, bracketed numerals `[1]`, `[1]–[3]`,
  `[1], [4]`.
- **Figure references:** `Fig. 1`, `Figs. 1–3`. Capital F, period after Fig.
- **Table references:** `Table I`, `Tables I–III`. Roman numerals.
- **Equation references:** `(1)`, `(1)–(3)`.
- **Em dashes:** use sparingly. Prefer commas, parentheses, or a new sentence.
- **Lists:** bulleted lists only in Methods and Limitations. Not in
  Introduction, Related Work, or Discussion.
- **Footnotes:** do not use. Move the content into the body or a table note.

---

## 9. Table format

- **Caption above the table.** Sentence case. No terminal period.
- **Column headers:** Title Case, units in parentheses.
- **Column order (standard):** identifier | category | value | unit |
  source. Adjust per table but keep source last.
- **Decimal places:** consistent within a column. Report the precision the
  source gives; do not add precision.
- **Units:** SI, stated in the header. Do not repeat unit in every cell.
- **Missing values:** `NOT_REPORTED` (exact string, no italics).
- **Empty cells:** never. Every cell has a value or `NOT_REPORTED`.
- **Row order:** by category, then by REC ID, unless the table is ranked.
- **Numbering:** Table I, Table II, ... Roman numerals.
- **Every table cited in text** at least once.

---

## 10. Figure format

- **Caption below the figure.** Sentence case. No terminal period.
- **DPI:** 300 for filled charts, 600 for line art and the PRISMA flow (F1).
- **Width:** double-column 7.16 in default. Single-column 3.5 in only if a
  chart reads poorly at full width (flag to human; do not decide).
- **Fonts:** sans-serif, minimum 8 pt at print size.
- **Palette:** colorblind-safe. No red/green as the only differentiator.
- **Axis labels:** include units. Title Case.
- **Legends:** inside the plot area if space permits, otherwise below.
- **Numbering:** Fig. 1, Fig. 2, ... Arabic numerals.
- **F1** is the PRISMA flow and lives in Methods.
- **F2–F8** live in Results.
- **F9** may close Results or open Discussion.
- **Every figure cited in text** at least once.
- **Figure SHAs recorded** after regeneration and after any Phase 13 DPI
  change.

---

## 11. Naming

- **File names:** no `_v2`, `_v3`, `_final`, `_new`, `_287` suffixes.
- **REC IDs:** exactly as in the card set (`REC_0001` through `REC_1759`,
  zero-padded to four digits).
- **Figure IDs:** `F1.png` through `F9.png`. No zero-padding.
- **Table IDs:** Table I, Table II, ... in-text only; no separate files.
- **Section IDs:** decimal, as in §8.
- **BibTeX keys:** `firstauthorlastnameYYYYkeyword` (e.g., `smith2023gnss`).
  Lowercase. No underscores except before keyword.

---

## 12. References

- **Source:** `04_master/MASTER_EVIDENCE.csv` only. No external sources.
- **Format:** IEEEtran BibTeX. Entry types: `@article`, `@inproceedings`,
  `@techreport`.
- **Missing fields:** `NOT_REPORTED` written literally. Never invent a DOI,
  venue, or year.
- **Ordering:** by first citation in text.
- **Duplicates:** merge by DOI if present, else by title + first author.
- **Recency:** no constraint, but the review period ends at the corpus date.
- **`references.bib` is generated, not hand-edited.** If a fix is needed,
  fix the master and regenerate.

---

## 13. Anti-patterns

These have appeared in the project or are common AI tells. None should
appear in the manuscript.

| Anti-pattern | Example | Replace with |
|---|---|---|
| Empty opener | "Unmanned aerial vehicles have become increasingly important in recent years." | "GPS-denied navigation is required in [operational settings]." |
| Stacked hedges | "may potentially suggest" | "suggests" or "indicates" |
| Tricolon filler | "fast, reliable, and efficient" | name the specific property |
| Not only X but also Y | "not only improves accuracy but also reduces latency" | two sentences |
| Em-dash chain | "three factors — A, B, C — drive the result" | "three factors drive the result: A, B, and C" |
| Named-baseline gap | "state-of-the-art performance" | name the baseline and metric |
| Empty transition | "Moreover, it is important to note that" | start the sentence with the claim |
| Self-referential intro | "This paper aims to..." | "We review..." |
| Undefined acronym in Abstract | "GNSS" without expansion | expand on first use |
| Pooled mean across studies | "mean error was 15 m" | "12–25 m across three studies" |

---

## 14. Proposals channel

This file does not authorize the agent to improvise. If the agent identifies
a better convention, format, or phrasing rule, it surfaces the idea in the
PDCA `PROPOSALS` block and continues with the convention as written here.

Adopted or rejected proposals are logged in `_AUDIT/rules_log.md` with status
`PROPOSED` / `ADOPTED` / `REJECTED` and a one-line rationale.

The agent's judgment is reported, not exercised. This is not an invitation to
override R4, R7, or the write list.

---

## 15. Session decision log

Decisions made in the session that produced this file. Recorded so future
sessions can trace the reasoning.

| Date | Decision | Rationale |
|---|---|---|
| 2026-10-03 | `MANUSCRIPT.md` canonical; any `.tex` is a Phase 13 derivative | Only `MANUSCRIPT.md` is in the write list and compliant with the naming rule |
| 2026-10-03 | `LOCKED_NUMBERS.md` canonical (not `LOCKED_NUMBERS_287.md`) | `_287` suffix forbidden by naming rule |
| 2026-10-03 | F1–F9 regenerated at 300 DPI (F1 at 600 DPI) before Gate E report | Certify the submission figures, not a superseded set |
| 2026-10-03 | Figure widths default 7.16 in; narrow charts flagged for human override | Uniformity is defensible; per-figure judgment reserved to human |
| 2026-10-03 | Venue default IEEE Access; final call reserved | 287-study review exceeds RA-L page cap; T-RO viable but unusual for SLRs |
| 2026-10-03 | `AUDIT_PROMPT.md` §8 banned-word superset applies | Stricter of two lists governs |
| 2026-10-03 | `06_manuscript/WRITING_CONVENTIONS.md` created as Phase 12 write | Consolidates scattered rules into one reference |
| 2026-10-03 | `_FRESH_SESSION_PROMPT.md` written as human carve-out | Outside enumerated write list; logged as carve-out |
| 2026-10-03 | `06_manuscript/action_log.md` retained unmodified | Exists; not in canonical write list; all new action-log writes go to `_AUDIT/action_log.md` only |
| 2026-10-03 | `tools/score_quality.py` retained as non-canonical duplicate | Byte-identical to `05_analysis/score_quality.py`; no reason to delete |
| 2026-10-03 | Proposals channel added (§14) | Agent surfaces better ideas; human decides; no improvisation |

---

*End of file. Frozen on first write of Phase 12.*


## §14.1 — Stop-condition override

A human instruction that trips a stop condition is not automatically
an authorization. The agent must flag the conflict and obtain explicit
confirmation before acting. Silence is not consent. Impatience is not
consent.
