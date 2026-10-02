# SCOPE.md

**Project:** GPS-Denied Navigation for UAVs — Multi-Sensor Fusion (2010–2026)
**Protocol:** PRISMA 2020
**Status:** Frozen 2026-10-02
**Supersedes:** v2, v3, v4, v5 (retained in `07_certificates/old_scopes/`)
**Authority:** `07_certificates/CENSUS_AUDIT_REPORT_20261002.md`
**Corpus authority:** `04_master/MASTER_EVIDENCE.csv` (287 × 28)
**Any change after freezing requires a new version file with a written reason.**

---

## Q1. Review title and scope rationale

**Title:** GPS-Denied Navigation for UAVs: A Systematic Literature Review of Multi-Sensor Fusion Approaches (2010–2026)

**Terminology rationale.** Throughout this review, "GPS-denied" is used as the standard umbrella terminology in aerospace and robotics literature. It encompasses broader GNSS-denied operational conditions (loss, degradation, jamming, spoofing, or multipath attenuation of GPS, GLONASS, Galileo, and BeiDou signals in indoor, subterranean, urban canyon, canopy, and contested environments).

---

## Q2. Research questions and operational definitions

### Research Questions

- **RQ1 (Sensors & Trends):** Which sensor-fusion configurations (camera, LiDAR, IMU, radar, UWB, barometer, ultrasonic) are most commonly used for GPS-denied UAV navigation, and how has their prevalence shifted between 2010 and 2026?

- **RQ2 (Accuracy & Environments):** What localization accuracy and robustness metrics are reported across different GPS-denied environments (indoor, urban canyon, subterranean, forest, adversarial), and how do they vary by environment and platform?

- **RQ3 (Algorithmic Approaches & Validation):** Which algorithmic approaches (VIO, SLAM, LIO, filter-based fusion, learning-based methods) dominate the literature, and how do they compare on validation type (real flight vs. simulation) and reported performance?

- **RQ4 (Limitations & Adversarial Conditions):** What limitations and future research directions are identified in the corpus, particularly regarding adversarial conditions, electronic warfare (jamming/spoofing), and resource-constrained edge platforms?

### Operational taxonomies and coding rules

**Sensor modalities:**
- *Proprioceptive:* IMU/INS (gyroscopes, accelerometers).
- *Exteroceptive:* Optical cameras (monocular, stereo, RGB-D, event), LiDAR (2D, 3D mechanical, solid-state), Radar (mmWave, FMCW), UWB RF ranging, acoustic/ultrasonic altimeters, barometric altimeters, magnetometers.

**Sensor fusion categories:**
- *Loosely coupled:* independent per-sensor estimation, then state-level filtering.
- *Tightly coupled:* joint optimization or filtering directly over raw sensor measurements (e.g., visual feature tracks + IMU pre-integration).
- *Optimization-based / factor graph:* non-linear least-squares smoothing over sliding windows or full graphs.
- *Filter-based:* EKF, UKF, MSCKF, particle filter.
- *Multi-label rule:* hybrid architectures (e.g., tightly coupled VIO front-end with pose-graph back-end) are coded hierarchically with primary front-end and back-end labels recorded.

**Environment taxonomy:**
- *MIXED:* study evaluates in more than one environment (Note: originally planned Open/Transition is folded into this).
- *INDOOR:* structured buildings, corridors, rooms, warehouses.
- *UNDERGROUND:* tunnels, mines, caves, culverts, underground structures.
- *FOREST / VEGETATED:* natural canopy, agricultural orchards, unstructured outdoor clutter.
- *URBAN_CANYON:* high-rise corridors, multipath-heavy urban.
- *ADVERSARIAL_CONTESTED:* RF jamming, GPS spoofing, contested operational zones.
- *NOT_REPORTED:* no specific environment reported.

**Platform taxonomy:**
- Multi-rotor (quadrotor, hexarotor, octocopter), fixed-wing, hybrid VTOL, flapping-wing / MAV.

**Reported accuracy and robustness metrics:**
- ATE / RMSE (meters), RPE (drift per meter or % distance traveled), success/failure rate, update latency / frame rate (Hz).

---

## Q3. Databases searched and full search strategy

### Information sources

Two primary indexing databases in engineering and applied sciences:
1. IEEE Xplore (`ieeexplore.ieee.org`)
2. Scopus (`scopus.com`)

### Full search strings and parameters (executed 2026-06-15)

**IEEE Xplore**

```text
("GPS-denied" OR "GNSS-denied" OR "GPS denied" OR "GNSS denied"
 OR "GPS-degraded" OR "GPS free" OR "GPS-free"
 OR "navigation without GPS")
AND ("UAV" OR "unmanned aerial vehicle" OR "drone" OR "quadrotor"
 OR "multirotor" OR "fixed-wing" OR "rotary-wing")
AND ("localization" OR "navigation" OR "SLAM" OR "odometry" OR "positioning")
```

- **Filters:** Publication Year 2010–2026; Content Type: Conference Publications, Journals; Language: English.
- **Yield:** ~3,200 initial hits; ~2,800 after document/language filters; **1,000** exported (relevance-ranked standard harvest cap).
- **Raw export:** `01_data/ieee_xplore_20260615.csv`.

**Scopus**

```text
TITLE-ABS-KEY(
  ("GPS-denied" OR "GNSS-denied" OR "GPS denied" OR "GNSS denied"
   OR "GPS-degraded" OR "GPS-free" OR "navigation without GPS")
  AND ("UAV" OR "unmanned aerial vehicle" OR "drone" OR "quadrotor"
   OR "multirotor")
  AND ("localization" OR "navigation" OR "SLAM" OR "odometry"
   OR "sensor fusion" OR "positioning")
)
```

- **Filters:** Publication Year 2010–2026; Document Type: Conference Paper, Article; Language: English.
- **Yield:** ~4,100 initial hits; ~3,800 after document/language filters; **1,000** exported.
- **Raw export:** `01_data/scopus_20260615.csv`.

**Total harvested corpus:** exactly **2,000 raw records** (1,000 IEEE + 1,000 Scopus), logged in `01_data/SEARCH_LOG.md`.

---

## Q4. Search window and temporal coverage

- **Search execution date:** 2026-06-15.
- **Search window:** 2010-01-01 to 2026-06-15 (inclusive).
- **Partial year 2026:** searches executed 2026-06-15. Literature indexed for 2026 is partial (January 1 – mid-June). All temporal trend analyses report 2026 as partial and do not annualize it.

---

## Q5. Inclusion criteria

- **I1 (Date):** Published between 2010-01-01 and 2026-06-15.
- **I2 (Language):** Written and published in English.
- **I3 (Document type):** Peer-reviewed journal article or full conference proceeding.
- **I4 (Primary topic):** Addresses GPS/GNSS-denied, degraded, or contested aerial navigation as the central research focus.
- **I5 (Platform focus):** Focuses explicitly on UAVs (drones, UAS, MAVs).
- **I6 (Multi-sensor fusion):** Implements or evaluates an integrated multi-sensor navigation solution fusing measurements from at least two distinct sensing modalities. Single-sensor-only approaches are excluded.
- **I7 (Empirical validation):** Presents empirical quantitative validation via physical real-world UAV flight tests, ground-robot flight-surrogate experiments, or high-fidelity simulation.

---

## Q6. Exclusion criteria

- **E1 (No validation):** Purely conceptual, tutorial, or theoretical papers.
- **E2 (GPS-dependent):** Systems requiring active, uninterrupted nominal GNSS signals.
- **E3 (Non-UAV platforms):** Ground vehicles, AUVs, spacecraft, non-aerial robotics.
- **E4 (Single-sensor):** Single-sensor navigation methods lacking multi-sensor fusion.
- **E5 (Non-English):** Publications in languages other than English.
- **E6 (Pre-2010):** Articles published prior to 2010-01-01.
- **E7 (Non-peer-reviewed):** Unrefereed preprints, trade magazines, white papers, patents, books, theses, extended abstracts.
- **E8 (Duplicates):** Duplicate records across IEEE Xplore and Scopus.
- **E9 (Retractions):** Formally retracted articles.
- **E10 (No extractable data):** Papers lacking extractable localization accuracy, error metrics, or quantitative performance data.

**Note on X1 / X3 labels.** Full-text exclusions use `X1` (out of scope) and `X3` (foreign language), superseding `E3`-labeled exclusions to avoid collision with `EXTRACTION_RULES.md` E1–E12.

---

## Q7. Quality appraisal framework (0–10 scale)

Four methodological dimensions:

**A. Experimental rigor (0–4 points)**
- `+2`: real-world experimental flight tests on a physical UAV platform.
- `+1`: ground-truth reference comparison (RTK-GPS, motion capture, total station, survey-grade map).
- `+1`: repeatability reporting (multiple runs with variance, SD, or confidence intervals). Code/dataset release is scored under Dimension D to avoid double-counting.

**B. Reporting completeness (0–3 points)**
- `+1`: quantitative trajectory error (ATE / RMSE and relative drift / odometry error).
- `+1`: operational environment parameters (trajectory length, flight duration, spatial scale).
- `+1`: robustness characterization (failure modes, edge cases, latency, ablation).

**C. Baseline fairness (0–2 points)**
- `+1`: direct quantitative comparison against an established benchmark (VINS-Mono, ORB-SLAM3, LIO-SAM, standard EKF).
- `+1`: baseline evaluated under matched conditions or identical benchmark datasets.

**D. Reproducibility (0–1 point)**
- `+1`: public release of open-source codebase, raw dataset, or full hardware BOM and calibration specs.

### Quality tiers
- **Q-High:** 8–10 points.
- **Q-Medium:** 5–7 points.
- **Q-Low:** 0–4 points.

### Simulation cap policy
Simulation-only papers cannot be classified Q-High regardless of raw points. A simulation-only study scoring 8–10 is capped at **Q-Medium (capped)**, with raw score preserved in logs.

### Appraisal procedure and inter-rater reliability
Calibration on an initial dual-appraiser sample of 20% of eligible studies. Inter-rater agreement via weighted Cohen's Kappa (κ ≥ 0.75) or ICC(2,1) ≥ 0.75. Discrepancies resolved by consensus with reference to verbatim evidence quotes.

**⚠ Verify:** did the project actually perform this calibration? If yes, the kappa value must appear in Methods. If no, the manuscript cannot claim it.

---

## Q8. Venue inclusion and exclusion

### Included venues
Peer-reviewed journals and conference proceedings indexed in IEEE Xplore, Scopus, or Web of Science. Representative examples:
- IEEE Transactions on Robotics (T-RO)
- IEEE Robotics and Automation Letters (RA-L)
- IROS, ICRA
- Journal of Field Robotics (JFR)
- GPS Solutions (Springer)
- Navigation: Journal of the Institute of Navigation (ION)
- Sensors (MDPI)
- IEEE Sensors Journal
- Drones / Aerospace (MDPI)

### Excluded venues
- Predatory or non-indexed journals.
- Unindexed workshops, non-peer-reviewed symposium presentations, vendor white papers.
- Venues outside robotics, aerospace, sensing, navigation.

---

## Q9. Language filter

English only.

---

## Q10. Document types

- **Included:** peer-reviewed journal articles and full peer-reviewed conference papers.
- **Excluded:** books, edited volumes, book chapters, theses, dissertations, letters to the editor, editorials, conference extended abstracts without peer review, non-refereed preprints.

---

## Q11. Synthesis and review workflow alignment

PRISMA 2020 pipeline:

1. **Deduplication:** cross-database matching (DOI, normalized title Levenshtein ≥ 0.95, year).
2. **Screening:** title/abstract then full-text against I1–I7 and E1–E10.
3. **Data extraction:** 28-column structured evidence extraction with verbatim quote anchoring (`00_scope/EXTRACTION_SCHEMA.md`).
4. **Synthesis:** narrative synthesis grouped by sensor combination and algorithm paradigm, supported by taxonomy tables and performance distributions.

---

## Appendix A — Pipeline census (frozen 2026-10-02)

| Stage | Count |
|---|---|
| Raw harvested | 2,000 |
| Duplicates removed | 284 |
| Unique records | 1,716 |
| Screened in | 501 |
| Full-text retrieved | 291 (100% retrieval) |
| Full-text excluded | 4 |
| — X1 out of scope | 3 (REC_0053, REC_0693, REC_0866) |
| — X3 non-English | 1 (REC_1688) |
| **Included (frozen denominator)** | **287** |

Every included study has a verified full-text PDF in `01_data/03_pdfs/` and an extraction card in `02_cards/`.

---

## Appendix B — Corpus asset verification

- 291 PDFs in `01_data/03_pdfs/` matching Sl. No 1–291 in the PRISMA master workbook.
- 291 extraction cards in `02_cards/` tracked by the frozen manifest.
- 287 INCLUDE records (Rule I2) and 4 EXCLUDE records (X1/X3) in the screening and retrieval files.

---

## Appendix C — Frozen artifacts and hashes

| Artifact | SHA256 |
|---|---|
| `04_master/MASTER_EVIDENCE.csv` (287 × 28) | `88F94A9EB023E12502D2F12342FD658D0878C6DAA66A99986CC8F151D0D888BA` |
| `04_master/MASTER_EVIDENCE_extended.csv` (287 × 29) | `08FC0C9413259EE47A5DC4B25DD9145A4804C651DD05188B5F8C1EFC86D451E5` |
| X3 evidence | `926a229415d9df488843413fc6a2a099ca3430f05017c8de8fc7a915de88ab8c` |
| `00_scope/LOCKED_NUMBERS.md` | `9FB314272426C5C40F3F682A5830C270F183680D87BB9F7A3506CDC292691B32` |

---

## Appendix D — Known discrepancies to reconcile

1. **Manifest filename.** This file references `FROZEN_MANIFEST_20260927.csv` (per `AUDIT_PROMPT.md §2`). The live manifest on disk is `FROZEN_MANIFEST_20261002.csv`. Reconcile: either the manifest was renamed, or two manifests exist.

2. **Path drift.** Earlier drafts of this scope referenced `01_data_raw/`, `02_data_processed/`, `08_docs/`. Current project layout uses `01_data/`, `02_cards/`, `00_scope/`. Paths in this file have been reconciled to the live tree.

3. **Inter-rater reliability.** Q7 describes a 20% dual-appraiser calibration with κ ≥ 0.75. Verify whether this was performed. If not performed, soften Q7 and state plainly in Methods.

4. **Missing exclusion-stage counts.** The corpus census traces 4 full-text exclusions. Stage-wise exclusion counts (by E1–E10) are not recorded. If Methods cites them, they must be derived from the screening files, not invented.

---

*End of SCOPE.md*
