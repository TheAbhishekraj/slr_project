# EXTRACTION SCHEMA (28 columns)

## IDENTITY (7)
* id
* title
* authors
* year
* venue
* doi
* country

## CONTENT (11)
* problem
* motivation
* approach_summary
* method_category
* sensors
* gps_denied_type
* fusion_method
* algorithm
* dataset
* platform
* contribution_type

## EVIDENCE (10)
* real_or_sim
* baseline
* headline_result
* metrics
* ablation
* limitations
* future_work
* funding
* notes
* verification_status

**Rule for the EVIDENCE group:** Every text field that quotes the paper must carry a `[p.N]` page anchor. `verification_status` is filled in Phase D, not by you.
