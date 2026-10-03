"""Compile LaTeX via optional pdflatex/latexmk/bibtex. Never writes outside cwd."""
from __future__ import annotations
import pathlib
import shutil
import subprocess


def which_latex():
    for c in ('pdflatex', 'latexmk'):
        if shutil.which(c):
            return c
    return None


def which_bib():
    for c in ('bibtex', 'biber'):
        if shutil.which(c):
            return c
    return None


def compile(tex_path, cwd, venue, timeout: int = 120) -> tuple:
    cwd_p = pathlib.Path(cwd)
    tex_p = pathlib.Path(tex_path)
    engine = getattr(venue, 'compile_engine', 'pdflatex') or 'pdflatex'
    bib = getattr(venue, 'bib_engine', 'bibtex') or 'bibtex'
    if shutil.which(engine) is None:
        engine = which_latex() or engine
    if shutil.which(bib) is None:
        bib = which_bib() or bib
    log = []
    ok = False
    try:
        def run(cmd):
            r = subprocess.run(cmd, cwd=str(cwd_p), capture_output=True, text=True, timeout=timeout)
            log.append('$ ' + ' '.join(cmd))
            log.append(r.stdout or '')
            log.append(r.stderr or '')
            return r.returncode == 0
        texname = tex_p.name
        stem = tex_p.stem
        if shutil.which(engine) is None:
            log.append(f'engine {engine} not found')
            (cwd_p / 'compile.log').write_text('\n'.join(log), encoding='utf-8')
            return False, '\n'.join(log)
        s1 = run([engine, '-interaction=nonstopmode', texname])
        if shutil.which(bib) is not None:
            try:
                run([bib, stem])
            except Exception as e:
                log.append(str(e))
        s2 = run([engine, '-interaction=nonstopmode', texname])
        s3 = run([engine, '-interaction=nonstopmode', texname])
        ok = bool(s1 and s2 and s3)
    except Exception as e:
        log.append(str(e))
        ok = False
    try:
        (cwd_p / 'compile.log').write_text('\n'.join(log), encoding='utf-8')
    except Exception:
        pass
    return ok, '\n'.join(log)
