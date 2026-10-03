"""Preservation trace. Raises ContentDrift on mismatch."""
from __future__ import annotations
import pathlib


class ContentDrift(Exception):
    pass


def build(repo, out, src_hashes, emitted_hashes, venue, profile, pre_meta, post_meta) -> str:
    generic = (getattr(profile, 'output_style', 'generic') or 'generic').lower() == 'generic'
    L = []
    L.append('# TRACE_PRESERVATION')
    L.append('')
    L.append('## Venue card')
    for k in sorted(vars(venue).keys()):
        L.append(f'- {k} = {getattr(venue, k)}')
    L.append('')
    L.append('## Profile card')
    for k in sorted(vars(profile).keys()):
        L.append(f'- {k} = {getattr(profile, k)}')
    L.append('')
    L.append('## Source hashes (path, sha256, bytes)')
    for k in sorted(src_hashes.keys()):
        try:
            nbytes = pathlib.Path(k).stat().st_size
        except Exception:
            nbytes = -1
        L.append(f'- {k} {src_hashes[k]} {nbytes}')
    L.append('')
    L.append('## Emitted hashes (path, sha256, bytes)')
    for k in sorted(emitted_hashes.keys()):
        try:
            nbytes = pathlib.Path(k).stat().st_size
        except Exception:
            nbytes = -1
        L.append(f'- {k} {emitted_hashes[k]} {nbytes}')
    L.append('')
    pre_recs = list(getattr(pre_meta, 'rec_ids_found', []) or [])
    post_recs = list(getattr(post_meta, 'rec_ids_found', []) or [])
    pre_nums = list(getattr(pre_meta, 'numeral_tokens_found', []) or [])
    post_nums = list(getattr(post_meta, 'numeral_tokens_found', []) or [])
    pre_keys = list(getattr(pre_meta, 'reference_keys_found', []) or [])
    post_keys = list(getattr(post_meta, 'reference_keys_found', []) or [])
    if not generic:
        L.append('## REC IDs — before/after')
        L.append(f'- before: {", ".join(pre_recs) if pre_recs else "none"}')
        L.append(f'- after: {", ".join(post_recs) if post_recs else "none"}')
        L.append('')
        if pre_recs != post_recs:
            raise ContentDrift(f'REC IDs changed: {pre_recs} vs {post_recs}')
    else:
        L.append('## REC IDs — before/after (skipped: generic profile)')
        L.append('')
    L.append('## Numerals — before/after')
    L.append(f'- before: {", ".join(pre_nums) if pre_nums else "none"}')
    L.append(f'- after: {", ".join(post_nums) if post_nums else "none"}')
    L.append('')
    if sorted(pre_nums) != sorted(post_nums):
        raise ContentDrift(f'numerals changed: {pre_nums} vs {post_nums}')
    L.append('## Reference keys — before/after')
    L.append(f'- before: {", ".join(pre_keys) if pre_keys else "none"}')
    L.append(f'- after: {", ".join(post_keys) if post_keys else "none"}')
    L.append('')
    if set(pre_keys) != set(post_keys):
        raise ContentDrift(f'reference keys changed: {pre_keys} vs {post_keys}')
    if not generic and getattr(profile, 'prisma_chain', []):
        L.append('## PRISMA chain check')
        chain = list(getattr(profile, 'prisma_chain', []))
        L.append(f'- chain: {", ".join(chain)}')
        flat = ' '.join(pre_nums)
        missing = [c for c in chain if c not in pre_nums and c not in flat]
        L.append(f'- missing: {", ".join(missing) if missing else "none"}')
        L.append('')
    else:
        L.append('## PRISMA chain check (skipped)')
        L.append('')
    if not generic and getattr(profile, 'excluded_ids', []):
        L.append('## Excluded IDs present as included? — must be NO')
        excl = set(getattr(profile, 'excluded_ids', []))
        present = sorted(set(pre_recs) & excl)
        L.append(f'- excluded: {", ".join(sorted(excl))}')
        L.append(f'- present-as-included: {", ".join(present) if present else "NO"}')
        L.append('')
        if present:
            raise ContentDrift(f'excluded IDs present as included: {present}')
    else:
        L.append('## Excluded IDs present as included? (skipped)')
        L.append('')
    return '\n'.join(L) + '\n'
