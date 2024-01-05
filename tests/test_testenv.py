"""
tests/test_testenv.py
=====================

This file contains tests that help verify the testing environment.

If any tests here fail, there is probably something wrong with
the environment we are testing in.
"""

import d2lfg


def test_d2lfg_import() -> None:
    """
    This test verifies d2lfg is imported.

    It should never fail.
    """
    assert d2lfg is not None


def test_d2lfg_version() -> None:
    """
    This test verifies that d2lfg's version is set.
    """
    assert isinstance(d2lfg.__version__, str)
