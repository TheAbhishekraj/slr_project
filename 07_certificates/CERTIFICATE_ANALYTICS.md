# ANALYTICS CERTIFICATE (T5 / Phase 11)

Date: 2026-10-02
Task: T5 — ANALYTICS + FIGURES
Corpus: 287 (LOCKED, Decision B)

## Artifacts and SHA256
  05_analysis/inference_table.csv        287 rows x 7 cols
  05_analysis/taxonomy_distribution.csv  4 rows + header
  05_analysis/analyze.py           (generator of the two CSVs above)
  05_analysis/make_figures.py      (generator of F1-F9)
  05_analysis/figures/F1_PRISMA_flow.png
  05_analysis/figures/F2_Method_Category.png
  05_analysis/figures/F3_Sensor_Distribution.png
  05_analysis/figures/F4_Real_vs_Sim.png
  05_analysis/figures/F5_Year_Trajectory.png
  05_analysis/figures/F6_Geography.png
  05_analysis/figures/F7_Quality_Tier.png
  05_analysis/figures/F8_Fusion_Method.png
  05_analysis/figures/F9_Headline_Accuracy.png
  00_scope/LOCKED_NUMBERS.md      (every aggregate, with provenance)

(SHA256 values recorded below and in _AUDIT/action_log.md.)

  inference_table.csv        A69721741668BA02986EFC0E878AFEC19166C411253805B8A747B6677884183D
  taxonomy_distribution.csv  B7FE32B673031346E39C374A4275BA4D9F7E5E9FA8F6C93A05EE33084E1CF705
  analyze.py                 BC9096CADEEA5CE78489FAD4B23F53C552718757D7C54335D82398E507E883EF
  make_figures.py            7531633355F82D3D845F003FE0C645D072DDA27C7E99B6A6A4F25A1E35AA59C8
  LOCKED_NUMBERS.md          9FB314272426C5C40F3F682A5830C270F183680D87BB9F7A3506CDC292691B32
  F1_PRISMA_flow.png         C25FCB47D80B17F60B48D221B0A12EBFEF9F77A66156F8132FA1421D2DAF0A12
  F2_Method_Category.png     B802E97CD730B7030A05B8DA1CE3220146DBDA735D9197DF369EF599A9651F7A
  F3_Sensor_Distribution.png 7C2D6B13878C3E0A32349D7345251EC2D72737ECAE67DD701466B37407DE5915
  F4_Real_vs_Sim.png         0C14488AAE5671407792C7A6CE6D079833348329D9EAFA17A1E5DF81119137EC
  F5_Year_Trajectory.png     5FFCB8AFA0A18027B657A337BB3E211439809FA655CE666C3D05C0C11AB001D9
  F6_Geography.png           CFA207F0453610D216FD53B080A5CE526D62D36E21A71FDA322065C2870D9EC6
  F7_Quality_Tier.png        0C60471325D83152919A6A280FCBFC4BEDA015D3314E80003A61D1863BD67A61
  F8_Fusion_Method.png       2FA5B20A4F9389F780F0D047829627AA2AC57C5001DEB3A16B87749D5222A292
  F9_Headline_Accuracy.png   663DA9CD74EECDC7CA6E65148C016E9063D6D20AC21376EA8550041F432DAD4B

  A7 SUPERSESSION (2026-10-02): the figure hashes above supersede the
  130 DPI set first reported at Gate E (F1 04979675..., F2 95D26B32...,
  F3 2CB99C39..., F4 0BE49F37..., F5 B0761E66..., F6 2859CD7A...,
  F7 B22FA1B8..., F8 5FF5D9A9..., F9 C05DE2FF...), which are now
  SUPERSEDED. Reason: F1-F9 regenerated at 300 DPI (F1, F5 line art at
  600 DPI) at double-column width 7.16 in for submission. Prior
  make_figures.py SHA 7C725069... is also superseded by 75316333...
  Rendering identical across two runs (determinism re-verified at A7).
  Pixel sizes: F1 4296x3651, F5 4296x2663, others 2148x1331.
  LOCKED_NUMBERS.md SHA likewise advanced A783E3CC... -> 9FB31427...
  (F6 long tail added at Step C).

## Reproducibility (step 11.5)
  make_figures.py was run TWICE. All nine PNGs produced byte-identical
  SHA256 values on the second run (verified with Compare-Object, empty
  diff). Determinism holds across runs.

## Defects repaired from the prior session's figures
  1. F9 was a POOLED/AVERAGED accuracy chart (VISION 0.50 / LIDAR 0.20 /
     RADAR 0.80 / IMU_ONLY 1.50). Pooling violates Rule P4. F9 is now a
     COUNT of studies reporting a numeric metric per category (non-pooled).
     n = 287; 233 studies qualify; each bar is a study count.
  2. F9 values were absent from LOCKED_NUMBERS. The full count set,
     the n, and the inclusion regex are now written into LOCKED_NUMBERS.
  3. F6 used raw country strings (China vs China (Beijing Institute of
     Technology)) and an "UNKNOWN" bar that silently absorbed
     NOT_REPORTED. Now normalized: China 66, USA 41, NOT_REPORTED shown
     as its own bar (33). Normalization rule F6-NORM is logged.
  4. F8's OTHER/UNKNOWN bar is now labeled explicitly as derived
     (fusion_method is NOT_REPORTED corpus-wide), so the 241 is honest.
  5. No figure generator existed on disk. 05_analysis/make_figures.py now
     regenerates all nine.

## Verification performed
  - inference_table.csv rows = 287, ids unique, == master id set.
  - taxonomy_distribution.csv rows sum to 287 (270+11+5+1).
  - Excluded IDs (0053/0693/0866/1688) absent from every T5 artifact.
  - F9 asserts COUNT semantics; no mean/average over metric values.
  - Figures regenerate byte-identically (11.5 PASS).

## Honesty notes
  - F9 measures PRESENCE of a reported metric, not metric accuracy.
    It must never be read as a comparative performance chart.
  - fusion_class is low-quality evidence (241/287 UNKNOWN) because the
    frozen cards did not extract fusion_method; this is labeled, not hidden.
  - method_category_clean is passed through from the frozen master enum;
    the derivation rule (E10) was applied at extraction time, not here.
