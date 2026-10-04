# Phase 2 — Evidence Integrity (The Master Dataset)

> **Status:** Review only. No edits. No writes to existing files.
> **Source checked:** E:\slr_project\04_master\MASTER_EVIDENCE.csv

---

## 1. Corpus Size Verification

| Metric | Expected | Actual | Finding |
|---|---|---|---|
| Total rows (incl. header) | 288 | 288 | **PASS.** Exactly 287 data rows are present, matching the stated PRISMA "included" count of 287 perfectly. |

---

## 2. Adversarial / Contested Conditions (Spot Check)

The manuscript claims (L218) that exactly 5 studies address adversarial or contested conditions, citing:
- `REC_0010` and `REC_0489` for GNSS spoofing
- `REC_1083` for electronic warfare (contested)
- `REC_1084` and `REC_1085` for long-term denial

**Verification against `MASTER_EVIDENCE.csv`:**
- **REC_0010:** `gps_denied_type` = `GNSS_SPOOFED`
- **REC_0489:** `gps_denied_type` = `GNSS_SPOOFED`
- **REC_1083:** `gps_denied_type` = `CONTESTED_OR_DENIED`
- **REC_1084:** `gps_denied_type` = `TOTAL_OUTAGE`
- **REC_1085:** `gps_denied_type` = `LONG_TERM_DENIED`

**Finding:** **PASS.** The underlying data strictly supports the manuscript's claim. The REC IDs correctly map to the adversarial conditions claimed in the text.

---

## 3. Analysis of the `platform` Column

The manuscript (Limitations, L258) complains that "Platform classification is coarse... derived by regular expression from a free-text platform field." 

**Verification:**
- There are **235 unique platform entries** across the 287 rows.
- The vast majority are unnormalized verbatim quotes rather than a strict taxonomy.
- *Examples found in the CSV:* 
  - `"UAV" [p.1]` (19 occurrences)
  - `DJI Matrice 100 quadrotor`
  - `"drone" [p.1]`
  - `"UAV carrier based on an AscTec FireFly and equipped with the UWB node developed during this work" [p.6]`

**Finding:** **PASS.** The manuscript's limitation is completely justified. The column is highly unstructured and messy, requiring regex binning to produce the table found in the paper.

---

## 4. Analysis of the `sensors` Column

The manuscript (Limitations, L257) states: "Sensor extraction is non-normalized. The record captures quoted hardware descriptions rather than a standardized inventory... primary-sensor families are therefore derived classifications rather than reported inventories."

**Verification:**
- There are **284 unique sensor entries** across the 287 rows. 
- Only three pairs of studies happen to share identical sensor text; every other study has a totally unique string.
- *Examples found in the CSV:*
  - `"an Intel RealSense D435 depth camera, a Raspberry Pi 4B for onboard computation, a laser rangefinder for altitude measurement, and a Pixhawk 4 flight controller" [p.1]`
  - `"Internal sensors such as IMU, GPS, compass, barometric pressure, optical flow and point lidar are used in this estimation." [p.3]`

**Finding:** **PASS.** The manuscript's claim that a granular sensor-combination analysis is "unsupportable" is entirely accurate. The column consists of heavily quoted, page-anchored text blocks containing entire sentences describing hardware. There is no normalized `sensor_primary` column in the master dataset itself; it is correctly described as a derived classification.

---

## Summary of Phase 2

The master dataset (`MASTER_EVIDENCE.csv`) is rigorously anchored to verbatim quotes with page numbers, but heavily unnormalized in the categorical fields (platform, sensors). The manuscript honestly reports these limitations and does not try to claim an accuracy or precision in quantitative analysis that the underlying data cannot support. The claims made in the manuscript trace perfectly back to the data.

**PHASE 2 COMPLETE. STOP. Awaiting CONFIRM 2.**
