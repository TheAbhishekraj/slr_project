"""Load venue and profile cards. INI-like key = value, # comments, trailing-comma continuation."""
from __future__ import annotations
import pathlib
from dataclasses import dataclass, field


def _parse_conf(path) -> dict:
    text = pathlib.Path(path).read_text(encoding='utf-8')
    raw_lines = text.splitlines()
    joined: list[str] = []
    buf = ''
    for ln in raw_lines:
        s = ln.strip()
        if not s or s.startswith('#') or s.startswith(';'):
            continue
        if ' #' in ln:
            ln = ln[:ln.index(' #')]
            s = ln.strip()
        if buf:
            buf = buf + ' ' + s
        else:
            buf = s
        if buf.rstrip().endswith(','):
            continue
        else:
            joined.append(buf)
            buf = ''
    if buf:
        joined.append(buf)
    d: dict = {}
    for line in joined:
        if '=' not in line:
            continue
        k, v = line.split('=', 1)
        k = k.strip()
        v = v.strip()
        if len(v) >= 2 and ((v[0] == '"' and v[-1] == '"') or (v[0] == "'" and v[-1] == "'")):
            v = v[1:-1]
        d[k] = v
    return d


def _split_list(v: str) -> list:
    if v is None or str(v).strip() == '':
        return []
    parts = [p.strip() for p in str(v).split(',')]
    return [p for p in parts if p != '']


def _to_int(v, default: int) -> int:
    try:
        return int(str(v).strip())
    except Exception:
        return default


def _to_bool(v, default: bool) -> bool:
    if isinstance(v, bool):
        return v
    s = str(v).strip().lower()
    if s in ('true', 'yes', '1', 'on'):
        return True
    if s in ('false', 'no', '0', 'off'):
        return False
    return default


@dataclass
class VenueCard:
    format_id: str = 'ieee'
    display_name: str = 'IEEEtran conference'
    template_class: str = 'IEEEtran'
    template_opt: str = 'conference'
    compile_engine: str = 'pdflatex'
    bib_engine: str = 'bibtex'
    bib_style: str = 'IEEEtran'
    paper: str = 'letter'
    margins_in: str = '0.75 0.75 0.75 0.75'
    columns: int = 2
    gutter_in: str = '0.25'
    body_font_pt: int = 10
    body_font_fam: str = 'times'
    title_pt: int = 24
    title_case: str = 'title'
    author_pt: int = 11
    abstract_pt: int = 9
    abstract_style: str = 'bold_italic'
    abstract_words: str = '150-250'
    keywords_pt: int = 9
    keywords_style: str = 'bold_italic'
    keywords_max: int = 6
    keywords_order: str = 'alphabetical'
    h1_style: str = 'small_caps_centered'
    h1_number: str = 'Roman'
    h2_style: str = 'italic_left'
    h2_number: str = 'Alpha'
    h3_style: str = 'italic_runin'
    h3_number: str = 'arabic_paren'
    fig_caption_pos: str = 'below'
    fig_caption_pt: int = 8
    fig_label_fmt: str = 'Fig. {n}.'
    tbl_caption_pos: str = 'above'
    tbl_caption_pt: int = 8
    tbl_caption_sc: bool = True
    tbl_label_fmt: str = 'TABLE {ROMAN}.'
    eq_number_align: str = 'right'
    eq_number_fmt: str = '({n})'
    cite_style: str = 'bracket_numeric'
    cite_run_min: int = 3
    cite_sep: str = ', '
    ref_pt: int = 8
    ref_indent: str = 'hanging'
    page_numbers: bool = False
    headers: bool = False
    footers: bool = False


@dataclass
class ProfileCard:
    slr_name: str = 'generic'
    output_style: str = 'generic'
    rec_id_pattern: str = r'^REC_\d{4}$'
    prisma_chain: list = field(default_factory=list)
    excluded_ids: list = field(default_factory=list)
    locked_numbers: str = ''
    evidence_csv: str = ''
    manifest_glob: str = ''
    number_trace: str = ''
    manuscript_md: str = '06_manuscript/MANUSCRIPT.md'
    references_bib: str = '06_manuscript/references.bib'
    banned_words: list = field(default_factory=list)
    banned_openers: list = field(default_factory=list)


def load_venue(path) -> VenueCard:
    d = _parse_conf(path)
    g = lambda k, dv: d.get(k, dv)
    return VenueCard(
        format_id=g('format_id', 'ieee'),
        display_name=g('display_name', 'IEEEtran conference'),
        template_class=g('template_class', 'IEEEtran'),
        template_opt=g('template_opt', 'conference'),
        compile_engine=g('compile_engine', 'pdflatex'),
        bib_engine=g('bib_engine', 'bibtex'),
        bib_style=g('bib_style', 'IEEEtran'),
        paper=g('paper', 'letter'),
        margins_in=g('margins_in', '0.75 0.75 0.75 0.75'),
        columns=_to_int(g('columns', '2'), 2),
        gutter_in=g('gutter_in', '0.25'),
        body_font_pt=_to_int(g('body_font_pt', '10'), 10),
        body_font_fam=g('body_font_fam', 'times'),
        title_pt=_to_int(g('title_pt', '24'), 24),
        title_case=g('title_case', 'title'),
        author_pt=_to_int(g('author_pt', '11'), 11),
        abstract_pt=_to_int(g('abstract_pt', '9'), 9),
        abstract_style=g('abstract_style', 'bold_italic'),
        abstract_words=g('abstract_words', '150-250'),
        keywords_pt=_to_int(g('keywords_pt', '9'), 9),
        keywords_style=g('keywords_style', 'bold_italic'),
        keywords_max=_to_int(g('keywords_max', '6'), 6),
        keywords_order=g('keywords_order', 'alphabetical'),
        h1_style=g('h1_style', 'small_caps_centered'),
        h1_number=g('h1_number', 'Roman'),
        h2_style=g('h2_style', 'italic_left'),
        h2_number=g('h2_number', 'Alpha'),
        h3_style=g('h3_style', 'italic_runin'),
        h3_number=g('h3_number', 'arabic_paren'),
        fig_caption_pos=g('fig_caption_pos', 'below'),
        fig_caption_pt=_to_int(g('fig_caption_pt', '8'), 8),
        fig_label_fmt=g('fig_label_fmt', 'Fig. {n}.'),
        tbl_caption_pos=g('tbl_caption_pos', 'above'),
        tbl_caption_pt=_to_int(g('tbl_caption_pt', '8'), 8),
        tbl_caption_sc=_to_bool(g('tbl_caption_sc', 'true'), True),
        tbl_label_fmt=g('tbl_label_fmt', 'TABLE {ROMAN}.'),
        eq_number_align=g('eq_number_align', 'right'),
        eq_number_fmt=g('eq_number_fmt', '({n})'),
        cite_style=g('cite_style', 'bracket_numeric'),
        cite_run_min=_to_int(g('cite_run_min', '3'), 3),
        cite_sep=g('cite_sep', ', '),
        ref_pt=_to_int(g('ref_pt', '8'), 8),
        ref_indent=g('ref_indent', 'hanging'),
        page_numbers=_to_bool(g('page_numbers', 'false'), False),
        headers=_to_bool(g('headers', 'false'), False),
        footers=_to_bool(g('footers', 'false'), False),
    )


def load_profile(path) -> ProfileCard:
    d = _parse_conf(path)
    g = lambda k, dv: d.get(k, dv)
    return ProfileCard(
        slr_name=g('slr_name', 'generic'),
        output_style=g('output_style', 'generic').strip().lower(),
        rec_id_pattern=g('rec_id_pattern', r'^REC_\d{4}$'),
        prisma_chain=_split_list(g('prisma_chain', '')),
        excluded_ids=_split_list(g('excluded_ids', '')),
        locked_numbers=g('locked_numbers', ''),
        evidence_csv=g('evidence_csv', ''),
        manifest_glob=g('manifest_glob', ''),
        number_trace=g('number_trace', ''),
        manuscript_md=g('manuscript_md', '06_manuscript/MANUSCRIPT.md'),
        references_bib=g('references_bib', '06_manuscript/references.bib'),
        banned_words=_split_list(g('banned_words', '')),
        banned_openers=_split_list(g('banned_openers', '')),
    )

