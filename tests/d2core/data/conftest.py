"""
``tests.d2core.data.conftest``
==============================

This module contains fixtures for Diablo 2 data processing tests.
"""

from pathlib import Path

import pytest

from d2lfg.d2core.data.txt import Diablo2TxtFile, Diablo2TxtParser


@pytest.fixture
def txt_parser() -> Diablo2TxtParser:
    """
    Returns a :py:class:`~d2lfg.d2core.data.txt.Diablo2TxtParser`
    """
    return Diablo2TxtParser()


@pytest.fixture
def weapons_txt_snippet_path() -> Path:
    """
    Returns a path to a snippet of a valid Diablo 2 Weapons.txt.
    """
    return Path(__file__).parent / "fixtures" / "snippet-weapons.txt"


@pytest.fixture
def weapons_txt_file(
    txt_parser: Diablo2TxtParser, weapons_txt_snippet_path: Path
) -> Diablo2TxtFile:
    return txt_parser.parse(weapons_txt_snippet_path)
