"""Citation mapping: first-appearance order, venue-aware formatting."""
from __future__ import annotations
import re

CITE_RE = re.compile(r'\[@([^\]]+)\]')


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


def _format_numbers(nums: list, venue) -> str:
    if not nums:
        return ''
    nums = sorted(set(nums))
    sep = getattr(venue, 'cite_sep', ', ')
    run_min = int(getattr(venue, 'cite_run_min', 3) or 3)
    groups: list = []
    cur = [nums[0]]
    for x in nums[1:]:
        if x == cur[-1] + 1:
            cur.append(x)
        else:
            groups.append(cur)
            cur = [x]
    groups.append(cur)
    parts = []
    for g in groups:
        if len(g) >= run_min:
            parts.append(f'[{g[0]}]-[{g[-1]}]')
        elif len(g) == 2:
            parts.append(f'[{g[0]}]{sep}[{g[1]}]')
        else:
            parts.append(f'[{g[0]}]')
    return sep.join(parts)


def apply(text: str, mapping: dict, venue) -> str:
    style = getattr(venue, 'cite_style', 'bracket_numeric')

    def repl(m):
        inner = m.group(1)
        keys = [p.strip().lstrip('@') for p in re.split(r'[;,\s]+', inner) if p.strip()]
        keys = [k for k in keys if k]
        if not keys:
            return m.group(0)
        if style == 'author_year':
            return '(' + '; '.join(keys) + ')'
        nums = []
        for k in keys:
            if k in mapping:
                nums.append(mapping[k])
            else:
                nums.append(k)
        int_nums = [x for x in nums if isinstance(x, int)]
        str_keys = [x for x in nums if not isinstance(x, int)]
        out = ''
        if int_nums:
            out = _format_numbers(int_nums, venue)
        if str_keys:
            extra = ', '.join(f'[{s}]' for s in str_keys)
            out = (out + getattr(venue, 'cite_sep', ', ') + extra) if out else extra
        return out

    return CITE_RE.sub(repl, text)
