"""
utils.py
--------

Small helper utilities.
"""

import os


def ensure_dir(path):
    """Create directory if not exists."""
    os.makedirs(path, exist_ok=True)
