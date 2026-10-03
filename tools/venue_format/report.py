"""Format report: markdown table of changes per file."""
from __future__ import annotations


def build(plan, applied, drift, venue, profile) -> str:
    L = []
    L.append('# FORMAT_REPORT')
    L.append('')
    L.append(f'- venue: {getattr(venue, "format_id", "")} ({getattr(venue, "display_name", "")})')
    L.append(f'- profile: {getattr(profile, "slr_name", "")} style={getattr(profile, "output_style", "")}')
    L.append(f'- drift: {drift}')
    L.append('')
    L.append('| file | change type | before | after | rule |')
    L.append('| --- | --- | --- | --- | --- |')
    rows = applied if applied else plan
    if not rows:
        L.append('| main.tex | none | - | - | R3 |')
    else:
        for r in rows:
            if isinstance(r, (list, tuple)) and len(r) == 5:
                f, c, b, a, rule = r
            elif isinstance(r, dict):
                f = r.get('file', '')
                c = r.get('change', '')
                b = r.get('before', '')
                a = r.get('after', '')
                rule = r.get('rule', '')
            else:
                continue
            L.append(f'| {f} | {c} | {b} | {a} | {rule} |')
    L.append('')
    return '\n'.join(L) + '\n'
