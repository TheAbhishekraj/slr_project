"""Figures and tables: collect and emit LaTeX without rewording."""
from __future__ import annotations
import pathlib
import re
import shutil


FIGCAP_RE = re.compile(r'^\s*\*\*Fig\.\s*(\d+)\.\*\*\s*(.+?)\s*$')
TABCAP_RE = re.compile(r'^\s*\*\*Table\s+([IVXLC]+)\.\*\*\s*(.+?)\s*$')

_SPECIALS = (('&', '\\&'), ('%', '\\%'), ('$', '\\$'), ('#', '\\#'), ('_', '\\_'),
             ('~', '\\textasciitilde{}'), ('^', '\\textasciicircum{}'))


def tex_escape(s: str) -> str:
    """LaTeX-escape specials and **bold**; \\cite spans left untouched."""
    parts = re.split(r'(\\cite\{[^}]*\})', s)
    out = []
    for p in parts:
        if p.startswith('\\cite{'):
            out.append(p)
            continue
        p = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', p)
        for ch, rep in _SPECIALS:
            p = p.replace(ch, rep)
        out.append(p)
    return ''.join(out)


def pair_float_captions(blocks) -> tuple:
    """Match figure blocks to the following **Fig. N.** caption paragraph and
    table blocks to the preceding **Table X.** caption paragraph.
    Returns (fig_caps, tab_caps, consumed_block_ids)."""
    fig_caps: dict = {}
    tab_caps: dict = {}
    consumed: set = set()
    for i, b in enumerate(blocks):
        if b.kind == 'figure':
            j = i + 1
            while j < len(blocks) and blocks[j].kind == 'blank':
                j += 1
            if j < len(blocks) and blocks[j].kind == 'paragraph':
                m = FIGCAP_RE.match(blocks[j].raw)
                if m:
                    fig_caps[id(b)] = (int(m.group(1)), m.group(2))
                    consumed.add(id(blocks[j]))
        elif b.kind == 'table':
            j = i - 1
            while j >= 0 and blocks[j].kind == 'blank':
                j -= 1
            if j >= 0 and blocks[j].kind == 'paragraph':
                m = TABCAP_RE.match(blocks[j].raw)
                if m:
                    tab_caps[id(b)] = (m.group(1), m.group(2))
                    consumed.add(id(blocks[j]))
    return fig_caps, tab_caps, consumed


def collect_figures(blocks) -> list:
    fig_caps, _, _ = pair_float_captions(blocks)
    figs = []
    n = 0
    for b in blocks:
        if b.kind == 'figure':
            n += 1
            num, cap = fig_caps.get(id(b), (n, b.meta.get('caption', b.text)))
            figs.append({'source_path': b.meta.get('src', ''), 'number': num, 'caption_wording': cap})
        elif b.kind == 'paragraph':
            for m in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', b.raw):
                n += 1
                figs.append({'source_path': m.group(2).strip(), 'number': n, 'caption_wording': m.group(1).strip()})
    return figs


def collect_tables(blocks) -> list:
    _, tab_caps, _ = pair_float_captions(blocks)
    tbls = []
    n = 0
    for b in blocks:
        if b.kind == 'table':
            n += 1
            rows = b.meta.get('rows', b.raw.splitlines())
            rn_cap = tab_caps.get(id(b))
            if rn_cap:
                tbls.append({'source_path': '', 'number': _roman_to_int(rn_cap[0]), 'caption_wording': rn_cap[1], 'rows': list(rows), 'block': b})
            else:
                tbls.append({'source_path': '', 'number': n, 'caption_wording': '', 'rows': list(rows), 'block': b})
    return tbls


def _roman(n: int) -> str:
    vals = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    out = ''
    for v, s in vals:
        while n >= v:
            out += s
            n -= v
    return out or 'I'


def _roman_to_int(r: str) -> int:
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    total = 0
    prev = 0
    for ch in reversed(r.upper()):
        v = vals.get(ch, 0)
        total += -v if v < prev else v
        prev = max(prev, v)
    return total or 1


def emit_figure_latex(fig: dict, venue) -> str:
    n = fig.get('number', 1)
    fmt = getattr(venue, 'fig_label_fmt', 'Fig. {n}.')
    try:
        label_txt = fmt.format(n=n, ROMAN=_roman(n))
    except Exception:
        label_txt = f'Fig. {n}.'
    cap = tex_escape(fig.get('caption_wording', ''))
    src = fig.get('source_path', '')
    if src:
        src = 'FIGURES/' + src.replace('\\', '/').rstrip('/').rsplit('/', 1)[-1]
    return '\n'.join(['\\begin{figure}[htbp]', '\\centering', f'\\includegraphics[width=\\columnwidth]{{{src}}}', f'\\caption{{{cap}}}', f'\\label{{fig:{n}}}', '\\end{figure}'])


def emit_table_latex(tbl: dict, venue) -> str:
    from .trace import ContentDrift
    n = tbl.get('number', 1)
    rows = tbl.get('rows', [])
    fmt = getattr(venue, 'tbl_label_fmt', 'TABLE {ROMAN}.')
    try:
        label_txt = fmt.format(n=n, ROMAN=_roman(n))
    except Exception:
        label_txt = f'TABLE {n}.'
    data = []
    for r in rows:
        data.append([c.strip() for c in r.strip().strip('|').split('|')])
    body = []
    for idx, r in enumerate(data):
        joined = ' '.join(r)
        if idx == 1 and set(joined.replace(' ', '').replace(':', '').replace('-', '')) == set():
            continue
        body.append(r)
    ncols = max((len(r) for r in body), default=1)
    colspec = ' '.join(['l'] * ncols)
    cap = (tbl.get('caption_wording', '') or '').strip()
    lines = [f'\\begin{{table}}[htbp]', '\\centering']
    if cap:
        lines.append(f'\\caption{{{cap}}}')
    lines.append(f'\\label{{tab:{n}}}')
    lines.append(f'\\begin{{tabular}}{{{colspec}}}')
    lines.append('\\hline')
    for r in body:
        while len(r) < ncols:
            r.append('')
        lines.append(' & '.join(tex_escape(c) for c in r) + ' \\\\')
        lines.append('\\hline')
    lines += ['\\end{tabular}', '\\end{table}']
    out = '\n'.join(lines)
    if out.count('\\\\') != len(body):
        raise ContentDrift('table row count mismatch')
    return out


def copy_float_assets(repo, out) -> list:
    repo_p = pathlib.Path(repo)
    out_p = pathlib.Path(out)
    copied = []
    srcs = {'FIGURES': [repo_p / 'FIGURES', repo_p / '05_analysis' / 'figures'],
            'TABLES': [repo_p / 'TABLES']}
    for name, candidates in srcs.items():
        for src in candidates:
            if src.is_dir():
                dst = out_p / name
                dst.mkdir(parents=True, exist_ok=True)
                for f in src.iterdir():
                    if f.is_file():
                        shutil.copy2(f, dst / f.name)
                        copied.append(str(dst / f.name))
    return copied
