"""
Vercel FastAPI services entry point.
Vercel's FastAPI framework detection looks for `main.py` at the service root.
This file re-exports the FastAPI `app` from the actual app package.
"""
import sys
import os

# Ensure the backend directory (this file's directory) is on sys.path
_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)

from app.main import app  # noqa: F401 — Vercel detects `app` here
