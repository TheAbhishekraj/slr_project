# PHASE C — MANUAL EXTRACTION (you + PDF, one card per paper)

For each PDF in `01_data/03_pdfs/`, create `02_cards/REC_XXXX.md` using this exact shape:

---- CARD TEMPLATE (copy for every paper) ----
ID: REC_XXXX
FIELDS:
title: ...
authors: ...            (if not on the paper: NOT_REPORTED)
year: ...
venue: ...
doi: ...
country: ...            (country of the AUTHORS' institution)
problem: """exact words from the paper""" [p.N]
motivation: """exact words""" [p.N]   (or NOT_REPORTED)
approach_summary: """exact words""" [p.N]
method_category: short label you choose (e.g., visual-inertial, lidar-inertial)
sensors: comma list (camera, IMU, lidar, ...)
gps_denied_type: short label (e.g., total outage, denied indoors)
fusion_method: short label (e.g., EKF, factor graph)
algorithm: name of the named method, or NOT_REPORTED
dataset: name, or NOT_REPORTED
platform: UAV type, or NOT_REPORTED
contribution_type: short label (e.g., new method, survey, dataset)
real_or_sim: REAL or SIM or BOTH or NOT_REPORTED
baseline: what the paper compares against, or NOT_REPORTED
headline_result: """exact words, the strongest number/claim""" [p.N]
metrics: """exact words""" [p.N]   (or NOT_REPORTED)
ablation: """exact words""" [p.N]  (or NOT_REPORTED)
limitations: """exact words""" [p.N] (or NOT_REPORTED)
future_work: """exact words""" [p.N] (or NOT_REPORTED)
funding: agency name, or NOT_REPORTED
notes: anything odd about the PDF (pages missing, etc.)
verification_status: PENDING
---- END TEMPLATE ----

YOUR 5 HAND-CHECKS after each card (takes 2 minutes, do them all):

1. Every """quoted""" field has a [p.N] and the quote is copy-paste exact.
2. year and doi match the PDF's first page.
3. real_or_sim matches what you actually read (real flight? simulation?).
4. id matches the PDF filename.
5. verification_status says PENDING (you never write VERIFIED yourself).
