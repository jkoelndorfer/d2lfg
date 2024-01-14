"""
``tests.bh.config.itemdisplay.test_outputcode``
===============================================

This module contains test code for :py:mod:`d2lfg.bh.config.itemdisplay.outputcode`.
"""

import pytest

from d2lfg.bh.config.itemdisplay.outputcode import BHOutputCodeLiteral


class TestBHOutputCode:
    """
    Tests :py:class:`~d2lfg.bh.config.itemdisplay.outputcode.BHOutputCode`.
    """

    @pytest.mark.parametrize("code", ["CONTINUE", "NL"])
    def test_str_surrounded_by_percent(self, code: str) -> None:
        """
        Verifies that stringifying a
        :py:class:`~d2lfg.bh.config.itemdisplay.outputcode.BHOutputCode` wraps the
        code in ``%`` characters.
        """
        mock_code = BHOutputCodeLiteral(code)

        assert str(mock_code) == f"%{code}%"
