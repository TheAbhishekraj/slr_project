import sys
import os
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')

def dump_paper_info(rec_id):
    pdf_path = f"01_data/03_pdfs/{rec_id}.pdf"
    doc = pymupdf.open(pdf_path)
    print(f"=== {rec_id} (Pages: {len(doc)}) ===")
    for p_num in range(min(5, len(doc))):
        print(f"--- Page {p_num + 1} ---")
        lines = [line.strip() for line in doc[p_num].get_text().splitlines() if line.strip()]
        print("\n".join(lines[:35]))
    print(f"--- Last Page {len(doc)} ---")
    lines = [line.strip() for line in doc[-1].get_text().splitlines() if line.strip()]
    print("\n".join(lines[:35]))

for r in ['REC_1083', 'REC_1084', 'REC_1085', 'REC_1095', 'REC_1096']:
    dump_paper_info(r)
