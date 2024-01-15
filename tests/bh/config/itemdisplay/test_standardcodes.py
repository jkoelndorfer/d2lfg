"""
``tests.bh.config.itemdisplay.test_standardcodes``
==================================================

This module contains test code for :py:mod:`d2lfg.bh.config.itemdisplay.standardcodes`.
"""

from d2lfg.bh.config.itemdisplay.standardcodes import BHCodes


class TestBHCodes:
    """
    Tests :py:class:`~d2lfg.bh.config.itemdisplay.standardcodes.BHCodes`.
    """

    def test_bhcodes(self) -> None:
        """
        Verifies :py:class:`~d2lfg.bh.config.itemdisplay.standardcodes.BHCodes` can
        be imported.
        """
        assert BHCodes is not None
