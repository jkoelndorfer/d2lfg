"""
``tests.d2core.d2types.test_bodyloc``
=====================================

Tests code in :py:mod:`d2lfg.d2core.d2types.bodyloc`.
"""

import pytest

from d2lfg.error import DataLookupError
from d2lfg.d2core.d2types import Diablo2BodyLoc, Diablo2BodyLocs


class TestDiablo2BodyLoc:
    """
    Tests :py:class:`~d2lfg.d2core.d2types.bodyloc.Diablo2BodyLoc`.
    """

    def test_hash(self) -> None:
        """
        Verifies that :py:class:`~d2lfg.d2core.d2types.bodyloc.Diablo2BodyLoc` objects
        are hashable.
        """
        for loc in Diablo2BodyLocs.all():
            assert isinstance(hash(loc), int)


class TestDiablo2BodyLocs:
    """
    Tests :py:class:`~d2lfg.d2core.d2types.bodyloc.Diablo2BodyLocs`.
    """

    @pytest.mark.parametrize("loc_str", [
        "HEAD",
        "TORS",
        "TORSO",
        "LRIN",
        "RIGHT_ARM",
    ])
    def test_successful_lookup(self, loc_str: str) -> None:
        """
        Verifies that a valid body location lookup returns a
        :py:class:`~d2lfg.d2core.d2types.bodyloc.Diablo2BodyLoc`.

        :param loc_str: the body location string which should be successfully looked up
        """
        body_loc = Diablo2BodyLocs.lookup(loc_str)

        assert isinstance(body_loc, Diablo2BodyLoc)

    @pytest.mark.parametrize("loc_str", [
        "NOTHEAD",
        "LIGHT_ARM",
        "RRING2",
    ])
    def test_unsuccessful_lookup(self, loc_str: str) -> None:
        """
        Verifies that an invalid body location lookup raises a
        :py:class:`~d2lfg.error.DataLookupError`.

        :param loc_str: the *invalid* body location which should fail a lookup
        """
        with pytest.raises(DataLookupError):
            Diablo2BodyLocs.lookup(loc_str)
