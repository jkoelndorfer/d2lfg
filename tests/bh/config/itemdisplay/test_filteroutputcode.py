"""
``tests.bh.config.itemdisplay.test_filteroutputcode``
=====================================================

This module contains test code for
:py:mod:`d2lfg.bh.config.itemdisplay.filteroutputcode`.
"""

import pytest

from tests.testhelper.typing import FixtureRequest

from d2lfg.bh.config.itemdisplay.filteroutputcode import BHFilterOutputCodeLiteral as FC


@pytest.fixture(params=["ILVL", "LVLREQ"])
def test_code(request: FixtureRequest[str]) -> str:
    return request.param


@pytest.fixture
def filter_output_code(test_code: str) -> FC:
    return FC(test_code)


class TestBHFilterOutputCode:
    """
    Tests :py:class:`~d2lfg.bh.config.itemdisplay.filteroutputcode.BHFilterOutputCode`.
    """

    def test_bhexpr_returns_code(self, filter_output_code: FC, test_code: str) -> None:
        """
        Verifies that ``bhexpr()`` returns the expected value.
        """
        assert filter_output_code.bhexpr() == test_code

    def test_str_produces_substitutable_token(
        self, filter_output_code: FC, test_code: str
    ) -> None:
        """
        Verifies that stringifying a
        :py:class:`~d2lfg.bh.config.itemdisplay.filteroutputcode.BHFilterOutputCode`
        produces a subtituable token surrounded by ``%`` characters.
        """
        assert str(filter_output_code) == f"%{test_code}%"
