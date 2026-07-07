"""
OncoLens Layouts Package.

All layout builder functions are collected here.
The main entry point is `create_layout()` from dashboard.py,
which assembles the unified Full HD dashboard.
"""

from app.layouts.dashboard import create_layout

__all__ = ["create_layout"]
