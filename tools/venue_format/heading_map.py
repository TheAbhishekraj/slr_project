"""Heading mapping: propose labels, apply LaTeX sections without reordering."""
from __future__ import annotations
import copy


def _roman(n: int) -> str:
    vals = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    out = ''
    for v, s in vals:
        while n >= v:
            out += s
            n -= v
    return out or 'I'


def _alpha(n: int) -> str:
    s = ''
    while n > 0:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s or 'A'


def _fmt_num(n: int, style: str) -> str:
    st = (style or '').lower()
    if st == 'roman':
        return _roman(n)
    if st == 'alpha':
        return _alpha(n)
    if st == 'arabic_paren':
        return f'({n})'
    if st == 'arabic':
        return str(n)
    if st in ('none', ''):
        return ''
    return str(n)


def propose(md_meta, venue) -> list:
    out = []
    c1 = 0
    for h in md_meta.section_list:
        c1 += 1
        lbl = _fmt_num(c1, getattr(venue, 'h1_number', 'Roman'))
        out.append((h, f'{lbl} {h}' if lbl else h))
    return out


def apply(blocks, venue):
    nb = copy.deepcopy(blocks)
    c1 = c2 = c3 = 0
    for b in nb:
        if b.kind != 'heading':
            continue
        lvl = b.meta.get('level', 1)
        if lvl == 1:
            c1 += 1
            c2 = 0
            c3 = 0
            num = _fmt_num(c1, getattr(venue, 'h1_number', 'Roman'))
            label = f'{num} {b.text}' if num else b.text
            b.raw = '\\section*{' + label.replace('}', '\\}') + '}'
            b.meta['new_label'] = label
        elif lvl == 2:
            c2 += 1
            c3 = 0
            num = _fmt_num(c2, getattr(venue, 'h2_number', 'Alpha'))
            label = f'{num} {b.text}' if num else b.text
            b.raw = '\\subsection*{' + label.replace('}', '\\}') + '}'
            b.meta['new_label'] = label
        else:
            c3 += 1
            num = _fmt_num(c3, getattr(venue, 'h3_number', 'arabic_paren'))
            label = f'{num} {b.text}' if num else b.text
            b.raw = '\\subsubsection*{' + label.replace('}', '\\}') + '}'
            b.meta['new_label'] = label
    return nb
