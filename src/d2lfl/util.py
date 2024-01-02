"""
d2lfl.util
==========

Contains utility functions.
"""

from pathlib import Path


def case_insensitive_file_path(base_path: Path, next_component: str) -> Path:
    """
    Given an existing directory `base_path`, returns the path to
    `base_path / next_component`, where `next_component` is a
    case-insensitive filename.

    `base_path` **is case-sensitive**.
    """
    for f in base_path.iterdir():
        if f.name.lower() == next_component.lower():
            return f
    raise FileNotFoundError(f"could not find {base_path / next_component}")
