"""Citation mapping: emit LaTeX \cite{...}. Let bibtex number."""
from __future__ import annotations
import re

CITE_RE = re.compile(
    r'\[\s*(?:@([^\]]+)|((?:REC_\d{4})(?:\s*[,;]\s*REC_\d{4})*))\s*\]'
)


def build(md_meta, bib_keys_ordered) -> dict:
    ordered = list(getattr(md_meta, 'reference_keys_found', []) or [])
    seen = set(ordered)
    for k in (bib_keys_ordered or []):
        if k not in seen:
            seen.add(k)
            ordered.append(k)
    mapping: dict = {}
    for idx, key in enumerate(ordered, start=1):
        mapping[key] = idx
    return mapping


def apply(text: str, mapping: dict, venue) -> str:
    style = getattr(venue, 'cite_style', 'bracket_numeric')

    def repl(m):
        inner = m.group(1) or m.group(2) or ''
        keys = [p.strip().lstrip('@') for p in re.split(r'[;,\s]+', inner) if p.strip()]
        keys = [k for k in keys if k]
        if not keys:
            return m.group(0)
        if style == 'author_year':
            return '(' + '; '.join(keys) + ')'
        # LaTeX: emit \cite{key1,key2}
        return '\\cite{' + ','.join(keys) + '}'

    return CITE_RE.sub(repl, text)
