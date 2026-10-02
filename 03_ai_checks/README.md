# 03_ai_checks — Phase D Automated Re-Verification & Certification Repository

## Overview
This directory contains the certified, immutable Automated re-verification reports generated during **Phase D — Automated Re-Verification** of the PRISMA 2020 Systematic Literature Review:
*Autonomous Multi-Sensor UAV Navigation in GPS-Denied Environments (2010–2026)*.

Every extraction card in `02_cards/` has been systematically cross-audited against its primary source PDF text layer in `01_data/03_pdfs/` in accordance with the frozen Phase D verification protocol and the 7 Golden Rules.

---

## Verification Protocol & Checks
Each check file (`REC_XXXX.check.md`) documents four comprehensive auditing dimensions:

1. **QUOTE CHECK (Rule R1):**
   - Evaluates all verbatim excerpts and confirms character-exact wording against the underlying PDF text layer.
   - Validates that physical page citations `[p.N]` map accurately to physical page indices within the PDF document.

2. **FACT CHECK (Rule R2):**
   - Validates publication year, digital object identifier (DOI), and bibliographic metadata against publication front matter.
   - Confirms operational mode (`real_or_sim`: `REAL`, `SIM`, or `BOTH`) against reported experimental flights.
   - Verifies reported sensor suites (IMU, cameras, LiDAR, UWB, radar, sonar, magnetometers), algorithmic fusion architectures (EKF, ESKF, UKF, factor graphs, optimization), and dataset benchmarks.

3. **MISSING CHECK (Rule R3):**
   - Audits all fields marked `NOT_REPORTED` to verify whether the source PDF provides explicit empirical parameters.

4. **LABEL CHECK (Rule R4):**
   - Ensures categorical taxonomies (`method_category`, `gps_denied_type`, `fusion_method`, `contribution_type`) are concise standard labels ($\le 10$ words) rather than descriptive paragraphs.

---

## Census & Audit Summary
- **Total Extraction Cards Audited:** 291
- **Total Check Reports Generated:** 291 (`REC_0001.check.md` through `REC_1715.check.md`)
- **Included Studies Certified:** 287 (Rule `I2`)
- **Excluded Studies Audited:** 4 (codes `X1` and `X3`)
  - `REC_0053`: Excluded under code `X1` (General computer vision review)
  - `REC_0693`: Excluded under code `X1` (ToF camera optical bench metrology)
  - `REC_0866`: Excluded under code `X1` (Conceptual search-and-rescue survey)
  - `REC_1688`: Excluded under code `X3` (Foreign Language - Chinese; translated text in `01_data/02_data_proceesed/REC_1688_translated_EN.txt`)
- **Certification Rate:** **100.0%** (`verdict = VERIFIED`, `[SELF-AUDIT: PASS]`)
- **Corpus Eligibility Rule (Rule R6):** Only cards certified with `verification_status: VERIFIED` are permitted to enter the master synthesis file (`04_master/`).
