"""SHA256 helpers. Pure stdlib."""
import hashlib
import pathlib


def sha256_file(path) -> str:
    p = pathlib.Path(path)
    h = hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def snapshot(paths) -> dict:
    out = {}
    for p in paths:
        pp = pathlib.Path(p)
        if pp.is_file():
            out[str(pp)] = sha256_file(pp)
    return out
