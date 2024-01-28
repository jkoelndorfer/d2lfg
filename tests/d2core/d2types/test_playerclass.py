"""
``tests.d2core.d2types.test_playerclass``
=========================================

Tests code in :py:mod:`d2lfg.d2core.d2types.playerclass`.
"""

from d2lfg.d2core.d2types.playerclass import Diablo2PlayerClass, Diablo2PlayerClasses


class Diablo2PlayerSubclass(Diablo2PlayerClass):
    """
    Subclass of :py:class:`~d2lfg.d2core.d2types.playerclass.Diablo2PlayerClass`
    for testing copy.
    """


class TestDiablo2PlayerClass:
    def test_copy_produces_correct_type(self) -> None:
        """
        Tests that :py:meth:`~d2lfg.d2core.d2types.playerclass.Diablo2PlayerClass.copy`
        creates an object of the appropriate type.
        """
        new_pc = Diablo2PlayerSubclass.copy(Diablo2PlayerClasses.AMA)

        assert isinstance(new_pc, Diablo2PlayerSubclass)

    def test_hash(self) -> None:
        """
        Tests that a :py:class:`Diablo2PlayerClass` is hashable.
        """
        for pc in Diablo2PlayerClasses.all():
            assert isinstance(hash(pc), int)
