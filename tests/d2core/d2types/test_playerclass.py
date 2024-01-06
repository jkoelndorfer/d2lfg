"""
``tests.d2core.d2types.test_playerclass``
=========================================

Tests code in :py:mod:`d2lfg.d2core.d2types.playerclass`.
"""

import pytest

from d2lfg.d2core.d2types import Diablo2PlayerClass, Diablo2PlayerClasses


class TestDiablo2PlayerClasses:
    """
    Tests functionality of the :py:class:`Diablo2PlayerClasses` collection.
    """


class TestDiablo2PlayerClass:
    def test_playerclass_equality(self, pc: Diablo2PlayerClass) -> None:
        """
        Tests that a :py:class:`Diablo2PlayerClass` compares equal to
        itself.
        """
