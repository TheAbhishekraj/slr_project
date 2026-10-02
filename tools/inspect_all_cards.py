import os
import re

cards = sorted([f for f in os.listdir('02_cards') if f.startswith('REC_') and f.endswith('.md')])
counts = []
quote_pattern = re.compile(r'\"([^\"]{8,})\"[^\n\[]*\[p\.?\s*(\d+)\]', re.DOTALL)

for c in cards:
    with open(os.path.join('02_cards', c), encoding='utf-8') as f:
        txt = f.read()
    m = quote_pattern.findall(txt)
    counts.append(len(m))

print(f"Total cards: {len(cards)}")
print(f"Cards with quotes found: {sum(1 for c in counts if c > 0)}")
print(f"Average quotes per card: {sum(counts)/len(counts):.1f}")
print(f"Min quotes: {min(counts)}, Max quotes: {max(counts)}")
zeros = [cards[i] for i, c in enumerate(counts) if c == 0]
print(f"Cards with 0 quotes found: {zeros}")
