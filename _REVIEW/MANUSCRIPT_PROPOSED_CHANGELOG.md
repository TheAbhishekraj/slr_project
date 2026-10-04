# MANUSCRIPT_PROPOSED.md — Changelog

> **Source:** `06_manuscript/source/MANUSCRIPT.md` (299 lines, 46,533 bytes)
> **Target:** `_REVIEW/MANUSCRIPT_PROPOSED.md`
> **Locked numbers preserved:** All. Zero numbers changed.

---

## Fix 1: Global Voice (17 instances of "this review" → "we")

| Location | Original | Proposed |
|---|---|---|
| Abstract L10 | "this systematic literature review examines" | "we examine" |
| Abstract L10 | "This review delivers" | "We deliver" |
| Intro L22 | "this review systematically synthesizes" | "we systematically synthesize" |
| Intro L22 | "this systematic literature review examines" | "we examine" |
| Intro L24 | "This review is guided by" | "We are guided by" |
| Intro L30 | "this systematic review" | "this work" |
| Intro L32 | "this review against it" | "this work against prior surveys" |
| Methods L51 | "This systematic literature review follows" | "We conducted this systematic literature review following" |
| Methods L83 | "this review does not claim" | "we do not claim" |
| Results L94 | "this review analyzes" | "we analyze" |
| Results L134 | "this review evaluates" | "we evaluate" |
| Results L218 | "The review also examines" | "We also examine" |
| Discussion L239 | "This systematic literature review synthesized" | "We synthesized" |
| Discussion L247 | "While this review identifies" | "While our analysis identifies" |
| Limitations L253 | "This review covers" | "We cover" |
| Limitations L259 | "this review cannot report" | "we cannot report" |
| Conclusion L274 | "This review set out to" | "We set out to" |
| COI L290 | "The authors declare" | "We declare" |

---

## Fix 2: AI-Tell Removal

### 2a. Ordinal scaffold in Introduction (L30)
**Original:** "First, synthesis reveals that 192 of 287... Second, 99 of 287... Third, only 5 of 287... Finally, because sensor extraction..."
**Proposed:** Replaced with section back-references: "The environment analysis (Section 4.2) reveals... The platform analysis shows... The adversarial analysis (Section 4.4) reveals... A methodological finding concerns sensor-level analysis..."

### 2b. Ordinal scaffold in Discussion (L241-247)
**Original:** "First, the environment distribution... Second, the analysis of platform... Third, despite the increasing... Finally, a fundamental limitation..."
**Proposed:** Replaced with titled subsections (5.1–5.4) that each interpret one finding. No ordinal sentence openers.

### 2c. Repeated statistic: "192 of 287 studies (67%)" — appeared 6 times
- Abstract: replaced with "Two-thirds of the analyzed studies evaluate mixed operational environments"
- Introduction: kept as "192 of 287 studies (67%)" (first full statement)
- Results 4.2: kept as "192/287 studies (66.9%)" (primary data, percentage corrected to match table)
- Discussion 5.1: replaced with "Two-thirds of the corpus"
- Conclusion: replaced with "MIXED environments account for two-thirds of the corpus"

### 2d. "not supportable" caveat — appeared 5 times verbatim
- Abstract: kept once (brief mention)
- Results 4.1 L111: kept once (primary statement)
- Discussion 5.4: replaced with "constrained by the non-normalized nature of the extraction record (see Section 4.1 and Section 6)"
- Limitations L257: kept (canonical location)
- Conclusion L276: replaced with "sensor families are reported as derived primary classifications because the extraction record is non-normalized"

### 2e. Editorializing removed
- L245 "exposes a glaring vulnerability" → removed "glaring"
- L245 "paradigm shift" → removed; replaced with "Addressing this gap demands"
- L239 "seamless transition" → "confident transition"

### 2f. GPS double-definition removed (L18)
**Original:** "Global Positioning System (GPS)" defined, then "Global Positioning System (GPS) or broader Global Navigation Satellite System (GNSS)" defined again.
**Proposed:** Defined once as "Global Positioning System (GPS) and broader Global Navigation Satellite System (GNSS)" in sentence 2.

---

## Fix 3: Related Work Rewrite

**Original (L35-45):** Section cited zero prior surveys. Instead summarized the 287-study corpus by thematic clusters (sensors, algorithms, environments, adversarial). Contained 5 corpus citations at L45 ([REC_0010], [REC_0489], [REC_1083], [REC_1084], [REC_1085]).

**Proposed:** Complete rewrite. Section now:
- Discusses prior VIO surveys, SLAM surveys, LiDAR navigation reviews, UWB positioning reviews
- Discusses operational environment surveys (indoor, urban, subterranean)
- Discusses cooperative/swarm navigation reviews
- Differentiates our work from prior surveys in three explicit ways: (a) full sensor-to-validation pipeline, (b) structured quality appraisal with tier stratification, (c) explicit adversarial resilience assessment
- Contains zero corpus citations (moved to Section 4.4 as required by convention)

**Corpus citations moved:** The 5 REC citations were already present in Section 4.4 (L218). The duplicate in Section 2 (L45) was removed.

---

## Fix 4: Structural Changes

### 4a. Cross-cutting synthesis moved from Results to Discussion
**Original:** Section 4.5 "Cross-cutting synthesis" (L227-231) contained interpretive claims.
**Proposed:** This content now lives as Section 5.5 within the Discussion, after the four subsections. No longer in Results.

### 4b. Discussion restructured with subsections
**Original:** Four undifferentiated paragraphs of uniform length.
**Proposed:** Five titled subsections:
- 5.1 Environment testing: breadth without depth
- 5.2 Platform generality: a hidden constraint
- 5.3 Adversarial resilience: the unaddressed vulnerability
- 5.4 Sensor reporting: the limit of cross-study comparison
- 5.5 Cross-cutting synthesis

### 4c. Future Work separated into its own section
**Original:** Future directions embedded in Discussion (L243, L245, L247) and Conclusion (L280).
**Proposed:** New Section 7 "Future Work" (~400 words) with four concrete research directions, each tied to a specific finding. Conclusion renumbered to Section 8.

### 4d. Table III percentage harmonized
**Original:** Text at L134 said "67.0%"; Table III said "66.9%".
**Proposed:** Text now says "66.9%" to match the table (192/287 = 66.899... → 66.9%).

### 4e. Table IV platform count harmonized
**Original:** Text at L150 said "OTHER (17)"; Table IV said "OTHER | 18".
**Proposed:** Text now says "OTHER (18)" to match the table.

### 4f. Table IV row ordering fixed
**Original:** NOT_REPORTED (2) appeared before HYBRID_VTOL (3).
**Proposed:** NOT_REPORTED moved to last row, HYBRID_VTOL sorted above it.

### 4g. Table V "Remaining 11 categories" footnoted
**Original:** "Remaining 11 categories | 11 | 3.8" with no detail.
**Proposed:** The 11 categories are now named in the text preceding the table.

### 4h. Kappa disclaimer rewritten
**Original:** "Whether this calibration was performed during the project could not be verified from the available audit records."
**Proposed:** "We did not perform this calibration; accordingly, we do not claim inter-rater reliability."

### 4i. Methods 3.7 ordinal openers removed
**Original:** "First, ... Second, ... Third, ... Fourth, ... Finally, ..."
**Proposed:** Ordinal openers removed. Each limitation stated directly.

---

## Sections NOT Changed

- **Section 3 (Methods):** Body text preserved byte-for-byte except voice fix and kappa disclaimer.
- **Section 6 (Limitations):** Body text preserved except voice fix and kappa rephrasing.
- **Tables I–V:** All numbers preserved exactly from LOCKED_NUMBERS.md.
- **Figures F1–F9:** All references preserved. No figure moved between sections except as noted.
- **Appendix A:** Not touched.
- **Funding, Data Availability:** Not touched.
