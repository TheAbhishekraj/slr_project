# 02_data_processed — PRISMA 2020 Data Processing & Evidence Repository (folder on disk keeps the legacy `proceesed` spelling; do not rename)

This directory contains the core processed datasets, screening registers, and batch extraction manifests for the systematic literature review:  
**"GPS-Denied Navigation for UAVs: A Systematic Literature Review of Multi-Sensor Fusion Approaches (2010–2026)"**.

---

## 1. Directory Structure

```text
02_data_proceesed/                     # legacy folder spelling on disk; do not rename
├── README.md                      # Directory guide, schema catalog, and cryptographic manifest (this file)
├── MASTER_EVIDENCE.csv            # REMOVED: legacy 279-row pre-Decision-B master; successor 04_master/MASTER_EVIDENCE.csv (287 rows, built in T3)
├── 01_deduplicated_master.csv       # FROZEN: 1,716 unique records after cross-database deduplication
├── dedup_log.csv                  # FROZEN: 284 dropped duplicate records log
├── DEDUP_REPORT.md                # Deduplication audit report and metric breakdown
├── DEDUP_VERIFY.md                # Verification checklist and SHA256 audit for deduplication
├── 02_screened_included.csv       # FROZEN: 501 candidate records passing preliminary screening
├── 03_screening_results.csv       # FROZEN: 291 records evaluated against full-text eligibility (287 INCLUDE, 4 EXCLUDE)
├── 04_retrieved_pdfs_291.csv      # FROZEN: 291 records successfully retrieved as PDFs
├── PRISMA_MASTER_WORKBOOK.xlsx    # MASTER REVIEW: Excel workbook containing sheets 01 to 04 for easy manual review
└── evidence_batches/              # REMOVED: legacy 279-era batch directory (superseded by Decision B, 287 corpus)
```

---

## 2. File Catalog & Cryptographic Manifest

All active core files have been audited and cryptographically verified:

| File | Type | Data Rows | Size | SHA256 Hash | Status |
| :--- | :--- | :---: | :---: | :--- | :--- |
| ~~`MASTER_EVIDENCE.csv`~~ | CSV | ~~279~~ | — | — | REMOVED (pre-Decision-B legacy); successor `04_master/MASTER_EVIDENCE.csv` (287 rows, built in T3) |
| **`01_deduplicated_master.csv`**| CSV | **1,716** | 2,485,100 B | `B6C8359D2355AF6E7CB057E035C9B84309C476D9CD06FD6777FCA1B26FE06810` | **FROZEN ANCHOR** |
| **`dedup_log.csv`** | CSV | **284** | 34,801 B | `F725F1A367FB47DE5969FFAF3EB4615B600F4937DC16F3DBD5A7129097C24F04` | **FROZEN AUDIT** |
| **`DEDUP_REPORT.md`** | Markdown | — | 2,309 B | `093992EB3364DAB9C14080524ECAA57D1B2640134D3330D72D1BF7A27AB74798` | Audit Log |
| **`DEDUP_VERIFY.md`** | Markdown | — | 975 B | `CD9AAA38722E6A5BE2BD9244807C814908FDF287D5D4A65E21E64D7A73A8598E` | Audit Log |
| **`02_screened_included.csv`** | CSV | **501** | 787,785 B | `DDCD89EDCA1546BCA72E77877F1F9C18FEA1C1CD8F365F34439F5CDAA45A4979` | **FROZEN ANCHOR** |
| **`03_screening_results.csv`** | CSV | **291** | 497,663 B | `9015BB35C68F0BAE470CA63661D3434CB43DCF6DB97BE088AD6568DFA5B805C1` | **FROZEN ANCHOR** |
| **`04_retrieved_pdfs_291.csv`** | CSV | **291** | 497,663 B | `9015BB35C68F0BAE470CA63661D3434CB43DCF6DB97BE088AD6568DFA5B805C1` | **FROZEN ANCHOR** |
| **`PRISMA_MASTER_WORKBOOK.xlsx`** | XLSX | — | 1,544,098 B | `02FD07156340BFEC1974507889584CBAF17B1E10250CDEB3F46D3830DDCC49D7` | Review Data |
NOTE: `pdf_removal_log.csv` and `screening_spreadsheet.xlsx` were referenced by
older versions of this README but are not present on disk (see §5 Archive
History for the 2026-09-27 relocation of pre-reset files). Do not recreate
them.

---

## 3. PRISMA 2020 Data Flow in this Directory

The files in this directory represent the quantitative stages of the PRISMA 2020 flow:

```
┌────────────────────────────────────────────────────────┐
│ Raw Harvest (01_data_raw/): 2,000 Records              │
│ (1,000 IEEE Xplore + 1,000 Scopus)                     │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼ [Automated Deduplication]
┌────────────────────────────────────────────────────────┐
│ 01_deduplicated_master.csv: 1,716 Unique Records       │
│ (284 Duplicate records documented in dedup_log.csv)    │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼ [Title & Abstract Screening]
┌────────────────────────────────────────────────────────┐
│ 02_screened_included.csv: 501 Candidate Records          │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼ [Full-Text Eligibility Screening]
┌────────────────────────────────────────────────────────┐
│ 03_screening_results.csv: 291 Assessed Records         │
│ ├── 287 INCLUDED                                       │
│ └── 4 EXCLUDED (3 Scope X1, 1 Language X3: REC_1688)   │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼ [Corpus Refinement & Deduplication]
┌────────────────────────────────────────────────────────┐
│ Corpus Denominator: 287 Included Studies               │
│ (291 Assessed - 4 Excluded = 287 Final Included Corpus)│
│ Verified in 03_screening_results.csv & 04_retrieved_   │
│ pdfs_291.csv (Sl. No 1 to 291 1-to-1 with PDFs)        │
└────────────────────────────────────────────────────────┘
```

---

## 4. `evidence_batches/` Details (REMOVED — legacy)

The legacy `evidence_batches/` directory has been removed. It was built
on the old 279-paper corpus (27 batches x 10 papers + 1 batch x 9) which
Decision B (2026-10-02) superseded. The frozen corpus is now **287
studies**; any future batch artefacts must be regenerated against the
287-corpus master (`04_master/MASTER_EVIDENCE.csv`, built in T3).

---

## 5. Archive History (Moved Legacy Files)

On 2026-09-27, the following 8 obsolete or conflicting Generation-1 (pre-reset) files were safely relocated (the `_ARCHIVE/` staging folder named by the pre-reset session is not present on disk; confirm the relocation target before treating it as archival):

1. `summary.txt` (Contained obsolete 2026-09-06 test numbers contradicting frozen deduplication).
2. `MASTER_EVIDENCE_V1.xlsx` (Pre-reset Generation-1 spreadsheet).
3. `EXTRACTION_NOTES.md` (Legacy notes citing deprecated 1,700-row extraction model).
4. `EXTRACTION_NOTES_v2.md` (Legacy notes citing 171-paper extraction subset).
5. `V1_SCOPE_IDS.txt` (Obsolete Generation-1 scope ID list).
6. `PENDING_MASTER_EXTENSION_IDS.txt` (Obsolete 121-paper extension tracking list).
7. `retrieval_log.csv` (Empty 0-row header template).
8. `pending_list.csv` (Empty 0-row header template).
