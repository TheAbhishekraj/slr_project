"""Bib handling: keys unchanged, order follows venue, uncited appended."""
from __future__ import annotations
import pathlib
import re

ENTRY_RE = re.compile(r'@(\w+)\s*\{\s*([^,\s]+)\s*,', re.IGNORECASE)


def load_bib(path) -> dict:
    p = pathlib.Path(path)
    if not p.is_file():
        return {}
    text = p.read_text(encoding='utf-8')
    entries: dict = {}
    starts = [m.start() for m in re.finditer(r'(?m)^\s*@', text)]
    if not starts:
        return {}
    starts.append(len(text))
    for i in range(len(starts) - 1):
        chunk = text[starts[i]:starts[i + 1]].strip()
        if not chunk:
            continue
        m = ENTRY_RE.search(chunk)
        if m:
            entries[m.group(2).strip()] = chunk
        else:
            entries[f'__raw_{i}'] = chunk
    return entries


def reorder(entries: dict, citation_map: dict, venue) -> list:
    cited = []
    uncited = []
    for key, raw in entries.items():
        if key.startswith('__raw_'):
            uncited.append((key, raw, False))
        elif citation_map and key in citation_map:
            cited.append((key, raw, True))
        elif not citation_map:
            uncited.append((key, raw, False))
        else:
            uncited.append((key, raw, False))
    cited_sorted = sorted(cited, key=lambda t: citation_map.get(t[0], 10 ** 9))
    return cited_sorted + uncited


def emit(entries, path, venue) -> None:
    p = pathlib.Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    lines = [f'% references for {getattr(venue, "format_id", "generic")}']
    items = []
    if isinstance(entries, dict):
        items = [(k, v, True) for k, v in entries.items()]
    else:
        for it in entries:
            if isinstance(it, (list, tuple)) and len(it) == 3:
                items.append((it[0], it[1], it[2]))
            elif isinstance(it, (list, tuple)) and len(it) == 2:
                items.append((it[0], it[1], True))
    uncited_started = False
    for key, raw, is_cited in items:
        if not is_cited and not uncited_started:
            if any(c for _, _, c in items):
                lines.append('% UNCITED')
            uncited_started = True
        lines.append(raw.strip())
        lines.append('')
    p.write_text('\n'.join(lines).strip() + '\n', encoding='utf-8')
