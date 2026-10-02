# 02_data_processed — PRISMA 2020 Data Processing & Evidence Repository

This directory contains the core processed datasets, screening registers, and batch extraction manifests for the systematic literature review:  
**"GPS-Denied Navigation for UAVs: A Systematic Literature Review of Multi-Sensor Fusion Approaches (2010–2026)"**.

---

## 1. Directory Structure

```text
02_data_processed/
├── README.md                      # Directory guide, schema catalog, and cryptographic manifest (this file)
├── MASTER_EVIDENCE.csv            # LIVE: Final 279-paper multi-sensor extraction master (28 columns)
├── 01_deduplicated_master.csv       # FROZEN: 1,716 unique records after cross-database deduplication
├── dedup_log.csv                  # FROZEN: 280 dropped duplicate records log
├── DEDUP_REPORT.md                # Deduplication audit report and metric breakdown
├── DEDUP_VERIFY.md                # Verification checklist and SHA256 audit for deduplication
├── 02_screened_included_v2.csv    # FROZEN: 501 candidate records passing preliminary screening
├── 03_screening_results.csv       # FROZEN: 291 records evaluated against full-text eligibility (287 INCLUDE, 4 EXCLUDE)
├── 04_retrieved_pdfs_291.csv      # FROZEN: 291 records successfully retrieved as PDFs
├── PRISMA_MASTER_WORKBOOK_v2.xlsx # MASTER REVIEW: Excel workbook containing sheets 01 to 04 for easy manual review
├── screening_spreadsheet.xlsx     # Working spreadsheet for screening evaluations
├── pdf_removal_log.csv            # Audit of 3 byte-identical duplicate PDFs excluded from corpus
└── evidence_batches/              # Batch extraction processing directory (28 batches)
    ├── BATCH_B01.csv ... BATCH_B28.csv       # 28 batch CSV tables (279 rows total)
    └── BATCH_B01_pages/ ... BATCH_B28_pages/ # Full-text page extraction snippets per batch
```

---

## 2. File Catalog & Cryptographic Manifest

All active core files have been audited and cryptographically verified:

| File | Type | Data Rows | Size | SHA256 Hash | Status |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **`MASTER_EVIDENCE.csv`** | CSV | **279** | 134,087 B | `15B26C59DFAAAD0A62A3D473AC7EB4DFC0491A89B7B6D4D5CF78BB8FB512B2C6` | **LIVE MASTER** |
| **`01_deduplicated_master.csv`**| CSV | **1,716** | 2,485,100 B | `B6C8359D2355AF6E7CB057E035C9B84309C476D9CD06FD6777FCA1B26FE06810` | **FROZEN ANCHOR** |
| **`dedup_log.csv`** | CSV | **280** | 34,801 B | `F725F1A367FB47DE5969FFAF3EB4615B600F4937DC16F3DBD5A7129097C24F04` | **FROZEN AUDIT** |
| **`DEDUP_REPORT.md`** | Markdown | — | 2,309 B | `093992EB3364DAB9C14080524ECAA57D1B2640134D3330D72D1BF7A27AB74798` | Audit Log |
| **`DEDUP_VERIFY.md`** | Markdown | — | 975 B | `CD9AAA38722E6A5BE2BD9244807C814908FDF287D5D4A65E21E64D7A73A8598E` | Audit Log |
| **`02_screened_included_v2.csv`** | CSV | **501** | 786,996 B | `7528BA3B929B8FE800D3457FEFFD59C39EACAAC6289A40AF58069DD5D78F2CEA` | **FROZEN ANCHOR** |
| **`03_screening_results.csv`** | CSV | **291** | 497,663 B | `9015BB35C68F0BAE470CA63661D3434CB43DCF6DB97BE088AD6568DFA5B805C1` | **FROZEN ANCHOR** |
| **`04_retrieved_pdfs_291.csv`** | CSV | **291** | 497,663 B | `9015BB35C68F0BAE470CA63661D3434CB43DCF6DB97BE088AD6568DFA5B805C1` | **FROZEN ANCHOR** |
| **`PRISMA_MASTER_WORKBOOK_v2.xlsx`** | XLSX | — | 1,535,135 B | `CA5681CABBC18E75AA21AF47E022323442587BC0A5FD47E18038FDE105716372` | Review Data |
| **`pdf_removal_log.csv`** | CSV | **3** | 285 B | `A9CFF5BCAF9A69B510CE5189FFACD5440CEDA60793946E67A23DFD9A8E30972D` | Audit Log |
| **`screening_spreadsheet.xlsx`** | XLSX | — | 2,279,257 B | `9C7F2E281F472210EC2BE6571C3A37AA12338DB2C1A04B4072D67850C7935CB8` | Working Data |

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
│ (280 Duplicate records documented in dedup_log.csv)    │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼ [Title & Abstract Screening]
┌────────────────────────────────────────────────────────┐
│ 02_screened_included_v2.csv: 501 Candidate Records     │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼ [Full-Text Eligibility Screening]
┌────────────────────────────────────────────────────────┐
│ 03_screening_results.csv: 291 Assessed Records         │
│ ├── 287 INCLUDED                                       │
│ └── 4 EXCLUDED (3 Scope E1, 1 Language E3: REC_1688)   │
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

## 4. `evidence_batches/` Details

To ensure scalable, reproducible extraction without memory overruns, the 279 in-corpus papers are divided into **28 sequential batches**:
- **Batches B01 to B27:** Exactly 10 papers each (27 × 10 = 270 papers).
- **Batch B28:** Exactly 9 papers (270 + 9 = 279 papers).
- **Page Extraction Folders (`BATCH_BXX_pages/`):** Full-text page extractions corresponding to each paper in the batch, used by extraction scripts and human spot-check validators.

---

## 5. Archive History (Moved Legacy Files)

On 2026-09-27, the following 8 obsolete or conflicting Generation-1 (pre-reset) files were safely relocated using `git mv` to `_ARCHIVE/legacy_02_data_processed/` to preserve a clean PRISMA 2020 workspace:

1. `summary.txt` (Contained obsolete 2026-09-06 test numbers contradicting frozen deduplication).
2. `MASTER_EVIDENCE_V1.xlsx` (Pre-reset Generation-1 spreadsheet).
3. `EXTRACTION_NOTES.md` (Legacy notes citing deprecated 1,700-row extraction model).
4. `EXTRACTION_NOTES_v2.md` (Legacy notes citing 171-paper extraction subset).
5. `V1_SCOPE_IDS.txt` (Obsolete Generation-1 scope ID list).
6. `PENDING_MASTER_EXTENSION_IDS.txt` (Obsolete 121-paper extension tracking list).
7. `retrieval_log.csv` (Empty 0-row header template).
8. `pending_list.csv` (Empty 0-row header template).
