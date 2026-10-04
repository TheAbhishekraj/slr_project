# Kappa Calibration — Methodology and Status

## What is Kappa?

Cohen's Kappa (κ) measures agreement between two independent
raters on a classification task, corrected for chance. Values:

| κ range   | Interpretation     |
|-----------|--------------------|
| < 0.20    | Poor              |
| 0.21–0.40 | Fair              |
| 0.41–0.60 | Moderate          |
| 0.61–0.80 | Substantial       |
| 0.81–1.00 | Almost perfect    |

Weighted Kappa is used when raters assign ordinal scores, as in
this project's 10-point quality appraisal rubric.

## What the project scope specifies

SCOPE.md Q7 defines a 20% dual-appraiser calibration:

- Sample size: 20% of eligible studies (approximately 58 studies)
- Two appraisers independently score each study
- Inter-rater agreement measured via weighted Cohen's Kappa
- Target: κ ≥ 0.75
- If met, one appraiser proceeds solo for the remainder

Reference: SCOPE.md lines 175–178 and 270.

## What was actually done

### Status C — Not verifiable
The calibration was specified in SCOPE.md but no record of
execution exists in the current audit trail. The value is
unknown.

## How the manuscript reports this

Section 3.6 states:

> "SCOPE.md specifies a 20% dual-appraiser calibration sample with a target weighted Cohen's Kappa of 0.75 or higher. The specific Kappa value could not be recovered from the current audit records. Accordingly, we do not claim a specific inter-rater reliability figure."

## How to explain this to a supervisor

If asked:

> "The 20% dual-appraiser calibration was specified in the
> project scope. The calibration record could not be located; the
> manuscript does not claim a specific reliability figure."

## Related documents

- SCOPE.md §Appraisal procedure and inter-rater reliability
- SCREENING_INDEPENDENCE.md (screening independence — Case C)
- PRISMA_CHECKLIST.md item 9 (extraction independence — status)

## Action log

| Date       | Action                                     |
|------------|--------------------------------------------|
| 2026-10-04 | README created                             |
| 2026-10-04 | Search for calibration record completed    |
| 2026-10-04 | Result: not found                          |
