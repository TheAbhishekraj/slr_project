# Phase 0 — Project Comprehension Report

> **Status:** Understanding only. No judgment. No edits.
> **Files read:** 16 (all listed in the Phase 0 manifest) plus Appendix A row-count verification.

---

## 1. One-Paragraph Summary

This project is a completed systematic literature review (SLR) of GPS-denied navigation for unmanned aerial vehicles, covering multi-sensor fusion approaches published between 2010 and 2026. It follows the PRISMA 2020 framework. A single author (Abhishek Raj) searched IEEE Xplore and Scopus on 2026-06-15, harvested 2,000 records (1,000 per database), deduplicated to 1,716, screened to 501, retrieved 291 full-text PDFs, excluded 4 (3 out-of-scope, 1 non-English), and froze a corpus of 287 included studies on 2026-10-02. Each study was extracted into a 28-column schema anchored by verbatim quotes. A 10-point quality appraisal rubric was applied, yielding 145 Q-High, 118 Q-Medium, and 24 Q-Low studies. The manuscript synthesizes findings narratively (no meta-analysis) across four research questions addressing sensors, environments, algorithms, and adversarial resilience. The project includes extensive audit infrastructure: locked numbers, SHA256 hashes, action and rules logs, certificates, and frozen manifests.

---

## 2. Declared Scope, Corpus Size, and Freeze Date

| Item | Value | Source |
|---|---|---|
| Title | GPS-Denied Navigation for Unmanned Aerial Vehicles: A Systematic Literature Review of Multi-Sensor Fusion Approaches (2010-2026) | MASTER_PROJECT_BIBLE.md, lines 3-5 |
| Protocol | PRISMA 2020 | MASTER_PROJECT_BIBLE.md, line 7 |
| Corpus size | 287 included studies | MASTER_PROJECT_BIBLE.md, line 8 |
| Freeze date | 2026-10-02 | MASTER_PROJECT_BIBLE.md, line 9 |
| Search window | 2010-01-01 to 2026-06-15 | SCOPE.md, line 112 |
| Databases | IEEE Xplore (1,000) + Scopus (1,000) | SCOPE.md, lines 67-105 |
| Tags | v287-certified, pre-latex-cleanup-complete | MASTER_PROJECT_BIBLE.md, lines 11-12 |

---

## 3. PRISMA Chain (declared consistently across files)

| Stage | Count | Verified in |
|---|---|---|
| Raw harvested | 2,000 | BIBLE L140, LOCKED L12, SCOPE L229, FROZEN L4, PRISMA_FLOWCHART L35, CENSUS L17, MANUSCRIPT L57 |
| Duplicates removed | 284 | BIBLE L141, LOCKED L13, SCOPE L230, FROZEN L4, PRISMA_FLOWCHART L9, CENSUS L24, MANUSCRIPT L61 |
| Unique records | 1,716 | BIBLE L142, LOCKED L14, SCOPE L231, FROZEN L4, PRISMA_FLOWCHART L36, CENSUS L23, MANUSCRIPT L61 |
| Screened in | 501 | BIBLE L144, LOCKED L15, SCOPE L234, FROZEN L4, PRISMA_FLOWCHART L37, CENSUS L29, MANUSCRIPT L61 |
| Full-text assessed | 291 | BIBLE L145, LOCKED L16, SCOPE L235, FROZEN L5, PRISMA_FLOWCHART L41, CENSUS L35, MANUSCRIPT L61 |
| Excluded | 4 | BIBLE L146, LOCKED L17, SCOPE L237-L238, FROZEN L6, PRISMA_FLOWCHART L19, CENSUS L38, MANUSCRIPT L61 |
| Included | 287 | BIBLE L147, LOCKED L18, SCOPE L239, FROZEN L11, PRISMA_FLOWCHART L42, CENSUS L45, MANUSCRIPT L61 |

**Result:** All seven PRISMA chain numbers are stated identically across all checked files. No discrepancy found.

---

## 4. Methodology Claimed (PRISMA 2020 Items)

The manuscript and scope documents claim compliance with PRISMA 2020. From SUBMISSION_CHECKLIST.md, lines 91-123, a mapping of all 27 PRISMA items is provided:

- **Addressed:** Items 1-11, 13-14, 16a, 17, 18, 20, 21, 23a-c, 24-27
- **NOT_ADDRESSED (explicitly):**
  - Item 12 (Effect measures) - narrative synthesis, no effect-size pooling
  - Item 15 (Certainty assessment) - no GRADE or equivalent applied
  - Item 19 (Results of individual studies) - aggregate synthesis only
  - Item 22 (Certainty of evidence) - no GRADE

---

## 5. Stated Limitations

From MASTER_PROJECT_BIBLE.md Part 7 (lines 191-199) and MANUSCRIPT.md Section 6 (lines 251-270):

1. Single-reviewer screening and extraction (no dual-reviewer process).
2. No formal protocol registration (no PROSPERO).
3. Narrative synthesis only (no meta-analysis, no effect-size pooling).
4. No publication-bias assessment.
5. English-only corpus (language bias).
6. Two databases only (IEEE Xplore and Scopus); 1,000-record cap per database.
7. Some evidence cards have extraction artifacts.
8. Sensor extraction is non-normalized (quoted descriptions, not standardized inventory).
9. Platform classification is coarse (regex-derived from free-text).
10. Environment labels are aggregated (GNSS_DENIED_OTHER pools several threat types).
11. Inter-rater reliability is not claimed (Kappa calibration could not be verified from audit records).
12. Quality appraisal assesses rigor, not novelty.
13. Two ablation fields waived (REC_1432, REC_1435).

---

## 6. Declared Standards

| Standard | Claimed | Where |
|---|---|---|
| PRISMA 2020 | Yes - full protocol adherence claimed | SCOPE.md line 4; MANUSCRIPT.md line 51 |
| AMSTAR-2 | Not explicitly claimed in manuscript | NOT_REPORTED in manuscript; mentioned only in the review prompt |
| IEEE formatting | Yes - IEEEtran style, IEEE Access target venue | FORMATTING_STANDARDS.md line 1; SUBMISSION_CHECKLIST.md line 5 |

---

## 7. Conflicting Claims Between Documents

### 7.1 Inter-rater reliability: aspiration vs. reality

- SCOPE.md lines 175-178 **specifies** a 20% dual-appraiser calibration sample with a target kappa >= 0.75.
- SCOPE.md line 270 immediately **flags** this as a known discrepancy: "Verify whether this was performed. If not performed, soften Q7."
- MANUSCRIPT.md line 83 **disclaims** it: "Whether this calibration was performed during the project could not be verified from the available audit records."
- MASTER_PROJECT_BIBLE.md line 107 states flatly: "No kappa."

**Assessment:** The manuscript's disclaimer is honest and consistent with the Bible's statement. The SCOPE.md Q7 text is aspirational protocol language that was never fulfilled. The conflict is between the protocol-as-planned (SCOPE.md Q7 body) and the project-as-executed (Bible + manuscript). The manuscript handles this correctly by disclaiming rather than claiming.

### 7.2 Deduplication method: Levenshtein vs. exact

- SCOPE.md line 220 says: "normalized title Levenshtein >= 0.95"
- MANUSCRIPT.md line 61 says: "exact cross-database matching on normalized DOI, a normalized title-year pair, and an MD5 content hash"
- MASTER_PROJECT_BIBLE.md lines 51-52 says: "Exact matching on normalized DOI, normalized title+year, and MD5 row-hash."

**Assessment:** SCOPE.md references Levenshtein; the Bible and manuscript describe exact matching + MD5. The Bible's "Challenges resolved" section (line 119) notes: "Dedup method mismatch (Levenshtein vs exact). Corrected." The manuscript and Bible are self-consistent. SCOPE.md carries legacy language that was corrected during the project but the SCOPE.md text was not updated to remove "Levenshtein." This is a minor inconsistency within SCOPE.md that does not propagate to the manuscript.

### 7.3 Related Work vs. corpus-based thematic review

- WRITING_CONVENTIONS.md lines 117-123 states Related Work should contain "Prior reviews and surveys only" and "Do not re-list the 287-corpus papers here."
- MANUSCRIPT.md line 37 opens Section 2 with: "Rather than summarizing prior surveys, this review groups the primary evidence base by sensor modality..." and proceeds to cite 5 REC IDs from the corpus ([REC_0010], [REC_0489], [REC_1083], [REC_1084], [REC_1085]) at line 45.

**Assessment:** The manuscript's Related Work section explicitly departs from the convention. It describes itself as a thematic grouping of the corpus rather than a survey of prior reviews. This is a deliberate design choice, but it contradicts the convention document. The 5 REC citations at line 45 are corpus papers appearing in what the convention says should be prior-surveys-only.

### 7.4 Evidence card count: 291 cards vs. 287 included

- REFERENCE_APPENDIX.md line 83 says "291 evidence cards."
- The project has 291 cards on disk (287 included + 4 excluded) - this is correct but could confuse a reader.
- FROZEN_SCOPE.md line 17 clarifies: "Exactly 291 extraction cards in 02_cards/."

**Assessment:** Not a true conflict. 291 cards exist (covering all assessed studies), of which 287 are included. The reference appendix could be clearer.

### 7.5 Voice convention: "we" vs. actual manuscript usage

- WRITING_CONVENTIONS.md lines 192-194 specifies first-person plural ("we screened," "this review finds") and says "Do not use 'the authors' or 'this paper' as a self-reference."
- The manuscript uses "this review" throughout but never uses "we" - it is written entirely in impersonal third person.

**Assessment:** The manuscript is internally consistent (impersonal throughout) but departs from the explicit "we" convention. This is a voice-level conflict between the convention document and the actual prose.

### 7.6 Manuscript structure: no Future Work section

- WRITING_CONVENTIONS.md lines 177-183 specifies a "Future Work" section of ~300-500 words.
- The manuscript has no standalone "Future Work" section. Future directions are embedded in the Conclusion (Section 7) and Discussion (Section 5).

**Assessment:** The convention calls for a separate section that does not exist. The content is present but not structured as specified.

### 7.7 Section lengths below convention targets

- SUBMISSION_CHECKLIST.md line 13 reports Introduction at 691 words; WRITING_CONVENTIONS.md line 110 targets ~1,000-1,500 words.
- Discussion at 884 words falls below the 1,500-2,200 target (WRITING_CONVENTIONS.md line 152).
- Results at 1,496 words is at the low end of the 2,000-3,000 range (WRITING_CONVENTIONS.md line 138).

**Assessment:** Multiple sections are significantly shorter than their convention-declared target ranges. The manuscript is within IEEE Access norms overall but does not meet its own internal targets.

---

## Summary of Conflicts Found

| # | Conflict | Severity | Status in Project |
|---|---|---|---|
| 1 | Kappa: protocol says calibrate, project did not | LOW | Correctly disclaimed in manuscript |
| 2 | Dedup: SCOPE.md says Levenshtein, Bible/manuscript say exact | LOW | Bible notes correction; SCOPE.md not updated |
| 3 | Related Work: convention says prior surveys only; manuscript uses corpus citations | MEDIUM | Deliberate design choice, undocumented |
| 4 | Voice: convention says "we"; manuscript uses impersonal | MEDIUM | Internally consistent but violates convention |
| 5 | Missing Future Work section | LOW | Content present in Conclusion, not separated |
| 6 | Section lengths below convention targets | LOW | Manuscript is within IEEE Access norms |
| 7 | 291 cards vs. 287 included (clarity, not error) | LOW | Explained in FROZEN_SCOPE.md |

---

**PHASE 0 COMPLETE. STOP. Awaiting human instruction before proceeding to Phase 1.**
