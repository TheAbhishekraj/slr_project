# MANUSCRIPT

## Subfolders

- `source/` — Markdown source files (MANUSCRIPT.md, references.bib, etc.)
- `ieee/` — LaTeX output from tools/venue_format.py
- `presentation/` — supervisor slide deck source

## Build LaTeX

    cd E:\slr_project
    python tools\venue_format.py `
      --repo . `
      --format tools\formats\IEEE.conf `
      --profile tools\formats\slr_profile.generic.conf `
      --strict --confirm

Output: `06_manuscript/ieee/manuscript_ieee.tex` and `.pdf`

## Rebuild the packages

    cd E:\slr_project
    Copy-Item 06_manuscript\ieee\manuscript_ieee.pdf _PACKAGES\submission\ -Force
    Copy-Item 06_manuscript\ieee\manuscript_ieee.tex _PACKAGES\submission\ -Force
    Copy-Item 06_manuscript\ieee\references_ieee.bib _PACKAGES\submission\ -Force
