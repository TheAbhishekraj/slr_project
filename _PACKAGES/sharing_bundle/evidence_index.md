# Evidence Index: Auditability & Reproducibility

To ensure maximum transparency, this systematic literature review tracks all critical evidence via immutable SHAs and strict version control. Below is the index of primary evidence artifacts required for auditing the methodology.

| Path | SHA256 Hash | Purpose | Verification Steps |
|---|---|---|---|
| `00_scope/SCOPE.md` | `2A649871F2F385AC5482C82BF9CB2E4876ADE3584EC856A58C6212C6A64CF584` | Defines the PRISMA 2020 protocol, exact Boolean search strings, and inclusion/exclusion criteria. | Confirm the criteria strictly match the PRISMA flow diagram (Fig. 1) in the manuscript. |
| `04_master/MASTER_EVIDENCE.csv` | `A2ACA6FA978FB49F4679425AF3254E4E2C45FA1D92F8E7491C1218D161804263` | The central database of all 287 included studies (28 columns of extracted metadata and metrics). | Run `python tools/venue_format.py` or pivot tables to confirm the statistical counts (e.g., 182 Vision studies) match the manuscript precisely. |
| `06_manuscript/source/MANUSCRIPT.md` | `469C11CD017F57349E57EE42F8ED58CDA75682B930004CFE69B18150128C0530` | The primary narrative text of the review, authored in markdown prior to LaTeX compilation. | Execute the freeze check `cli.py` to ensure zero token drift occurred during PDF rendering. |
| `06_manuscript/source/APPENDIX_A.md` | `9F736003F4404E62C4F06AD945A0D3BE5BCB7F992032B92B00966E90086B8F79` | Provides the PRISMA-required list of all 287 included studies, fulfilling Item 17. | Cross-reference REC_IDs against `MASTER_EVIDENCE.csv` to ensure 1:1 mapping (287 rows). |
| `02_cards/REC_*.md` | *(287 individual SHAs)* | Individual markdown extraction cards containing verbatim quotes anchored to each paper. | Select any random `REC_XXXX.md` and trace the verbatim quotes back to the original source PDF. |
| `tools/venue_format/cli.py` | *(Managed via Git)* | Custom Python build script that handles the end-to-end token validation and PDF compilation. | Run `pytest` or execute the script in `--strict` mode to verify build deterministic logic. |

*Note: All hashes correspond to the `v-final-pdf` / `v287-certified` tag in the repository.*
