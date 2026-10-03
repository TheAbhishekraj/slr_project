SLR ?= generic

.PHONY: ieee acm lncs elsevier clean formats

ieee:     ; python tools/venue_format.py --repo . --format tools/formats/IEEE.conf     --profile tools/formats/slr_profile.$(SLR).conf --strict --confirm
acm:      ; python tools/venue_format.py --repo . --format tools/formats/ACM.conf      --profile tools/formats/slr_profile.$(SLR).conf --strict --confirm
lncs:     ; python tools/venue_format.py --repo . --format tools/formats/LNCS.conf     --profile tools/formats/slr_profile.$(SLR).conf --strict --confirm
elsevier: ; python tools/venue_format.py --repo . --format tools/formats/ELSEVIER.conf --profile tools/formats/slr_profile.$(SLR).conf --strict --confirm
clean:    ; rm -rf 06_manuscript/ieee 06_manuscript/acm 06_manuscript/lncs 06_manuscript/elsevier
formats:  ; @ls -1 tools/formats/
