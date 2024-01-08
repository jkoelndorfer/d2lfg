"""
``tests.d2core.d2types.test_item.test_item``
============================================

Tests :py:class:`d2lfg.d2core.d2types.item.Diablo2ItemType`.
"""

from d2lfg.d2core.d2types.item import Diablo2Item, Diablo2ItemTier


class TestDiablo2Item:
    """
    Tests :py:class:`~d2lfg.d2core.d2types.Diablo2Item`.
    """

    def test_axe_is_equippable(self, axe_item: Diablo2Item) -> None:
        """
        Verifies that the axe is equippable.
        """

        assert axe_item.equippable()

    def test_axe_is_normal(self, axe_item: Diablo2Item) -> None:
        """
        Verifies that the axe is a normal tier item.
        """

        assert axe_item.tier == Diablo2ItemTier.NORMAL

    def test_cleaver_is_exceptional(self, cleaver_item: Diablo2Item) -> None:
        """
        Verifies that the cleaver is an exceptional tier item.
        """

        assert cleaver_item.tier == Diablo2ItemTier.EXCEPTIONAL

    def test_small_crescent_is_elite(self, small_crescent_item: Diablo2Item) -> None:
        """
        Verifies that the small crescent is an elite tier item.
        """

        assert small_crescent_item.tier == Diablo2ItemTier.ELITE

    def test_amulet_is_normal(self, amulet_item: Diablo2Item) -> None:
        """
        Verifies that the amulet is a normal tier item.

        TODO: Is this correct behavior? Items in ``Misc.txt`` do not have
        a ``normcode``, ``ubercode``, or ``ultracode``.
        """
        assert amulet_item.tier == Diablo2ItemTier.NORMAL

    def test_amulet_is_equippable(self, amulet_item: Diablo2Item) -> None:
        """
        Verifies that the amulet is equippable.
        """

        assert amulet_item.equippable()
