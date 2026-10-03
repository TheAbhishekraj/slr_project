"""Parse manuscript markdown. Preserves raw."""
from __future__ import annotations
import pathlib
import re
from dataclasses import dataclass, field


@dataclass
class Block:
    kind: str
    raw: str
    text: str
    line_no: int
    meta: dict = field(default_factory=dict)


@dataclass
class Metadata:
    title: str = 'NOT_REPORTED'
    authors_as_found: str = 'NOT_REPORTED'
    abstract: str = 'NOT_REPORTED'
    keywords_as_found: str = 'NOT_REPORTED'
    section_list: list = field(default_factory=list)
    rec_ids_found: list = field(default_factory=list)
    numeral_tokens_found: list = field(default_factory=list)
    reference_keys_found: list = field(default_factory=list)


REC_RE = re.compile(r'REC_\d{4}')
NUM_RE = re.compile(r'\d+(?:\.\d+)?%?')
CITE_RE = re.compile(r'\[\s*(?:@([^\]]+)|((?:REC_\d{4})(?:\s*[,;]\s*REC_\d{4})*))\s*\]')
HEADING_RE = re.compile(r'^(#{1,6})\s*(.*)$')
FIG_RE = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
FOOT_RE = re.compile(r'^\[\^[^\]]+\]:?.*')
LIST_RE = re.compile(r'^\s*(?:[-*+]\s+|\d+\.\s+).+')
TABLE_SEP_RE = re.compile(r'^\s*\|?[\s:\-|]+\|?\s*$')
TABLE_SEP_RE = re.compile(r'^\s*\|?[\s:\-|]+\|?\s*$')


def parse_markdown(path) -> tuple:
    p = pathlib.Path(path)
    text = p.read_text(encoding='utf-8')
    lines = text.splitlines()
    blocks: list = []
    meta = Metadata()
    in_fence = False
    fence_buf: list = []
    fence_start = 0
    i = 0
    n = len(lines)
    while i < n:
        ln = lines[i]
        no = i + 1
        if ln.strip().startswith('```'):
            if not in_fence:
                in_fence = True
                fence_start = no
                fence_buf = [ln]
            else:
                fence_buf.append(ln)
                raw = '\n'.join(fence_buf)
                blocks.append(Block(kind='code_fence', raw=raw, text=raw, line_no=fence_start, meta={}))
                in_fence = False
                fence_buf = []
            i += 1
            continue
        if in_fence:
            fence_buf.append(ln)
            i += 1
            continue
        if ln.strip() == '':
            blocks.append(Block(kind='blank', raw=ln, text='', line_no=no, meta={}))
            i += 1
            continue
        m = HEADING_RE.match(ln)
        if m:
            level = len(m.group(1))
            htext = m.group(2).strip()
            blocks.append(Block(kind='heading', raw=ln, text=htext, line_no=no, meta={'level': level}))
            meta.section_list.append(htext)
            i += 1
            continue
        if FOOT_RE.match(ln.strip()):
            blocks.append(Block(kind='footnote', raw=ln, text=ln.strip(), line_no=no, meta={}))
            i += 1
            continue
        if '|' in ln:
            if i + 1 < n and TABLE_SEP_RE.match(lines[i + 1]):
                tbl_lines = [ln, lines[i + 1]]
                j = i + 2
                while j < n and '|' in lines[j] and lines[j].strip() != '':
                    tbl_lines.append(lines[j])
                    j += 1
                raw = '\n'.join(tbl_lines)
                blocks.append(Block(kind='table', raw=raw, text=raw, line_no=no, meta={'rows': list(tbl_lines), 'row_count': len(tbl_lines)}))
                i = j
                continue
        fm = FIG_RE.search(ln)
        if fm and ln.strip().startswith('!['):
            cap = fm.group(1).strip()
            srcp = fm.group(2).strip()
            blocks.append(Block(kind='figure', raw=ln, text=cap, line_no=no, meta={'src': srcp, 'caption': cap}))
            i += 1
            continue
        s = ln.strip()
        if s.startswith('$$') or s.startswith('\\[') or s.startswith('\\begin{equation'):
            eq_lines = [ln]
            j = i + 1
            if not (s.endswith('$$') and len(s) > 2):
                while j < n:
                    if lines[j].strip().endswith('$$') or lines[j].strip().startswith('\\]') or 'end{equation' in lines[j]:
                        break
                    eq_lines.append(lines[j])
                    j += 1
                if j < n:
                    eq_lines.append(lines[j])
                    j += 1
            else:
                j = i + 1
            blocks.append(Block(kind='equation', raw='\n'.join(eq_lines), text='\n'.join(eq_lines), line_no=no, meta={}))
            i = j
            continue
        if LIST_RE.match(ln):
            blocks.append(Block(kind='list_item', raw=ln, text=ln.strip(), line_no=no, meta={}))
            i += 1
            continue
        blocks.append(Block(kind='paragraph', raw=ln, text=ln, line_no=no, meta={}))
        i += 1
    full = text
    for b in blocks:
        if b.kind == 'heading' and b.meta.get('level') == 1:
            meta.title = b.text if b.text else 'NOT_REPORTED'
            break
    abs_text = []
    in_abs = False
    for b in blocks:
        if b.kind == 'heading' and 'abstract' in b.text.lower():
            in_abs = True
            continue
        if in_abs:
            if b.kind == 'heading':
                break
            if b.kind in ('paragraph', 'list_item'):
                abs_text.append(b.text)
    if abs_text:
        meta.abstract = ' '.join(abs_text).strip()[:4000]
    # keywords — accept heading OR paragraph that starts with **Keywords:**
    for idx, b in enumerate(blocks):
        if b.kind == 'heading' and 'keyword' in b.text.lower():
            for nb in blocks[idx + 1:]:
                if nb.kind in ('paragraph', 'list_item'):
                    meta.keywords_as_found = nb.text.strip()
                    break
                if nb.kind == 'heading':
                    break
            break
    if meta.keywords_as_found == 'NOT_REPORTED':
        for b in blocks:
            if b.kind not in ('paragraph', 'list_item'):
                continue
            clean = re.sub(r'^\*+\s*', '', b.raw.strip())
            if clean.lower().startswith('keywords:'):
                meta.keywords_as_found = clean.split(':', 1)[1].strip().strip('*').strip()
                break
    for b in blocks:
        if b.kind not in ('paragraph', 'list_item'):
            continue
        raw = b.raw.strip()
        # strip leading ** and possible spaces
        clean = re.sub(r'^\*+\s*', '', raw)
        low = clean.lower()
        if low.startswith('author:'):
            meta.authors_as_found = clean.split(':', 1)[1].strip().strip('*').strip()
            break
    seen = set()
    recs = []
    for mrec in REC_RE.finditer(full):
        tok = mrec.group(0)
        if tok not in seen:
            seen.add(tok)
            recs.append(tok)
    meta.rec_ids_found = recs
    meta.numeral_tokens_found = NUM_RE.findall(full)
    rseen = set()
    rkeys = []
    for cmt in CITE_RE.finditer(full):
        inner = cmt.group(1) or cmt.group(2) or ''
        for part in re.split(r'[;,\s]+', inner):
            k = part.strip().lstrip('@')
            if k and k not in rseen:
                rseen.add(k)
                rkeys.append(k)
    meta.reference_keys_found = rkeys
    return blocks, meta

