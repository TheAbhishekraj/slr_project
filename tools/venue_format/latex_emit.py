"""Emit full LaTeX document. No content bytes changed."""
from __future__ import annotations
import re

from . import citation_map as cm
from . import floats as fl


def _title_case(s: str, mode: str) -> str:
    if mode == 'upper':
        return s.upper()
    if mode == 'sentence':
        return s[:1].upper() + s[1:] if s else s
    return s


def _is_ieee(tcls: str) -> bool:
    return tcls.strip().lower() == 'ieeetran'


def build(blocks, meta, maps, venue, profile) -> str:
    mapping = maps.get('citation', {}) if isinstance(maps, dict) else {}
    paper = getattr(venue, 'paper', 'letter')
    fontpt = int(getattr(venue, 'body_font_pt', 10) or 10)
    fam = getattr(venue, 'body_font_fam', 'times')
    fam_pkg = 'mathptmx' if fam == 'times' else 'lmodern'
    tcls = getattr(venue, 'template_class', 'article')
    docopt = getattr(venue, 'template_opt', '') or ''

    title = _title_case(
        getattr(meta, 'title', 'NOT_REPORTED') or 'NOT_REPORTED',
        getattr(venue, 'title_case', 'title'))
    authors = getattr(meta, 'authors_as_found', 'NOT_REPORTED') or 'NOT_REPORTED'
    abstract = getattr(meta, 'abstract', 'NOT_REPORTED') or 'NOT_REPORTED'
    keywords = getattr(meta, 'keywords_as_found', 'NOT_REPORTED') or 'NOT_REPORTED'
    if keywords != 'NOT_REPORTED':
        parts = [k.strip() for k in keywords.replace(';', ',').split(',') if k.strip()]
        if getattr(venue, 'keywords_order', '') == 'alphabetical':
            parts = sorted(parts, key=str.lower)
        kmax = int(getattr(venue, 'keywords_max', 6) or 6)
        keywords = ', '.join(parts[:kmax]) if parts else 'NOT_REPORTED'

    L = []
    if _is_ieee(tcls):
        L.append('\\documentclass[conference]{IEEEtran}')
    else:
        L.append(f'\\documentclass[{fontpt}pt,{paper}]{{{tcls or "article"}}}')
    L.append(f'% venue: {getattr(venue, "format_id", "")} {getattr(venue, "display_name", "")}')
    L.append('\\usepackage{graphicx}')
    L.append('\\usepackage{amsmath}')
    L.append('\\usepackage{url}')
    L.append('\\usepackage{booktabs}')
    L.append('\\usepackage{array}')
    if not _is_ieee(tcls):
        L.append(f'\\usepackage[{paper}paper]{{geometry}}')
        L.append(f'\\usepackage{{{fam_pkg}}}')
    if not bool(getattr(venue, 'page_numbers', False)):
        L.append('\\pagestyle{empty}')
    L.append('')
    L.append('\\begin{document}')
    L.append('')

    if _is_ieee(tcls):
        L.append('\\title{' + fl.tex_escape(title) + '}')
        L.append('\\author{' + fl.tex_escape(authors) + '}')
        L.append('\\maketitle')
        L.append('')
        L.append('\\begin{abstract}')
        L.append(fl.tex_escape(abstract))
        L.append('\\end{abstract}')
        L.append('')
        if keywords != 'NOT_REPORTED':
            L.append('\\begin{IEEEkeywords}')
            L.append(fl.tex_escape(keywords))
            L.append('\\end{IEEEkeywords}')
            L.append('')
    else:
        L.append(f'{{\\fontsize{{{getattr(venue, "title_pt", 24)}pt}}{{1.2em}}\\selectfont {fl.tex_escape(title)}}}')
        L.append('')
        L.append(f'{{\\fontsize{{{getattr(venue, "author_pt", 11)}pt}}{{1.2em}}\\selectfont {fl.tex_escape(authors)}}}')
        L.append('')
        L.append(f'{{\\fontsize{{{getattr(venue, "abstract_pt", 9)}pt}}{{1.2em}}\\selectfont \\textbf{{\\textit{{Abstract---{fl.tex_escape(abstract)}}}}} }}')
        L.append('')
        L.append(f'{{\\fontsize{{{getattr(venue, "keywords_pt", 9)}pt}}{{1.2em}}\\selectfont \\textbf{{\\textit{{Keywords---{fl.tex_escape(keywords)}}}}} }}')
        L.append('')

    L.append('%FRONTMATTER-END')
    L.append('')

    n_fig = 0
    fig_caps, tab_caps, consumed = fl.pair_float_captions(blocks)
    skip_section = None  # None | 'abstract' | 'keywords'

    for b in blocks:
        if id(b) in consumed:
            continue
        if b.kind == 'heading':
            low = b.text.lower()
            if 'abstract' in low:
                skip_section = 'abstract'
                continue
            if 'keyword' in low:
                skip_section = 'keywords'
                continue
            if 'reference' in low:
                skip_section = 'references'
                continue
            skip_section = None
            if b.meta.get('level', 1) == 1 and b.text.strip() == (getattr(meta, 'title', '') or '').strip():
                continue
            L.append(b.raw)
            L.append('')
        elif b.kind in ('paragraph', 'list_item'):
            if skip_section is not None:
                continue
            raw = b.raw.strip()
            low = raw.lower().lstrip('*').lstrip()
            if (low.startswith('author:') or low.startswith('affiliation:')
                    or low.startswith('email:') or low.startswith('orcid:')
                    or low.startswith('keywords:')):
                continue
            t = fl.tex_escape(cm.apply(b.raw, mapping, venue))
            m = re.search(r'!\[([^\]]*)\]\(([^)]+)\)', t)
            if m:
                n_fig += 1
                fig = {'source_path': m.group(2).strip(), 'number': n_fig, 'caption_wording': m.group(1).strip()}
                L.append(fl.emit_figure_latex(fig, venue))
                L.append('')
            else:
                L.append(t)
                L.append('')
        elif b.kind == 'figure':
            fig = fl.collect_figures([b])[0]
            if id(b) in fig_caps:
                fnum, fcap = fig_caps[id(b)]
                fig['number'] = fnum
                fig['caption_wording'] = fcap
            L.append(fl.emit_figure_latex(fig, venue))
            L.append('')
        elif b.kind == 'table':
            tbl = fl.collect_tables([b])[0]
            if id(b) in tab_caps:
                rn, tcap = tab_caps[id(b)]
                tbl['number'] = fl._roman_to_int(rn)
                tbl['caption_wording'] = tcap
            L.append(fl.emit_table_latex(tbl, venue))
            L.append('')
        elif b.kind == 'equation':
            L.append('\\begin{equation}')
            L.append(b.raw)
            L.append('\\end{equation}')
            L.append('')
        elif b.kind == 'code_fence':
            L.append('\\begin{verbatim}')
            L.append(b.raw)
            L.append('\\end{verbatim}')
            L.append('')
        elif b.kind == 'footnote':
            L.append(f'\\footnote{{{fl.tex_escape(b.text)}}}')
        elif b.kind == 'blank':
            L.append('')

    L.append('\\nocite{*}')
    L.append(f'\\bibliographystyle{{{getattr(venue, "bib_style", "IEEEtran")}}}')
    L.append(f'\\bibliography{{references_{getattr(venue, "format_id", "generic")}}}')
    L.append('\\end{document}')
    return '\n'.join(L) + '\n'
