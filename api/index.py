"""
Vercel Serverless Python entrypoint.
Vercel looks for `app` (ASGI) in this file.
"""
import sys
import os

# Add the backend directory to the Python path so `app.*` imports work
_backend_dir = os.path.join(os.path.dirname(__file__), "..", "backend")
_backend_dir = os.path.abspath(_backend_dir)

if _backend_dir not in sys.path:
    sys.path.insert(0, _backend_dir)

# Expose the FastAPI app — Vercel detects the `app` variable automatically
from app.main import app  # noqa: F401, E402
