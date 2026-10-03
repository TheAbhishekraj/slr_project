"""Thin wrapper for python tools/venue_format.py."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from venue_format.cli import main

if __name__ == '__main__':
    raise SystemExit(main())
