"""
``tests.d2core.d2types.test_playerclass``
=========================================

Tests code in :py:mod:`d2lfg.d2core.d2types.playerclass`.
"""

from d2lfg.d2core.d2types.playerclass import Diablo2PlayerClasses


class TestDiablo2PlayerClass:
    def test_hash(self) -> None:
        """
        Tests that a :py:class:`Diablo2PlayerClass` is hashable.
        """
        for pc in Diablo2PlayerClasses.all():
            assert isinstance(hash(pc), int)
