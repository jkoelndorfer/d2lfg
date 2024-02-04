"""
``tests.d2core.d2types.test_skill``
===================================

Tests code in :py:mod:`d2lfg.d2core.d2types.skill`.
"""

from d2lfg.d2core.d2types.playerclass import Diablo2PlayerClasses
from d2lfg.d2core.d2types.skill import Diablo2Skill


class TestDiablo2Skill:
    """
    Tests :py:class:`~d2lfg.d2core.d2types.skill.Diablo2Skill`.
    """

    def test_hashable(self) -> None:
        """
        Verifies that a Diablo2Skill is hashable.
        """
        skill = Diablo2Skill(10, Diablo2PlayerClasses.AMAZON, "Jab", 3)

        assert isinstance(hash(skill), int)
