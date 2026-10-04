# Phase 1 — Manuscript Review Against Its Own Guidelines

> **Status:** Review only. No edits. No writes to existing files.
> **Sources checked:** MANUSCRIPT.md, WRITING_CONVENTIONS.md, SUBMISSION_CHECKLIST.md, FORMATTING_STANDARDS.md

---

## 0. Global Word-Frequency Analysis

Before per-section review, a frequency scan of key patterns across the full 6,059-word manuscript:

| Pattern | Count | Concern |
|---|---|---|
| "this review" | 17 | Overuse — monotonous self-reference |
| "the corpus" | 29 | Overuse — dominates nearly every paragraph |
| "the field" | 12 | Overuse — generic, impersonal |
| "robust" | 12 | Buzzword-adjacent, though not banned |
| "gap" / "gaps" | 14 / 8 = 22 | Hammered relentlessly |
| "critical" | 12 | Near-buzzword saturation |
| "significant" | 8 | High for a 6K-word paper |
| "substantial" | 7 | High for a 6K-word paper |
| "deployment" | 14 | Repetitive technical noun |
| "mission-critical" | 7 | Formulaic repeated phrase |
| "resilience" / "resilient" | 7 / 1 = 8 | Thematic but over-concentrated |
| "Consequently" | 5 | Formulaic transition |
| "not supportable" | 5 | Same caveat stated 5 times verbatim |
| "First," / "Second," / "Third," / "Finally," | 4 / 4 / 4 / 3 | Ordinal enumeration pattern used twice (Intro + Discussion), AI tell |
| "we" / "We" | 0 / 0 | Convention says use "we"; manuscript never does |
| Banned words (delve, landscape, crucial, pivotal, etc.) | 0 | Clean |

---

## 1. Abstract (Line 10)

| Issue type | Line | Verbatim snippet | Finding |
|---|---|---|---|
| Convention: word count | L10 | (full abstract) | SUBMISSION_CHECKLIST reports 191 words. Convention cap is 250. Compliant. |
| Convention: no citations | L10 | — | No citations in Abstract. Compliant. |
| Convention: no undefined acronyms | L10 | "GPS-denied" expanded as "Global Positioning System-denied" | Compliant. |
| AI-tell: repetition from Intro | L10, L30 | "192 of 287 studies (67%) evaluate mixed operational environments, 99 of 287 investigations (34%)..." | The Abstract's key findings are repeated nearly verbatim in the Introduction (L30). Both the Abstract and L30 share the same three-stat sequence (192/287, 99/287, 5/287) in the same order with near-identical phrasing. A human author would rephrase at least one instance. |
| AI-tell: one long paragraph | L10 | Entire abstract is a single paragraph, ~191 words | Convention says 150-250. This is fine structurally but reads as a compressed dump rather than a shaped summary. |
| Readability | L10 | "quantitative sensor-combination synthesis is not supportable, and sensor families are reported via derived primary classifications" | This sentence is inside the Abstract and is opaque to a general reader. The caveat is appropriate for Methods/Limitations but clutters the Abstract. |

---

## 2. Section 1: Introduction (Lines 16-33)

| Issue type | Line | Verbatim snippet | Finding |
|---|---|---|---|
| Convention: length | — | 691 words | Target is 1,000-1,500 (WRITING_CONVENTIONS L110). Significantly short. |
| Convention: RQ1-RQ4 present | L25-28 | RQ1-RQ4 stated | Compliant. |
| Convention: contributions paragraph | L30 | "The contributions of this systematic review..." | Present. Compliant. |
| Convention: roadmap sentence | L32 | "The remainder of this paper..." | Present. Compliant. |
| AI-tell: repeated opening | L18 | "Autonomous navigation in GPS-denied environments..." | This sentence opens L18 (para 1, sentence 1) and is echoed in L18 (para 1, sentence 4): "Autonomous navigation in GPS-denied environments requires robust multi-sensor fusion." The identical phrase opens both the section and reappears 3 sentences later. |
| AI-tell: double definition | L18 | "Global Positioning System (GPS)" then "Global Positioning System (GPS) or broader Global Navigation Satellite System (GNSS)" | GPS is defined twice in the same paragraph. First at the start, then again in sentence 2. A human author would define once. |
| AI-tell: formulaic contributions list | L30 | "First, synthesis reveals... Second, 99 of 287... Third, only 5 of 287... Finally, because sensor extraction..." | Four-item enumeration with First/Second/Third/Finally structure. This exact pattern is repeated in the Discussion (L241-247). Using the same ordinal scaffold twice in one paper is a machine-generation tell. |
| Missing: no literature citations | L18-20 | Paragraphs 1-2 discuss "existing literature reviews and surveys" | No citations given. Convention (L114) says: "Cite the problem-statement literature." The Introduction discusses prior reviews generically without naming any. |
| Voice: impersonal | L22 | "this review systematically synthesizes" | Convention says use "we" (WRITING_CONVENTIONS L192-194). The entire Introduction uses "this review" instead of "we." |

---

## 3. Section 2: Related Work (Lines 35-45)

| Issue type | Line | Verbatim snippet | Finding |
|---|---|---|---|
| Convention violation | L37 | "Rather than summarizing prior surveys, this review groups the primary evidence base" | WRITING_CONVENTIONS L117-123 says Related Work should contain "Prior reviews and surveys only" and "Do not re-list the 287-corpus papers." The section explicitly does the opposite. |
| Missing: no prior review citations | L37-43 | Entire section | Not a single prior review or survey is cited by name. The section discusses "a substantial portion of the collected literature" and "a significant volume of literature" — all from the corpus, none from prior reviews. This makes the section a corpus summary, not a Related Work section. A reviewer will notice that no prior survey is named or compared against. |
| Corpus citations in wrong section | L45 | "[REC_0010], [REC_0489], [REC_1083], [REC_1084], [REC_1085]" | Five corpus citations appear here. These are the ONLY in-text citations in the entire manuscript (repeated at L218). The convention says corpus citations belong in Results, not Related Work. |
| AI-tell: paragraph structure | L39-43 | Four paragraphs: sensors, algorithms, environments, adversarial | Each paragraph is a neat thematic bucket. The parallelism is too clean — each paragraph introduces a "cluster" with the same structure: topic sentence, sensor list, elaboration. |
| Readability | L37 | "this section examines the primary thematic clusters within the corpus" | This sentence tells the reader what the section will do instead of doing it. Academic convention frowns on meta-commentary that delays content. |

---

## 4. Section 3: Methods (Lines 47-87)

| Issue type | Line | Verbatim snippet | Finding |
|---|---|---|---|
| Convention: length | — | 973 words | Target 1,200-1,800 (WRITING_CONVENTIONS L127). Short by ~230 words. |
| Convention: Fig. 1 placement | L63-65 | Fig. 1 referenced and placed | Compliant — in Methods per convention. |
| Convention: PRISMA chain | L61 | "2,000 raw harvested... 287 studies" | Chain matches LOCKED_NUMBERS.md. Compliant. |
| Convention: QA rubric replicable | L79-81 | Rubric described in detail | Compliant — a reader could replicate. |
| Kappa disclaimer | L83 | "Whether this calibration was performed during the project could not be verified from the available audit records" | Honest and appropriate. However, the phrasing is unusual — it speaks about the project in the third person as if the author does not know what happened in their own project. A reviewer may question this. |
| AI-tell: passive evasion | L83 | "could not be verified from the available audit records" | This reads as if an AI audited the project rather than the author describing their own methods. A human author would write: "We did not perform dual-appraiser calibration" or "Dual-appraiser calibration was not performed." |
| Methods in wrong subsection | L87 | "Effect measures, certainty assessment, and per-study results are not reported..." | This sentence belongs in Limitations, not in Section 3.7. The subsection is titled "Limitations of the review method" but it is inside Methods. This creates a structural oddity — Limitations appear in both Section 3.7 and Section 6. |
| Double limitations sections | L85-87, L251-270 | Section 3.7 + Section 6 | Both discuss the same limitations. Section 3.7 covers PRISMA-specific gaps; Section 6 covers them more broadly. There is overlap but not full duplication. A reviewer may see this as padding. |

---

## 5. Section 4: Results (Lines 90-231)

| Issue type | Line | Verbatim snippet | Finding |
|---|---|---|---|
| Convention: length | — | ~1,496 words | Target 2,000-3,000 (WRITING_CONVENTIONS L138). Short by ~500+ words. |
| Convention: F2-F8 in Results | L123-224 | F2, F3, F4, F5, F6, F7, F8 present | Compliant. |
| Convention: every table/figure cited | — | — | All tables (I-V) and figures (F1-F9) are cited in text. Compliant. |
| Table V: "Remaining 11 categories" | L200 | "Remaining 11 categories \| 11 \| 3.8" | Vague. A reviewer will ask what these 11 categories are. The 11 categories with 1 study each are named in LOCKED_NUMBERS.md (L22-25) but collapsed to a single row in the table. This loses information and looks evasive. |
| Table IV: row ordering | L156-163 | NOT_REPORTED (2) appears before HYBRID_VTOL (3) | NOT_REPORTED should sort last per convention (WRITING_CONVENTIONS L316: "by category, then by REC ID"). HYBRID_VTOL (3) sorts above NOT_REPORTED (2) alphabetically but is placed below it. Table rows are not sorted by count or alphabetically. |
| Table III: percentage mismatch | L134, L140 | "67.0%" in text vs "66.9%" in table | Text at L134 says 192/287 = "67.0%"; Table III at L140 says "66.9%". 192/287 = 66.899% which rounds to 66.9%. The text rounds up, the table rounds down. Pick one. |
| Table IV: platform count mismatch | L150, L158 | "OTHER (17)" in text vs "OTHER \| 18" in table | Text at L150 says "OTHER (17)"; Table IV at L158 says "OTHER \| 18." One of these is wrong. See also action_log.md L47 which documents this as a known edge case (REC_1248). |
| RQ2: accuracy not answered | L168 | "Accuracy is therefore reported as NOT_REPORTED at the aggregate level" | RQ2 asks about localization accuracy. The section reports environment and platform counts but never answers the accuracy question. The answer is "we cannot report accuracy" — which is honest but means the RQ is effectively unanswered. |
| Section 4.4: taxonomy distribution vs. limitations | L220 | "CORE (270), IMPORTANT (11), NOT_REPORTED (5), and PERIPHERAL (1)" | This taxonomy distribution describes contribution types, not limitations. The section is titled "Limitations and adversarial conditions" but the taxonomy counts do not address limitations. The Fig. 7 reference shows quality tiers, not limitations. |
| Section 4.5: belongs in Discussion | L227-231 | "Cross-cutting synthesis" | This entire subsection is interpretive, not reporting results. It makes claims like "the field's rapid advancement... has significantly outpaced its commitment" — this is Discussion material. WRITING_CONVENTIONS L136 says Results is "organized by RQ, in order RQ1-RQ4." Cross-cutting synthesis is Discussion. |
| Fig placement: F4, F6 in wrong RQ section | L174, L178 | F4 (Real vs Sim) and F6 (Geography) appear in RQ2 section | F4 describes validation type (RQ3 material). F6 describes geography (not tied to any RQ). Both appear under Section 4.2 (RQ2: accuracy and environments). |

---

## 6. Section 5: Discussion (Lines 233-249)

| Issue type | Line | Verbatim snippet | Finding |
|---|---|---|---|
| Convention: length | — | 884 words | Target 1,500-2,200 (WRITING_CONVENTIONS L152). Significantly short. |
| Convention: interpret, don't restate | L241, L243, L245 | "First,... Second,... Third,..." | The Discussion restates the same three findings from Results using nearly identical numbers (192/287, 99/287, 5/287) and the same First/Second/Third scaffold. This is restatement, not interpretation. |
| Convention: compare against Related Work | L233-249 | Entire section | No comparison to any prior survey or review. WRITING_CONVENTIONS L154 says "Compare against Related Work." The Discussion never references Related Work at all. |
| Convention: name disagreements | L233-249 | Entire section | No disagreements in the literature are named. WRITING_CONVENTIONS L155 says "Name disagreements in the literature; do not paper over them." |
| AI-tell: ordinal scaffold (again) | L241-247 | "First,... Second,... Third,..." | Same First/Second/Third/Finally pattern as Introduction L30. The manuscript uses this scaffold twice — once for contributions, once for discussion. |
| AI-tell: hyperbolic language | L245 | "This finding exposes a glaring vulnerability" | "glaring" is editorializing. Academic register avoids such loaded adjectives. |
| AI-tell: grandiose phrasing | L245 | "Bridging this gap requires a paradigm shift in how robustness is defined" | "paradigm shift" is a cliche. The manuscript uses it to advocate for adversarial testing, which is a reasonable recommendation but not a paradigm shift. |
| AI-tell: long identical paragraphs | L241, L243, L245, L247 | Four Discussion paragraphs | All four body paragraphs are of similar length (150-200 words each) and follow the same structure: claim, elaboration, implication. Human writing varies paragraph length more. |
| Repetition of sensor-non-normalization caveat | L247 | "The extraction record relies on non-normalized quoted descriptions..." | This caveat has now appeared 5 times in the manuscript (Abstract L10, Results 4.1 L111, Discussion L247, Limitations L257, Conclusion L276). Five times is excessive. |
| Missing: no corpus-paper references | L233-249 | Entire section | Zero references to individual studies. The Discussion interprets findings without citing the evidence that supports them. |

---

## 7. Section 6: Limitations (Lines 251-270)

| Issue type | Line | Verbatim snippet | Finding |
|---|---|---|---|
| Convention: length | — | 519 words | Target 500-800 (WRITING_CONVENTIONS L162). Compliant. |
| Convention: corpus scope stated | L253 | "287 studies published between 2010 and 2026, appraised as Q-High (145), Q-Medium (118), and Q-Low (24)" | Compliant. |
| Convention: waived cells stated | L253 | "REC_1432 and REC_1435" | Compliant. |
| Convention: inter-rater stated | L260 | "Inter-rater reliability is not claimed" | Compliant and honest. |
| Structural strength | — | Two-group organization (corpus vs. method) | Well-organized, specific, and not defensive. This is one of the strongest sections. |
| Overlap with Methods 3.7 | L264-268 | Database cap, language bias, I6 exclusion | Same points appear in Section 3.7 (L87). Some redundancy. |

---

## 8. Section 7: Conclusion (Lines 272-282)

| Issue type | Line | Verbatim snippet | Finding |
|---|---|---|---|
| Convention: length | — | 422 words | Target 400-600 (WRITING_CONVENTIONS L171). Compliant. |
| Convention: no new citations/figures | — | — | Compliant. |
| Convention: no banned opener | — | Does not open with "In conclusion" | Compliant. |
| Convention: restate problem, method, findings | L274-276 | Problem, method, and three findings restated | Compliant. |
| AI-tell: near-verbatim repetition | L276 | "MIXED environments account for 192 of 287 studies (67%)" | This exact statistic (192/287, 67%) has now appeared in: Abstract (L10), Introduction (L30), Results 4.2 (L134), Results 4.5 (L229), Discussion (L241), and Conclusion (L276). That is 6 occurrences of the same number. |
| Strength: authentic closing | L282 | "The corpus already contains the evidence needed to act; what remains is the discipline to act on it." | This is a strong, human-sounding closing sentence. It has voice. |
| Convention: Future Work absent | — | — | Convention specifies a separate Future Work section (WRITING_CONVENTIONS L177-183, ~300-500 words). Future directions are embedded in the Conclusion (L280) but not separated out. |

---

## 9. End Sections (Lines 284-299)

| Issue type | Line | Verbatim snippet | Finding |
|---|---|---|---|
| Funding | L286 | "This research received no external funding." | Compliant. |
| COI | L290 | "The authors declare no competing interests." | Uses "the authors" — convention says avoid this phrasing (WRITING_CONVENTIONS L193). |
| Data Availability | L294 | GitHub link | Present. Compliant. |
| References | L298 | "[references will be inserted by the LaTeX build from references.bib]" | Placeholder — no references yet in the markdown source. This means the manuscript currently has 0 bibliography entries. The 5 REC citations ([REC_0010] etc.) at L45 and L218 are the only citations in the entire manuscript. |
| Appendix A | — | 287 rows verified | Present and complete. |

---

## 10. Summary of Phase 1 Findings

### Convention Violations (ranked by severity)

| # | Finding | Severity | Section |
|---|---|---|---|
| 1 | Zero prior-survey citations in Related Work; convention says "prior reviews and surveys only" | HIGH | Section 2 |
| 2 | Zero literature citations in Introduction; convention says "Cite the problem-statement literature" | HIGH | Section 1 |
| 3 | Only 5 in-text corpus citations in entire manuscript (all in Related Work and RQ4) | HIGH | Global |
| 4 | Discussion restates Results instead of interpreting them; no comparison to prior work | HIGH | Section 5 |
| 5 | Section 4.5 (Cross-cutting synthesis) is Discussion material placed inside Results | MEDIUM | Section 4 |
| 6 | Introduction (691 words) and Discussion (884 words) significantly below convention targets | MEDIUM | Sections 1, 5 |
| 7 | Voice uses "this review" (17x) instead of convention-mandated "we" | MEDIUM | Global |
| 8 | Missing Future Work section | MEDIUM | Structure |
| 9 | Table IV: text says OTHER=17, table says OTHER=18 | MEDIUM | Section 4.2 |
| 10 | Table III: text says 67.0%, table says 66.9% | LOW | Section 4.2 |

### AI-Tell Patterns (ranked by severity)

| # | Pattern | Severity | Where |
|---|---|---|---|
| 1 | Ordinal enumeration (First/Second/Third/Finally) used identically in both Introduction and Discussion | HIGH | L30, L241-247 |
| 2 | "not supportable" caveat repeated 5 times verbatim across 5 sections | HIGH | Abstract, 4.1, 5, 6, 7 |
| 3 | Key statistic 192/287 (67%) repeated 6 times | MEDIUM | Abstract, Intro, 4.2, 4.5, 5, 7 |
| 4 | "this review" used 17 times; "the corpus" 29 times; "the field" 12 times | MEDIUM | Global |
| 5 | Discussion paragraphs are uniform length with identical internal structure | MEDIUM | Section 5 |
| 6 | GPS defined twice in same paragraph | LOW | L18 |
| 7 | Kappa disclaimer phrased as if author does not know what happened in own project | MEDIUM | L83 |
| 8 | "glaring vulnerability," "paradigm shift" — editorializing and cliche | LOW | L245 |

### What Works Well

| # | Strength | Section |
|---|---|---|
| 1 | Zero banned words found | Global |
| 2 | Limitations section (Section 6) is specific, honest, and well-structured | Section 6 |
| 3 | PRISMA chain numbers are consistent throughout | Section 3 |
| 4 | QA rubric is clearly described and replicable | Section 3.6 |
| 5 | Closing sentence of Conclusion has genuine voice | Section 7, L282 |
| 6 | All 9 figures and 5 tables cited in text | Global |
| 7 | Appendix A has exactly 287 rows | Appendix A |

---

**PHASE 1 COMPLETE. STOP. Awaiting human instruction before proceeding to Phase 2.**
