# NUMBER_TRACE.md

This file bridges the locked aggregates (`LOCKED_NUMBERS.md`) and the card-level extractions with the final manuscript. Every number cited in the manuscript must appear here.

**E10 Derivation Note (Platform Taxonomy):** The Platform counts (RQ2) are derived by a regular expression applied to the free-text `platform` column in `MASTER_EVIDENCE.csv`. The specific regex logic applied is:
- MULTI_ROTOR: `r'quad|hex|oct|multi-?rotor|dji|parrot|crazyflie|pixhawk|holybro'`
- FIXED_WING: `r'fixed-?wing|plane'`
- HYBRID_VTOL: `r'vtol|hybrid'`
- FLAPPING_WING_MAV: `r'flap|mav|micro'`
- SWARM: `r'swarm'`
- GENERIC_UAV: `r'uav|drone|vehicle'`
- NOT_REPORTED: `'not_reported' or 'not reported'`
- OTHER: Fallthrough

| manuscript_section | value | unit | source_file | rec_id | column | page | quote | qa_tier |
|---|---|---|---|---|---|---|---|---|
| Abstract | 287 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate) | - |
| Methods | 2,000 | raw records | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate) | - |
| Methods | 284 | duplicates | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate) | - |
| Methods | 1,716 | unique records | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate) | - |
| Methods | 1,215 | records | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate) | - |
| Methods | 501 | screened-in | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate) | - |
| Methods | 210 | records | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - excluded at full text) | - |
| Methods | 291 | full-text | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate) | - |
| Methods | 4 | excluded | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate) | - |
| Methods | 3 | out-of-scope | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate) | - |
| Methods | 1 | non-English | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate) | - |
| Methods | 145 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate) | - |
| Methods | 118 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate) | - |
| Methods | 24 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate) | - |
| Methods | 3.648 | rigor mean | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate) | - |
| Methods | 2.739 | reporting mean | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate) | - |
| Methods | 1.376 | baseline mean | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate) | - |
| Methods | 0.230 | repro mean | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate) | - |
| Methods | 7.9930 | overall mean | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate) | - |
| Results RQ1 | 78 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - HYBRID) | - |
| Results RQ1 | 55 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - VISION_OBJECT) | - |
| Results RQ1 | 41 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - COOPERATIVE) | - |
| Results RQ1 | 29 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - OTHER method) | - |
| Results RQ1 | 19 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - VIO) | - |
| Results RQ1 | 16 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - UNKNOWN method) | - |
| Results RQ1 | 13 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - SLAM) | - |
| Results RQ1 | 9 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - LIDAR) | - |
| Results RQ1 | 8 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - UWB) | - |
| Results RQ1 | 8 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - SURVEY) | - |
| Results RQ1 | 1 | study | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - QUANTUM) | - |
| Results RQ1 | 1 | study | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - OPTICAL_FLOW) | - |
| Results RQ1 | 1 | study | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - SYSTEM) | - |
| Results RQ1 | 1 | study | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - TERRAIN_AIDED_NAVIGATION) | - |
| Results RQ1 | 1 | study | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - DEEP_LEARNING_ODOMETRY) | - |
| Results RQ1 | 1 | study | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - VISUAL_INERTIAL) | - |
| Results RQ1 | 1 | study | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - MULTI_SENSOR_FUSION) | - |
| Results RQ1 | 1 | study | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - COOPERATIVE_SWARM_LOCALIZATION) | - |
| Results RQ1 | 1 | study | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - RADAR) | - |
| Results RQ1 | 1 | study | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - DATASET) | - |
| Results RQ1 | 1 | study | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - VSLAM) | - |
| Results RQ1 | 182 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - VISION sensor) | - |
| Results RQ1 | 35 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - IMU_ONLY sensor) | - |
| Results RQ1 | 27 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - OTHER sensor) | - |
| Results RQ1 | 22 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - LIDAR sensor) | - |
| Results RQ1 | 14 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - UWB sensor) | - |
| Results RQ1 | 7 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - RADAR sensor) | - |
| Results RQ1 | 9 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - pre-2016) | - |
| Results RQ1 | 96 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - 2016-2020) | - |
| Results RQ1 | 182 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - 2021-2026) | - |
| Results RQ2 | 233 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - Numeric Accuracy) | - |
| Results RQ2 | 54 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - NOT_REPORTED accuracy) | - |
| Results RQ2 | 192 | studies | inference_table.csv | - | - | - | N/A (aggregate - MIXED environment) | - |
| Results RQ2 | 72 | studies | inference_table.csv | - | - | - | N/A (aggregate - INDOOR environment) | - |
| Results RQ2 | 7 | studies | inference_table.csv | - | - | - | N/A (aggregate - UNDERGROUND) | - |
| Results RQ2 | 5 | studies | inference_table.csv | - | - | - | N/A (aggregate - ADVERSARIAL_CONTESTED) | - |
| Results RQ2 | 5 | studies | inference_table.csv | - | - | - | N/A (aggregate - FOREST) | - |
| Results RQ2 | 4 | studies | inference_table.csv | - | - | - | N/A (aggregate - URBAN_CANYON) | - |
| Results RQ2 | 2 | studies | inference_table.csv | - | - | - | N/A (aggregate - NOT_REPORTED env) | - |
| Results RQ2 | 134 | studies | MASTER_EVIDENCE.csv | - | - | - | N/A (Regex derived - MULTI_ROTOR) | - |
| Results RQ2 | 99 | studies | MASTER_EVIDENCE.csv | - | - | - | N/A (Regex derived - GENERIC_UAV) | - |
| Results RQ2 | 18 | studies | MASTER_EVIDENCE.csv | - | - | - | N/A (Regex derived - OTHER platform) | - |
| Results RQ2 | 11 | studies | MASTER_EVIDENCE.csv | - | - | - | N/A (Regex derived - FLAPPING_WING_MAV) | - |
| Results RQ2 | 10 | studies | MASTER_EVIDENCE.csv | - | - | - | N/A (Regex derived - SWARM) | - |
| Results RQ2 | 10 | studies | MASTER_EVIDENCE.csv | - | - | - | N/A (Regex derived - FIXED_WING) | - |
| Results RQ2 | 3 | studies | MASTER_EVIDENCE.csv | - | - | - | N/A (Regex derived - HYBRID_VTOL) | - |
| Results RQ2 | 2 | studies | MASTER_EVIDENCE.csv | - | - | - | N/A (Regex derived - NOT_REPORTED platform) | - |
| Results RQ3 | 241 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - OTHER/UNKNOWN fusion) | - |
| Results RQ3 | 45 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - KALMAN_FILTER fusion) | - |
| Results RQ3 | 1 | study | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - FACTOR_GRAPH fusion) | - |
| Results RQ3 | 123 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - REAL validation) | - |
| Results RQ3 | 88 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - BOTH validation) | - |
| Results RQ3 | 69 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - SIM validation) | - |
| Results RQ3 | 7 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - NOT_REPORTED validation) | - |
| Results RQ3 | 270 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - Taxonomy CORE) | - |
| Results RQ3 | 11 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - Taxonomy IMPORTANT) | - |
| Results RQ3 | 5 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - Taxonomy NOT_REPORTED) | - |
| Results RQ3 | 1 | study | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - Taxonomy PERIPHERAL) | - |
| Results RQ4 | 217 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - Top 10 countries) | - |
| Results RQ4 | 66 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - China normalized) | - |
| Results RQ4 | 41 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - USA normalized) | - |
| Results RQ4 | 33 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - NOT_REPORTED normalized) | - |
| Results RQ4 | 14 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - Canada normalized) | - |
| Results RQ4 | 12 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - Australia normalized) | - |
| Results RQ4 | 11 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - India normalized) | - |
| Results RQ4 | 11 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - Singapore normalized) | - |
| Results RQ4 | 11 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - Taiwan normalized) | - |
| Results RQ4 | 10 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - Spain normalized) | - |
| Results RQ4 | 8 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - Germany normalized) | - |
| Results RQ4 | 70 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - Long tail geography) | - |
| Results RQ4 | 32 | countries | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - Long tail geography) | - |
| Limitations | 287 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - Corpus Scope) | - |
| Limitations | 49 | studies | LOCKED_NUMBERS.md | - | - | - | N/A (aggregate - subset of Q-Medium) | - |

## Tier 2 — RQ1

### Sub-table 2b: Sensor x Year (cross-tabulation)

| manuscript_section | value | unit | source_file | rec_id | column | page | quote | qa_tier |
|---|---|---|---|---|---|---|---|---|
| Results RQ1 | 6 | studies | inference_table.csv | - | sensor_primary x year_bucket | - | N/A (cross-tab VISION 2010-2015) | - |
| Results RQ1 | 66 | studies | inference_table.csv | - | sensor_primary x year_bucket | - | N/A (cross-tab VISION 2016-2020) | - |
| Results RQ1 | 110 | studies | inference_table.csv | - | sensor_primary x year_bucket | - | N/A (cross-tab VISION 2021-2026) | - |
| Results RQ1 | 0 | studies | inference_table.csv | - | sensor_primary x year_bucket | - | N/A (cross-tab IMU_ONLY 2010-2015) | - |
| Results RQ1 | 9 | studies | inference_table.csv | - | sensor_primary x year_bucket | - | N/A (cross-tab IMU_ONLY 2016-2020) | - |
| Results RQ1 | 26 | studies | inference_table.csv | - | sensor_primary x year_bucket | - | N/A (cross-tab IMU_ONLY 2021-2026) | - |
| Results RQ1 | 2 | studies | inference_table.csv | - | sensor_primary x year_bucket | - | N/A (cross-tab OTHER 2010-2015) | - |
| Results RQ1 | 11 | studies | inference_table.csv | - | sensor_primary x year_bucket | - | N/A (cross-tab OTHER 2016-2020) | - |
| Results RQ1 | 14 | studies | inference_table.csv | - | sensor_primary x year_bucket | - | N/A (cross-tab OTHER 2021-2026) | - |
| Results RQ1 | 1 | studies | inference_table.csv | - | sensor_primary x year_bucket | - | N/A (cross-tab LIDAR 2010-2015) | - |
| Results RQ1 | 5 | studies | inference_table.csv | - | sensor_primary x year_bucket | - | N/A (cross-tab LIDAR 2016-2020) | - |
| Results RQ1 | 16 | studies | inference_table.csv | - | sensor_primary x year_bucket | - | N/A (cross-tab LIDAR 2021-2026) | - |
| Results RQ1 | 0 | studies | inference_table.csv | - | sensor_primary x year_bucket | - | N/A (cross-tab UWB 2010-2015) | - |
| Results RQ1 | 3 | studies | inference_table.csv | - | sensor_primary x year_bucket | - | N/A (cross-tab UWB 2016-2020) | - |
| Results RQ1 | 11 | studies | inference_table.csv | - | sensor_primary x year_bucket | - | N/A (cross-tab UWB 2021-2026) | - |
| Results RQ1 | 0 | studies | inference_table.csv | - | sensor_primary x year_bucket | - | N/A (cross-tab RADAR 2010-2015) | - |
| Results RQ1 | 2 | studies | inference_table.csv | - | sensor_primary x year_bucket | - | N/A (cross-tab RADAR 2016-2020) | - |
| Results RQ1 | 5 | studies | inference_table.csv | - | sensor_primary x year_bucket | - | N/A (cross-tab RADAR 2021-2026) | - |

### Sub-table 2c: Illustrative Anchors (RQ1)

These are not trace rows. They are card-exact quotes anchoring each sensor family to a specific study.

| sensor_family | rec_id | card_line | quote (character-exact from card) |
|---|---|---|---|
| VISION | REC_0001 | L35 | "The inputs of the proposed framework include the building BIM model and the image sequence captured by the onboard UAV camera" [p.1] |
| IMU_ONLY | REC_0195 | L35 | "inertial navigation (INS)" [p.1] |
| LIDAR | REC_0057 | L35 | "LIDAR sensor, which is the key component for SLAM algorithm is modeled in details in Unity3D script." [p.2] |
| UWB | REC_0115 | L35 | "Inertial Measurement Unit (IMU)" as primary, "Ultra-wideband system (UWB)" as secondary [p.1] |
| RADAR | REC_0071 | L35 | "24 GHz FMCW cooperative radar" [p.1] |


Misclassification scan withdrawn. The extraction record for sensor fields is a partial, non-normalized capture of quoted descriptions. Validating sensor_primary against it produces false positives in both directions. Primary-sensor classification is therefore reported as derived (Fig. 3) and not independently validated. The same limitation applies to sub-table 2a.

Misclassification scan withdrawn. The extraction record for sensor fields is a partial, non-normalized capture of quoted descriptions. Validating sensor_primary against it produces false positives in both directions. Primary-sensor classification is therefore reported as derived (Fig. 3) and not independently validated. The same limitation applies to sub-table 2a.
| CORRECTION | Duplicate withdrawal paragraph above. See rules_log row 2026-10-03 CORRECTION. Original paragraph stands once. |
