"""Heading mapping: apply LaTeX sections. Let LaTeX number them."""
from __future__ import annotations
import copy
import re


def _strip_number(t: str) -> str:
    return re.sub(r'^\s*(?:[IVXLC]+|\d+|[A-Z])\.\s+', '', t).strip()


def propose(md_meta, venue) -> list:
    out = []
    for h in md_meta.section_list:
        clean = _strip_number(h)
        out.append((h, clean))
    return out


def apply(blocks, venue):
    nb = copy.deepcopy(blocks)
    for b in nb:
        if b.kind != 'heading':
            continue
        lvl = b.meta.get('level', 1)
        clean = _strip_number(b.text).replace('}', '\\}')
        if lvl == 1:
            b.raw = '\\section{' + clean + '}'
        elif lvl == 2:
            b.raw = '\\subsection{' + clean + '}'
        else:
            b.raw = '\\subsubsection{' + clean + '}'
        b.meta['new_label'] = clean
    return nb
