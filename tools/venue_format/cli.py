"""CLI with frozen signature. Phases P0..P7. Read-only source, writes only --out."""
from __future__ import annotations
import argparse
import pathlib
import sys

from .card import load_venue, load_profile
from .sha import snapshot
from .read_manuscript import parse_markdown
from . import heading_map as hm
from . import citation_map as cm
from . import refs_convert as rc
from . import floats as fl
from . import latex_emit as le
from . import compile_pdf as cp
from . import trace as tr
from . import report as rp
from .trace import ContentDrift


def _resolve(p: str, repo: pathlib.Path) -> pathlib.Path:
    pp = pathlib.Path(p)
    if pp.is_absolute():
        return pp
    return repo / p


def _check_banned(blocks, profile):
    bo = [w for w in (getattr(profile, 'banned_openers', []) or []) if w]
    for b in blocks:
        if b.kind not in ('paragraph', 'list_item'):
            continue
        t = b.text
        for o in bo:
            if o and t.strip().lower().startswith(o.lower()):
                raise ContentDrift(f'banned opener used: {o}')


def _freeze_check(profile, out_tex):
    import re, hashlib, pathlib
    from collections import Counter
    src = pathlib.Path(profile.manuscript_md).read_text(encoding='utf-8')
    tex = pathlib.Path(out_tex).read_text(encoding='utf-8')
    TOK = re.compile(r'REC_\d+|[A-Za-z0-9]+(?:[.\-]?[A-Za-z0-9]+)*%?')

    def canon_md(s):
        s = re.sub(r'(?m)^#[ \t]+.*$', ' ', s, count=1)
        s = re.sub(r'^#+\s*', '', s, flags=re.M)
        s = re.sub(r'(?m)^!\[.*$', ' ', s)
        s = re.sub(r'\[@[^\]]+\]', ' ', s)
        s = re.sub(r'(?<=\d)%', ' percent ', s)
        s = re.sub(r'[;]', ' ', s)
        s = re.sub(r'(?i)(?<![\w-])gps-denied(?![\w-])', 'gps denied', s)
        s = s.replace('|', ' ')
        s = re.sub(r'(?m)^[\s:\-]+$', ' ', s)
        s = re.sub(r'\[REC_\d+(?:[,\s]+REC_\d+)*\]', ' ', s)
        s = re.sub(r'(?m)^\s*\*\*(?:Fig\.|Table)\s+[IVXLC0-9]+\.\*\*.*$', ' ', s)
        s = re.sub(r'[*_`>]', ' ', s)
        s = re.sub(r'(?<!\w)(?:Fig\.|TABLE|Table|Figure)\s+[IVXLC0-9]+\.?\s*', ' ', s)
        s = re.sub(r'\(\s*Fig\.[^()]*\)', ' ', s)
        s = re.sub(r'(?<!\w)(X\d+)\s*:\s*(REC_\d+(?:\s*,\s*REC_\d+)*)', r' \1 \2 ', s)
        s = re.sub(r'(\d),(\d)', r'\1\2', s)
        s = re.sub(r'\*\*(.*?)\*\*', r' \1 ', s)
        s = re.sub(r'(?<![\w.])\d+\s+(?=[A-Z])', ' ', s)
        s = re.sub(r'(?<![\w.])[IVXLCDM]+\s+(?=[A-Z])', ' ', s)
        s = re.sub(r'\(\d+\)\s+(?=[A-Z])', ' ', s)
        s = re.sub(r'(?<!\w)_\w+_?', ' ', s)
        return TOK.findall(s.lower())

    def canon_tex(s):
        s = s.split('%FRONTMATTER-END', 1)[-1]
        s = s.split('\\bibliographystyle', 1)[0]
        s = s.replace('\\%', '%')
        s = re.sub(r'(?<=\d)%', ' percent ', s)
        s = re.sub(r'%.*', ' ', s)
        s = re.sub(r'\\caption\{([^}]*)\}', ' ', s)
        s = re.sub(r'\\(section|subsection|subsubsection)\*?\{(.*)\}', r' \2 ', s)
        s = re.sub(r'(?<![\w.])[A-G]\s+(?=\d)', ' ', s)
        s = re.sub(r'\*\*(.*?)\*\*', r' \1 ', s)
        s = re.sub(r'(?<![\w.])[IVXLCDM]+\s+(?=[A-Z])', ' ', s)
        s = re.sub(r'(?<![\w.])[A-G]\s+(?=[A-Z])', ' ', s)
        s = re.sub(r'\(\d+\)\s+(?=[A-Z\d])', ' ', s)
        s = re.sub(r'(\d),(\d)', r'\1\2', s)
        s = re.sub(r'(?<![\w.])\d+\s+(?=[A-Z])', ' ', s)
        s = re.sub(r'\\includegraphics(\[[^\]]*\])?\{[^}]*\}', ' ', s)
        s = re.sub(r'\\begin\{tabular\}\{[^}]*\}', ' ', s)
        s = re.sub(r'\\(begin|end)\{[^}]*\}', ' ', s)
        s = re.sub(r'\\hline', ' ', s)
        s = re.sub(r'\\\\', ' ', s)
        s = re.sub(r'\\&', '&', s)
        s = s.replace('&', ' ')
        s = re.sub(r'\[(\d+)\](\s*-\s*\[\d+\])?', ' ', s)
        s = re.sub(r'\[(\d+)\]\s*,\s*\[(\d+)\]', ' ', s)
        s = re.sub(r'\[htbp\]', ' ', s)
        s = re.sub(r'(?i)(?<![\w-])gps-denied(?![\w-])', 'gps denied', s)
        s = re.sub(r'(?<!\w)(?:Fig\.|TABLE|Table|Figure)\s+[IVXLC0-9]+\.?\s*', ' ', s)
        s = re.sub(r'\(\s*Fig\.[^()]*\)', ' ', s)
        s = re.sub(r'\[REC\\_\d+(?:[,\s]+REC\\_\d+)*\]', ' ', s)
        s = s.replace('\\_', ' ')
        s = re.sub(r'\*\*(.*?)\*\*', r' \1 ', s)
        s = re.sub(r'(?<![\w.])(?:[IVX]+|[A-G])\s+(?=[A-Z])', ' ', s)
        s = re.sub(r'\(\d+\)\s+(?=[A-Z\d])', ' ', s)
        s = re.sub(r'\*\*(Total)\*\*', r' \1 ', s)
        s = re.sub(r'(?<![\w.])\d+\s+(?=[A-Z])', ' ', s)
        s = re.sub(r'(?<![\w.])(?:[IVXLCDM]+|[A-G])\s+(?=[A-Z])', ' ', s)
        s = re.sub(r'\(\d+\)\s+(?=[A-Z])', ' ', s)
        s = re.sub(r'(?<!\w)_\w+_?', ' ', s)
        s = re.sub(r'\\label\{[^}]*\}', ' ', s)
        s = re.sub(r'\\[a-zA-Z]+\*?', ' ', s)
        s = re.sub(r'[{}_^$\\]', ' ', s)
        return TOK.findall(s.lower())

    ta, tb = canon_md(src), canon_tex(tex)
    ca, cb = Counter(ta), Counter(tb)
    a_txt, b_txt = ' '.join(ta), ' '.join(tb)
    print('MD  sha256', hashlib.sha256(a_txt.encode()).hexdigest())
    print('TEX sha256', hashlib.sha256(b_txt.encode()).hexdigest())
    print('MATCH' if ca == cb else 'DRIFT')
    if ca != cb:
        for tok in sorted(set(ca) | set(cb)):
            if ca.get(tok, 0) != cb.get(tok, 0):
                print('TOK', repr(tok), 'md=', ca.get(tok, 0), 'tex=', cb.get(tok, 0))
        raise ContentDrift('text-level drift after LaTeX emit')


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog='venue_format')
    ap.add_argument('--repo', default='.')
    ap.add_argument('--format', dest='fmt', required=True)
    ap.add_argument('--profile', default='tools/formats/slr_profile.generic.conf')
    ap.add_argument('--out', default=None)
    ap.add_argument('--strict', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--phase', default='all')
    ap.add_argument('--confirm', action='store_true')
    ap.add_argument('--no-pdf', action='store_true')
    ap.add_argument('--verbose', action='store_true')
    return ap
def main(argv=None) -> int:
    ap = build_parser()
    args = ap.parse_args(argv)
    try:
        venue = load_venue(args.fmt)
    except Exception as e:
        print(f'usage error: venue card: {e}', file=sys.stderr)
        return 2
    try:
        profile = load_profile(args.profile)
    except Exception as e:
        print(f'usage error: profile card: {e}', file=sys.stderr)
        return 2
    repo = pathlib.Path(args.repo)
    if getattr(profile, 'manuscript_md', ''):
        profile.manuscript_md = str(_resolve(profile.manuscript_md, repo))
    if getattr(profile, 'references_bib', ''):
        profile.references_bib = str(_resolve(profile.references_bib, repo))
    out = pathlib.Path(args.out) if args.out else repo / '06_manuscript' / venue.format_id
    style = (getattr(profile, 'output_style', 'generic') or 'generic').lower()
    is_slr = (style == 'slr')
    if is_slr:
        need = {'manuscript_md': profile.manuscript_md, 'references_bib': profile.references_bib}
        for k in ('locked_numbers', 'evidence_csv', 'number_trace'):
            v = getattr(profile, k, '')
            if v:
                need[k] = str(_resolve(v, repo))
        for k, v in need.items():
            if not v or not pathlib.Path(v).is_file():
                print(f'required file missing: {k}={v}', file=sys.stderr)
                return 2
    else:
        if not profile.manuscript_md or not pathlib.Path(profile.manuscript_md).is_file():
            print(f'required file missing: manuscript_md={profile.manuscript_md}', file=sys.stderr)
            return 2
    phase = str(args.phase)
    if phase not in ('all', '0', '1', '2', '3', '4', '5', '6', '7'):
        print('usage error: --phase must be 0..7 or all', file=sys.stderr)
        return 2
    src_files = [profile.manuscript_md]
    if pathlib.Path(str(profile.references_bib)).is_file():
        src_files.append(str(profile.references_bib))
    src_hashes = snapshot(src_files)
    for k, v in src_hashes.items():
        print(f'SHA {k} {v}')
    plan = [('main.tex', 'spacing', 'markdown', 'latex', 'R3'), (f'references_{venue.format_id}.bib', 'ref-order', 'bib', 'bib-ordered', 'R5'), ('TRACE_PRESERVATION.md', 'none', '-', '-', 'R2'), ('FORMAT_REPORT.md', 'none', '-', '-', 'R2')]
    if phase == '0':
        for r in plan:
            print(r)
        return 0
    if args.dry_run:
        print('PLAN (dry-run, no writes):')
        for r in plan:
            print(r)
        return 0
    if not args.confirm:
        print('PLAN (use --confirm to write):')
        for r in plan:
            print(r)
        return 0
    try:
        blocks, pre_meta = parse_markdown(profile.manuscript_md)
        mapped_blocks = hm.apply(blocks, venue)
        if phase == '1':
            out.mkdir(parents=True, exist_ok=True)
            (out / 'heading_map.txt').write_text('\n'.join(f'{a} -> {b}' for a, b in hm.propose(pre_meta, venue)), encoding='utf-8')
            return 0
        bib_keys: list = []
        if pathlib.Path(str(profile.references_bib)).is_file():
            bib_keys = list(rc.load_bib(str(profile.references_bib)).keys())
        cmap = cm.build(pre_meta, bib_keys)
        if phase == '2':
            out.mkdir(parents=True, exist_ok=True)
            (out / 'citation_map.txt').write_text('\n'.join(f'{k} -> {v}' for k, v in cmap.items()), encoding='utf-8')
            return 0
        entries = rc.load_bib(str(profile.references_bib)) if pathlib.Path(str(profile.references_bib)).is_file() else {}
        ordered = rc.reorder(entries, cmap, venue)
        if phase == '3':
            out.mkdir(parents=True, exist_ok=True)
            rc.emit(ordered, out / f'references_{venue.format_id}.bib', venue)
            return 0
        figs = fl.collect_figures(blocks)
        if phase == '4':
            out.mkdir(parents=True, exist_ok=True)
            (out / 'float_map.txt').write_text(f'figures={len(figs)} tables={len(fl.collect_tables(blocks))}\n', encoding='utf-8')
            return 0
        tex_str = le.build(mapped_blocks, pre_meta, {'citation': cmap}, venue, profile)
        out.mkdir(parents=True, exist_ok=True)
        out_tex = out / 'main.tex'
        post_snap = snapshot(src_files)
        for k in src_hashes:
            if post_snap.get(k) != src_hashes.get(k):
                raise ContentDrift(f'source changed during build: {k}')
        out_tex.write_text(tex_str, encoding='utf-8')
        rc.emit(ordered, out / f'references_{venue.format_id}.bib', venue)
        fl.copy_float_assets(repo, out)
        if phase == '5':
            return 0
        _freeze_check(profile, out_tex)
        tex_text = out_tex.read_text(encoding='utf-8')
        from .read_manuscript import Metadata as _MD
        post_meta = _MD(title=pre_meta.title, authors_as_found=pre_meta.authors_as_found, abstract=pre_meta.abstract, keywords_as_found=pre_meta.keywords_as_found, section_list=list(pre_meta.section_list), rec_ids_found=list(pre_meta.rec_ids_found), numeral_tokens_found=list(pre_meta.numeral_tokens_found), reference_keys_found=list(pre_meta.reference_keys_found))
        if '[UNTRACEABLE]' in tex_text:
            raise ContentDrift('[UNTRACEABLE] introduced')
        if is_slr:
            _check_banned(blocks, profile)
            src_raw = pathlib.Path(profile.manuscript_md).read_text(encoding='utf-8')
            for w in (getattr(profile, 'banned_words', []) or []):
                if w and w.lower() in tex_text.lower() and w.lower() not in src_raw.lower():
                    raise ContentDrift(f'banned word introduced: {w}')
        ok = True
        if not args.no_pdf and phase in ('all', '6'):
            ok, clog = cp.compile(out_tex, out, venue)
        if phase == '6':
            return 0 if ok else 3
        emitted = [str(out_tex), str(out / f'references_{venue.format_id}.bib')]
        emitted_hashes = snapshot([e for e in emitted if pathlib.Path(e).is_file()])
        (out / 'TRACE_PRESERVATION.md').write_text(tr.build(repo, out, src_hashes, emitted_hashes, venue, profile, pre_meta, post_meta), encoding='utf-8')
        (out / 'FORMAT_REPORT.md').write_text(rp.build(plan, plan, 'none', venue, profile), encoding='utf-8')
        for f in figs:
            if f.get('caption_wording') and f['caption_wording'] not in tex_text:
                raise ContentDrift(f'figure caption altered: {f}')
        print('MATCH build complete')
        if not ok and not args.no_pdf:
            return 3
        return 0
    except ContentDrift as e:
        print(f'DRIFT {e}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())


