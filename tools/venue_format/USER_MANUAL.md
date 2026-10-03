# Venue Formatter — Requirements + User Manual v1.0.0
Tool: tools/venue_format/ | Run: tools/venue_format.py
Python 3.10+ | stdlib only | Windows/Linux OK

## 1. WHAT IT DOES
Reformats MANUSCRIPT.md + references.bib into any venue style
(IEEE/ACM/LNCS/Elsevier/custom). Layout only. Sources READ-ONLY.
All outputs go to 06_manuscript/<format_id>/.
Same tool: this SLR, future SLRs (new profile card), non-SLR (generic).

## 2. REQUIREMENTS
- Python 3.10+: python --version
- No pip installs. Optional pdflatex/latexmk/bibtex for PDF.
  Without LaTeX: .tex still written, exit 3 (soft).
- Repo files expected (slr mode):
  00_scope/LOCKED_NUMBERS.md, 06_manuscript/MANUSCRIPT.md,
  06_manuscript/references.bib, 06_manuscript/NUMBER_TRACE.md,
  04_master/MASTER_EVIDENCE.csv, 02_cards/FROZEN_MANIFEST_*.csv
- Generic mode: ONLY manuscript_md required.

## 3. TOOL FILES (21)
venue_format/: __init__ sha card read_manuscript heading_map
citation_map refs_convert floats latex_emit compile_pdf trace
report cli  +  tools/venue_format.py  +  tools/Makefile
+ formats: IEEE ACM LNCS ELSEVIER slr_profile.template
slr_profile.generic + slr_profile.gps_denied_uav (this SLR).

## 4. CLI (frozen)
python tools/venue_format.py --repo . --format <venue.conf>
  --profile <profile.conf> --out <dir> --strict --dry-run
  --phase {0..7} --confirm --no-pdf --verbose
--confirm REQUIRED to write. Exits: 0 clean, 1 drift,
2 usage, 3 latex-missing.
Phases: 0 inventory, 1 headings, 2 cites, 3 bib, 4 floats,
5 emit tex, 6 compile, 7 trace+report.
## 5. INPUT — WHAT YOU PROVIDE (files, not chat text)
Do NOT paste manuscript prose in chat. Keep files in repo.

THIS SLR (profile slr_profile.gps_denied_uav.conf):
1. 06_manuscript/MANUSCRIPT.md (REQUIRED — body copied byte-for-byte)
2. 06_manuscript/references.bib (REQUIRED — keys never changed)
3. 00_scope/LOCKED_NUMBERS.md (slr mode — path must exist)
4. 04_master/MASTER_EVIDENCE.csv (slr mode — must exist)
5. 02_cards/FROZEN_MANIFEST_*.csv (glob must match)
6. 06_manuscript/NUMBER_TRACE.md (slr mode — must exist)
7. 05_analysis/figures/* optional — copied to out/FIGURES/ unchanged.
Profile: slr_name=gps_denied_uav, output_style=slr,
prisma=2000,1716,501,291,287, excluded_ids empty (your 4 IDs
are audit-only prose mentions), manuscript+bib paths as above,
banned words/openers per card.

FUTURE SLR: copy slr_profile.template.conf to
slr_profile.<new>.conf, edit 6 marked lines
(name, prisma, excluded, locked/evidence/manifest/trace paths,
manuscript+bib), place its files, run with --profile <new>.

NON-SLR: use slr_profile.generic.conf (output_style=generic,
audit fields empty). Only freeze-and-diff runs.

AUTHOR RULES: cites as [@key]/[@k1;@k2]; [REC_x] = audit IDs
not bib cites; pipe tables need | --- | row; images as
![cap](path) alone; never [UNTRACEABLE]; missing=NOT_REPORTED;
American spelling.
## 6. OUTPUT — WHAT THE TOOL WRITES (only inside --out)
Default out = 06_manuscript/<format_id>/. Nothing outside --out.
main.tex          spacing/layout only, body bytes preserved (R3)
references_<id>.bib  ref-order only; keys/fields unchanged;
                  uncited appended under "% UNCITED" (R5)
TRACE_PRESERVATION.md  venue card, profile card, source hashes,
                  emitted hashes, REC before/after, numerals
                  before/after, ref keys before/after, PRISMA
                  chain check, excluded-ID check (R2)
FORMAT_REPORT.md  table: file / change type / before / after / rule
compile.log + main.pdf  only if LaTeX present (else log notes missing)
FIGURES/ TABLES/  copied without renaming (only if repo has them)
phase files: heading_map.txt (P1), citation_map.txt (P2),
             float_map.txt (P4)

## 7. HOW TO RUN (from E:/slr_project root)
Dry run (no writes):
  python tools/venue_format.py --repo . --format tools/formats/IEEE.conf --profile tools/formats/slr_profile.gps_denied_uav.conf --dry-run
This SLR in IEEE (full, no PDF):
  python tools/venue_format.py --repo . --format tools/formats/IEEE.conf --profile tools/formats/slr_profile.gps_denied_uav.conf --confirm --no-pdf
Future SLR in ACM:
  python tools/venue_format.py --repo . --format tools/formats/ACM.conf --profile tools/formats/slr_profile.<newname>.conf --strict --confirm
Non-SLR paper in LNCS:
  python tools/venue_format.py --repo . --format tools/formats/LNCS.conf --profile tools/formats/slr_profile.generic.conf --confirm --no-pdf
Make (SLR=gps_denied_uav for this project):
  make -f tools/Makefile ieee SLR=gps_denied_uav
  (acm / lncs / elsevier same pattern; Windows: use python lines)
Expected tree (one IEEE run):
  06_manuscript/ieee/main.tex
  06_manuscript/ieee/references_ieee.bib
  06_manuscript/ieee/TRACE_PRESERVATION.md
  06_manuscript/ieee/FORMAT_REPORT.md
  06_manuscript/ieee/compile.log (+ main.pdf if LaTeX)
  06_manuscript/ieee/FIGURES/ (when repo has figures)
## 8. ADDING A NEW SLR — 3 STEPS
1. copy tools\formats\slr_profile.template.conf
   to tools\formats\slr_profile.myslr.conf
2. Edit 6 lines (marked EDIT 1/6..6/6): slr_name, prisma_chain,
   excluded_ids, locked/evidence/manifest/trace paths,
   manuscript_md + references_bib.
3. Run:
   python tools/venue_format.py --repo . --format tools/formats/IEEE.conf --profile tools/formats/slr_profile.myslr.conf --strict --confirm

## 9. STOP CONDITIONS (ContentDrift -> exit 1)
ALWAYS (both modes): body sentence differs | numeral changed |
table row count differs | [UNTRACEABLE] introduced | source SHA
changed mid-build | caption reworded | ref key changed or dropped.
SLR-ONLY: REC ID missing/added/renumbered | excluded ID as
included | banned word introduced | banned opener at paragraph
start.

## 10. PASTING DATA + GETTING OUTPUT (the workflow you asked about)
Step A: you write FILES into the repo at the Section 5 paths
(or tell me the paths where your new files live, and I copy them
into place — that is a write into your repo, so I ask first).
Step B: you tell me which venue + which profile card to use.
Step C: I run the Section 7 command and hand you back the
output tree: main.tex, references_<id>.bib,
TRACE_PRESERVATION.md, FORMAT_REPORT.md (+ compile.log/pdf).
If exit=1, I return the DRIFT token diff lines so you can see
exactly which token set differs.
You never paste manuscript bodies into chat as the input mechanism
— files are the input contract.

## 11. KNOWN STATUS (E:/slr_project, 2026-10-03)
- Tool wired: YES. Test project E:/PJ green on all 4 venues.
- This repo: --phase 5 emits main.tex + bib for the real 45KB
  manuscript. Full run DRIFTs on the freeze check: tables
  **Total**, (Fig. 2-8), [REC_xxxx] brackets, and heading
  numbers 1./3.x/4.x vs venue A/B/(1) tokenize asymmetrically.
  Fix = symmetric freeze canonizer in cli.py. Stray file
  tools/venue_format/tok_patch.txt already DELETED.
- Source files untouched by all runs so far.



