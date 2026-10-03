# MASTER PROJECT BIBLE

**Project:** GPS-Denied Navigation for Unmanned Aerial Vehicles: A
Systematic Literature Review of Multi-Sensor Fusion Approaches
(2010–2026)

**Protocol:** PRISMA 2020
**Corpus:** 287 included studies
**Freeze date:** 2026-10-02
**Repository:** https://github.com/TheAbhishekraj/slr_project
**Original tag:** v287-certified
**Current tag:** pre-latex-cleanup-complete
**Author:** Abhishek Raj
**Affiliation:** [blank]
**ORCID:** [blank]
**Corresponding email:** [blank]
**Funding:** No external funding received.

---

## Part 1 — The Journey

### Stage 0 — The Idea
UAVs rely on GPS/GNSS for navigation. In contested, indoor,
subterranean, urban-canyon, and forest environments, GNSS is
denied, degraded, or spoofed. The field has produced a large but
fragmented body of multi-sensor fusion approaches. No prior review
unified them.

Four research questions:
1. Which sensor modalities dominate GPS-denied UAV navigation?
2. Which algorithmic architectures are used for fusion?
3. Which operational environments are tested?
4. How resilient are the systems under adversarial conditions?

Scope: 2010-01-01 to 2026-06-15. English only. Peer-reviewed
journals and full conference proceedings.

### Stage 1 — Search Strategy
Databases: IEEE Xplore, Scopus.
Execution date: 2026-06-15.
Two database-specific queries, three concept groups joined by AND:
  1. GPS/GNSS denial terminology
  2. UAV platform descriptors
  3. Navigation task descriptors
Filters: English, 2010–2026, journal + conference.
Harvest cap: 1,000 per database.
Raw corpus: 2,000 records.

### Stage 2 — Deduplication
Method: Exact matching on normalized DOI, normalized title+year,
and MD5 row-hash.
Result: 284 duplicates removed. 1,716 unique records.

### Stage 3 — Title/Abstract Screening
Result: 1,215 rejected. 501 advanced.
Single-pass, not dual-reviewer.

### Stage 4 — Full-Text Retrieval
Result: 291 PDFs retrieved. 210 not retrieved.
Retrieval rate: 291/501 = 58.1%. "100%" refers to assessed
studies only (291 of 291).

### Stage 5 — Full-Text Eligibility
4 exclusions:
  REC_0053 — X1 — Out of scope
  REC_0693 — X1 — Out of scope
  REC_0866 — X1 — Out of scope
  REC_1688 — X3 — Non-English (Chinese)
Final corpus: 287 included studies.

### Stage 6 — Data Extraction
Schema: 28 columns.
Method: Structured extraction into REC_XXXX.md cards.
Single-pass. Documented as a limitation.

### Stage 7 — Quality Appraisal
Rubric: 10-point, four dimensions.
  Q-High:   145 (8–10)
  Q-Medium: 118 (5–7)
  Q-Low:     24 (0–4)
  Total:    287

### Stage 8 — Synthesis
Narrative synthesis. No meta-analysis.
No formal publication-bias assessment (justified for narrative).

### Stage 9 — Manuscript Writing
Sections: Abstract, Introduction, Related Work, Methods, Results,
Discussion, Limitations, Conclusion.
IEEE style. Banned words enforced. American spelling.

### Stage 10 — Audit
Read-only 14-phase audit. Phases 0–6 completed. Phases 7–14
planned but not run. 66 issues logged. All CRITICAL and HIGH
issues resolved.

### Stage 11 — LaTeX + PDF
Tool: tools/venue_format.py
Output: 06_manuscript/ieee/manuscript_ieee.tex and .pdf

---

## Part 2 — Constraints and Challenges

### Constraints
1. Single-reviewer screening. No kappa.
2. Single-pass extraction.
3. No PROSPERO registration.
4. Two databases only.
5. English only.
6. Journal articles and conference papers only.
7. No meta-analysis.
8. No publication-bias assessment.
9. Single-pass quality appraisal.
10. One off-pipeline PDF (REC_0053, excluded, does not affect 287).

### Challenges resolved
1. Dedup method mismatch (Levenshtein vs exact). Corrected.
2. Query description mismatch (one vs two). Corrected.
3. Card title errors (39 found, 13 substantive). Investigated.
4. Stale file references (18 files). Cleaned.
5. Manifest verified column. Set to PASS.
6. Mojibake encoding. Fixed.
7. Word count discrepancy. Now 6,052.
8. Missing end sections. Added.
9. Triple-title case REC_1208. PDF title used.

### What remains
1. REC_0053 PDF still wrong on disk. Archival only.
2. Some cards with alternate titles. Cosmetic.
3. No PROSPERO registration. Documented limitation.

---

## Part 3 — Key Numbers

| Stage | Count |
|---|---|
| Raw harvested | 2,000 |
| Duplicates removed | 284 |
| Unique records | 1,716 |
| Title/abstract excluded | 1,215 |
| Screened in | 501 |
| Full-text retrieved | 291 |
| Full-text excluded | 4 |
| Included | 287 |

---

## Part 4 — Files and Purpose

| File | Purpose |
|---|---|
| 06_manuscript/MANUSCRIPT.md | Main text |
| 06_manuscript/references.bib | Bibliography |
| 05_analysis/figures/F1..F9.png | Figures |
| 02_cards/REC_*.md | Evidence cards |
| 04_master/MASTER_EVIDENCE.csv | Extracted data |
| 00_scope/LOCKED_NUMBERS.md | Locked numerics |
| 00_scope/SCOPE.md | Protocol |
| 00_scope/PRISMA_FLOWCHART.md | PRISMA flow |
| 07_certificates/CERTIFICATE_*.md | Certificates |
| 07_certificates/CENSUS_AUDIT_REPORT_*.md | Corpus audit |

---

## Part 5 — Verification Recipe

1. Clone the repo.
2. Checkout tag v287-certified.
3. Verify SHA256 of MASTER_EVIDENCE.csv
   = 88F94A9EB023E12502D2F12342FD658D0878C6DAA66A99986CC8F151D0D888BA
4. Verify SHA256 of LOCKED_NUMBERS.md
   = 9FB314272426C5C40F3F682A5830C270F183680D87BB9F7A3506CDC292691B32
5. Read the certificates in 07_certificates/.

---

## Part 6 — Contributions

1. First unified review of GPS-denied UAV navigation across
   sensor modalities, algorithms, environments, and resilience.
2. Corpus-level empirical baseline with quality stratification.
3. Identification of the adversarial-resilience gap:
   only 5 of 287 studies address contested conditions.
4. Reproducible pipeline with locked numbers and certificates.

---

## Part 7 — Limitations (for transparency)

1. Single-reviewer screening and extraction.
2. No formal protocol registration.
3. Narrative synthesis only.
4. No publication-bias assessment.
5. English-only corpus.
6. Two databases only.
7. Some evidence cards have extraction artifacts.

---

*End of MASTER_PROJECT_BIBLE.md*
