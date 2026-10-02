# GPS-Denied Navigation for UAVs: Systematic Literature Review (2010–2026)

**Protocol:** PRISMA 2020  
**Domain:** Multi-Sensor Fusion Approaches for UAV Navigation in GNSS-Denied Environments  
**Status:** Frozen Corpus & Extraction Base (2026-10-02)

---

## 1. Project Directory Structure

- [`00_scope/`](file:///e:/slr_project/00_scope/) — Scope governance, PRISMA census, extraction schemas, and versioned frozen scopes:
  - [`FROZEN_SCOPE.md`](file:///e:/slr_project/00_scope/FROZEN_SCOPE.md) & [`FROZEN_SCOPE_v6.md`](file:///e:/slr_project/00_scope/FROZEN_SCOPE_v6.md)
  - [`EXTRACTION_SCHEMA.md`](file:///e:/slr_project/00_scope/EXTRACTION_SCHEMA.md) (28 standardized columns)
  - [`PHASE_C_MANUAL_EXTRACTION.md`](file:///e:/slr_project/00_scope/PHASE_C_MANUAL_EXTRACTION.md) (7 Golden Rules & validation protocols)
- [`01_data/`](file:///e:/slr_project/01_data/) — All search, screening, and full-text data assets:
  - [`01_data_raw/`](file:///e:/slr_project/01_data/01_data_raw/) — 2,000 raw search records (IEEE Xplore & Scopus).
  - [`02_data_proceesed/`](file:///e:/slr_project/01_data/02_data_proceesed/) — Deduplication reports (`01_deduplicated_master.csv`), candidate screening (`02_screened_included_v2.csv`), PRISMA full-text screening (`03_screening_results.csv`), retrieved manifests (`04_retrieved_pdfs_291.csv`), and master Excel review workbook (`PRISMA_MASTER_WORKBOOK_v2.xlsx`).
  - [`03_pdfs/`](file:///e:/slr_project/01_data/03_pdfs/) — 291 full-text primary study PDF documents (`REC_0001.pdf` to `REC_1715.pdf`), text conversions (`.txt`), and English translations (canonical Bible Part 3 location).
- [`02_cards/`](file:///e:/slr_project/02_cards/) — 291 per-paper markdown extraction evidence cards (`REC_XXXX.md`), tracked by [`FROZEN.md`](file:///e:/slr_project/02_cards/FROZEN.md) and [`FROZEN_MANIFEST_20260927.csv`](file:///e:/slr_project/02_cards/FROZEN_MANIFEST_20260927.csv).
- [`03_ai_checks/`](file:///e:/slr_project/03_ai_checks/) — Cross-validation logs and automated extraction audit outputs.
- [`04_master/`](file:///e:/slr_project/04_master/) — Master synthesis tables and consolidated data matrices.
- [`05_analysis/`](file:///e:/slr_project/05_analysis/) — Meta-analysis scripts, bibliometric plots, and taxonomic statistics.
- [`06_manuscript/`](file:///e:/slr_project/06_manuscript/) — Draft chapters, PRISMA flow diagrams, and LaTeX sources.
- [`07_certificates/`](file:///e:/slr_project/07_certificates/) — Data freeze hashes, audit sign-offs, and compliance certificates.
- [`tools/`](file:///e:/slr_project/tools/) — Utilities for corpus validation, schema auditing, and duplicate detection.

---

## 2. PRISMA 2020 Flow Census

```
┌────────────────────────────────────────────────────────┐
│ Raw Database Harvest: 2,000 Records                    │
│ (1,000 IEEE Xplore + 1,000 Scopus)                     │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼ [Automated Deduplication]
┌────────────────────────────────────────────────────────┐
│ deduplicated_master.csv: 1,716 Unique Records          │
│ (284 Duplicate records documented in dedup_log.csv)    │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼ [Title & Abstract Screening]
┌────────────────────────────────────────────────────────┐
│ screened_included_v2.csv: 501 Records                  │
│ (1,215 Excluded as non-UAV or out of scope)            │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼ [Full-Text Retrieval & Eligibility Assessment]
┌────────────────────────────────────────────────────────┐
│ Assessed for Full-Text Eligibility: 291 Records        │
│ Retrieved as Physical PDFs (03_pdfs/): 291 (100%)      │
│ Excluded Full-Text Studies: 4 Records                  │
│   • E1 (Scope / Metrology Bench Test / Survey): 3      │
│     - REC_0053, REC_0693, REC_0866                     │
│   • E3 (Foreign Language - Chinese Full Text): 1       │
│     - REC_1688 (English translation provided)         │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼ [Synthesis Corpus]
┌────────────────────────────────────────────────────────┐
│ Included Studies in Review: 287 Studies                │
│ (291 Assessed - 4 Excluded = 287 Final Included Corpus)│
│ Extraction Evidence Cards (02_cards/): 291 Cards       │
└────────────────────────────────────────────────────────┘
```

---

## 3. Detailed Reasons for the 4 Full-Text Exclusions (291 → 287)

| Sl. No | Record ID | Title | Exclusion Rule | Methodological & PRISMA Justification |
| :---: | :--- | :--- | :---: | :--- |
| 1 | **`REC_0053`** | *A Survey of Deep Learning Techniques and Computer Vision in Robotic and Drone with Applications* | **Rule E1 (Scope)** | Broad, non-empirical educational review of generic computer vision algorithms (YOLO, CNNs) across robotics/drones; no novel multi-sensor state estimation in GPS-denied environments. |
| 2 | **`REC_0693`** | *Characterization and Testing of a High-Resolution Time-of-Flight Camera for Autonomous Navigation* | **Rule E1 (Scope)** | Isolated laboratory bench-test and sensor metrology study evaluating depth noise and reflectivity of a ToF camera on an optical bench rail; no flying UAV platform or integrated multi-sensor navigation filter. |
| 3 | **`REC_0866`** | *Autonomous Aerial Robots for Search and Rescue Missions* | **Rule E1 (Scope)** | High-level conceptual survey describing search-and-rescue drone missions; contains no algorithmic formulation, state estimation mathematics, or empirical quantitative flight navigation benchmarks. |
| 4 | **`REC_1688`** | *Pose estimation based on laser range finder for a quadrotor unmanned aerial vehicle in GPS-denied environment* | **Rule E3 (Language)** | Full-text published entirely in Chinese (Chinese Control Conference 2013). Excluded under standard PRISMA English-language protocol criteria. Preserved in full-text archive with complete English translation (`REC_1688_translated_EN.txt`) and extraction card. |

---

## 4. Corpus Boundary & File Census

| Collection | Total Files | Included Studies | Excluded Studies | Integrity Status |
| :--- | :---: | :---: | :---: | :--- |
| **PDFs** ([`01_data/03_pdfs/`](file:///e:/slr_project/01_data/03_pdfs/)) | **291** | **287** | 4 | 100% 1-to-1 match with Excel Sl. No (1 to 291) |
| **Evidence Cards** ([`02_cards/`](file:///e:/slr_project/02_cards/)) | **291** | **287** | 4 | 100% 1-to-1 Parity with PDFs & Manifest |
| **Screening Results CSV** | **291** | **287** | 4 | Sl. No 1 to 291 mapped to `id` and `pdf_file_name` |
| **Retrieved Manifest CSV** | **291** | **287** | 4 | Sl. No 1 to 291 mapped to `id` and `pdf_file_name` |

---

## 5. Governance & Freeze Rules
- Every extraction card in `02_cards/` is cryptographically locked with its SHA256 in [`FROZEN_MANIFEST_20260927.csv`](file:///e:/slr_project/02_cards/FROZEN_MANIFEST_20260927.csv).
- Primary corpus denominator for all quantitative synthesis in the review is **287 included studies**.
