"""Figures and tables: collect and emit LaTeX without rewording."""
from __future__ import annotations
import pathlib
import shutil


def collect_figures(blocks) -> list:
    figs = []
    n = 0
    for b in blocks:
        if b.kind == 'figure':
            n += 1
            figs.append({'source_path': b.meta.get('src', ''), 'number': n, 'caption_wording': b.meta.get('caption', b.text)})
        elif b.kind == 'paragraph':
            import re
            for m in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', b.raw):
                n += 1
                figs.append({'source_path': m.group(2).strip(), 'number': n, 'caption_wording': m.group(1).strip()})
    return figs


def collect_tables(blocks) -> list:
    tbls = []
    n = 0
    for b in blocks:
        if b.kind == 'table':
            n += 1
            rows = b.meta.get('rows', b.raw.splitlines())
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


def emit_figure_latex(fig: dict, venue) -> str:
    n = fig.get('number', 1)
    fmt = getattr(venue, 'fig_label_fmt', 'Fig. {n}.')
    try:
        label_txt = fmt.format(n=n, ROMAN=_roman(n))
    except Exception:
        label_txt = f'Fig. {n}.'
    cap = fig.get('caption_wording', '').replace('}', '\\}')
    src = fig.get('source_path', '')
    return '\n'.join(['\\begin{figure}[htbp]', '\\centering', f'\\includegraphics[width=\\columnwidth]{{{src}}}', f'\\caption{{{label_txt} {cap}}}', f'\\label{{fig:{n}}}', '\\end{figure}'])


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
        lines.append(f'\\caption{{{label_txt} {cap}}}')
    lines.append(f'\\label{{tab:{n}}}')
    lines.append(f'\\begin{{tabular}}{{{colspec}}}')
    lines.append('\\hline')
    for r in body:
        while len(r) < ncols:
            r.append('')
        lines.append(' & '.join(c.replace('&', '\\&') for c in r) + ' \\\\')
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
    for name in ('FIGURES', 'TABLES'):
        src = repo_p / name
        if src.is_dir():
            dst = out_p / name
            dst.mkdir(parents=True, exist_ok=True)
            for f in src.iterdir():
                if f.is_file():
                    shutil.copy2(f, dst / f.name)
                    copied.append(str(dst / f.name))
    return copied
