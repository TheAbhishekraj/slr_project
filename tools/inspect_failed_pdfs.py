import pymupdf
import re

for rec_id in ['REC_1083', 'REC_1084', 'REC_1085', 'REC_1095', 'REC_1096']:
    pdf_path = f"01_data/03_pdfs/{rec_id}.pdf"
    doc = pymupdf.open(pdf_path)
    print("=" * 60)
    print(f"{rec_id}: Total pages = {len(doc)}")
    p1 = doc[0].get_text()
    print("PAGE 1 (first 1000 chars):")
    print(p1[:1000])
    p_last = doc[-1].get_text()
    print("LAST PAGE (first 500 chars):")
    print(p_last[:500])
