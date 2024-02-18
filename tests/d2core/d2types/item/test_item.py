"""
``tests.d2core.d2types.item.test_item``
=======================================

Tests :py:class:`d2lfg.d2core.d2types.item.Diablo2ItemType`.
"""

from d2lfg.d2core.d2types.bodyloc import Diablo2BodyLoc
from d2lfg.d2core.d2types.item import (
    Diablo2Item,
    Diablo2ItemTier,
    Diablo2ItemTiers,
    Diablo2ItemType,
)
from d2lfg.d2core.d2types.playerclass import Diablo2PlayerClass

Item = Diablo2Item[Diablo2ItemType[Diablo2BodyLoc, Diablo2PlayerClass]]


class TestDiablo2Item:
    """
    Tests :py:class:`~d2lfg.d2core.d2types.item.Diablo2Item`.
    """

    def test_axe_is_equippable(self, axe_item: Item) -> None:
        """
        Verifies that the axe is equippable.
        """

        assert axe_item.equippable()

    def test_axe_is_normal(self, axe_item: Item) -> None:
        """
        Verifies that the axe is a normal tier item.
        """

        assert axe_item.tier == Diablo2ItemTiers.NORMAL

    def test_cleaver_is_exceptional(self, cleaver_item: Item) -> None:
        """
        Verifies that the cleaver is an exceptional tier item.
        """

        assert cleaver_item.tier == Diablo2ItemTiers.EXCEPTIONAL

    def test_small_crescent_is_elite(self, small_crescent_item: Item) -> None:
        """
        Verifies that the small crescent is an elite tier item.
        """

        assert small_crescent_item.tier == Diablo2ItemTiers.ELITE

    def test_amulet_is_normal(self, amulet_item: Item) -> None:
        """
        Verifies that the amulet is a normal tier item.

        TODO: Is this correct behavior? Items in ``Misc.txt`` do not have
        a ``normcode``, ``ubercode``, or ``ultracode``.
        """
        assert amulet_item.tier == Diablo2ItemTiers.NORMAL

    def test_amulet_is_equippable(self, amulet_item: Item) -> None:
        """
        Verifies that the amulet is equippable.
        """

        assert amulet_item.equippable()


class TestDiablo2ItemTier:
    """
    Tests :py:class:`~d2lfg.d2core.d2types.item.Diablo2ItemTier`.
    """

    def test_hashable(self) -> None:
        """
        Verifies that a Diablo2ItemTier is hashable.
        """
        tier = Diablo2ItemTier("normal", "norm")

        assert isinstance(hash(tier), int)


class TestDiablo2ItemTiers:
    """
    Tests :py:class:`~d2lfg.d2core.d2types.item.Diablo2ItemTiers`.
    """

    def test_collection_type(self) -> None:
        """
        Verifies that Diablo2ItemTiers has the correct collection type.
        """
        assert Diablo2ItemTiers.collection_type() == Diablo2ItemTier
