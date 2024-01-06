"""
Diablo 2 Loot Filter Generator (``d2lfg``)
==========================================

Diablo 2 Loot Filter Generator (``d2lfg``) is a small Python library
to aid in maintenance of Diablo 2 loot filter configurations.
"""

from .__version__ import __version__
from . import d2core
from . import error

__all__ = [
    "d2core",
    "error",
    "__version__",
]
