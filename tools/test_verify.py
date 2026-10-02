import re
import pymupdf

doc = pymupdf.open('01_data/03_pdfs/REC_0001.pdf')
pages_text = {i + 1: ' '.join(doc[i].get_text().split()) for i in range(len(doc))}

with open('02_cards/REC_0001.md', 'r', encoding='utf-8') as f:
    card_text = f.read()

# Pattern for quoted text followed by [p.N]
matches = re.findall(r'\"([^\"]{10,})\"[^\n\[]*\[p\.(\d+)\]', card_text)
print(f"Found {len(matches)} quotes")

for q, p_str in matches:
    p_num = int(p_str)
    q_clean = ' '.join(q.split())
    pdf_clean = pages_text.get(p_num, '')
    if q_clean not in pdf_clean:
        print(f"MISMATCH on p.{p_num}:")
        print("  Quote:", q_clean[:80])
        # Find where it might be
        found = False
        for p_idx, text in pages_text.items():
            if q_clean[:25] in text:
                print(f"  --> Actually found on p.{p_idx}")
                found = True
        if not found:
            print("  --> Not found on any page with first 25 chars")
        print("-" * 50)
    else:
        print(f"MATCH on p.{p_num}: {q_clean[:40]}...")
