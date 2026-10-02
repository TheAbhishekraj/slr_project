# END_GOAL_287 — slr_project

Frozen: 2026-10-02 (Decision B)
Corpus: LOCKED at 287
Target venue: IEEE T-RO or IEEE Access

================================================================
PURPOSE
================================================================
Complete a PRISMA 2020 systematic literature review:
"GPS-Denied Navigation for UAVs: Multi-Sensor Fusion Approaches
(2010-2026)".
Every number traceable to a paper and page. Zero invented data.

================================================================
THE FROZEN ANCHOR
================================================================
2,000 raw (IEEE 1,000 + Scopus 1,000)
-> 1,716 unique (284 duplicates removed)
-> 501 screened-in  (verified by file count 2026-10-02)
-> 291 full-text assessed (291 PDFs on disk)
-> 4 EXCLUDED (REC_0053 X1, REC_0693 X1, REC_0866 X1, REC_1688 X3)
-> 287 FINAL CORPUS — LOCKED

No additions, no removals, ever, without a new signed FROZEN_SCOPE.

================================================================
DELIVERABLES (all five required for "done")
================================================================
D1  MANUSCRIPT
    06_manuscript/MANUSCRIPT_V2.md (+ venue-formatted PDF)
    Sections: Abstract, Intro, Related Work, Methods (PRISMA 2020),
    Results, Discussion, Threats, Conclusion.
    Every number traced in 06_manuscript/NUMBER_TRACE.md.
    Zero [UNTRACEABLE]. Zero banned words (R7).

D2  SUPPLEMENTARY TABLES
    06_manuscript/SUPPLEMENTARY/
      S1  Evidence matrix — 287 rows x 28 cols
      S2  PRISMA flow diagram (2,000/1,716/501/291/4/287)
      S3  Exclusion log — the 4 excluded records
      S4  Inclusion/exclusion criteria (X1, X3)

D3  CERTIFIED MASTER
    04_master/MASTER_EVIDENCE_v2.csv
      287 rows, 28 cols, every quote carries [p.N]
    Certificate: 07_certificates/CERTIFICATE_MASTER_287.md

D4  AUDIT TRAIL
    07_certificates/
      MERGE_DECISIONS.md        (one line per diff vs old 279)
      CERTIFICATE_MASTER_287.md
      CERTIFICATE_MANUSCRIPT.md
      CENSUS_AUDIT_REPORT_20261002.md
    03_ai_checks/                (one P1 report per card — 287)

D5  SUBMISSION PACKAGE
    06_manuscript/SUBMISSION_CHECKLIST.md
    06_manuscript/references.bib
    git tag "v287-certified"

================================================================
DEFINITION OF DONE
================================================================
1. All five deliverables exist.
2. All counts reconcile to the frozen anchor.
3. All figures regenerate from a script.
4. Zero [UNTRACEABLE] markers.
5. Zero excluded IDs (0053/0693/0866/1688) in any count, table,
   figure, or manuscript sentence.
6. Zero old 279-corpus numbers in any live file.
7. Manuscript submitted to IEEE T-RO or IEEE Access.

================================================================
END OF END_GOAL_287
================================================================
