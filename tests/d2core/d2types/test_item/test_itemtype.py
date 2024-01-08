"""
``tests.d2core.d2types.test_item.test_itemtype``
================================================

Tests :py:class:`d2lfg.d2core.d2types.item.Diablo2ItemType`.
"""

from d2lfg.d2core.d2types.item import Diablo2ItemType


class TestDiablo2ItemType:
    """
    Tests :py:class:`~d2lfg.d2core.d2types.Diablo2ItemType`.
    """

    def test_all_types_yielded_once(self, axe_item_type: Diablo2ItemType) -> None:
        """
        Verifies that :py:meth:`d2lfg.d2core.d2types.item.Diablo2ItemType.all_types`
        yields all item types exactly once.
        """
        expected_axe_types = ["axe", "gen", "mele", "mgen", "weap"]

        all_axe_types = sorted(list(t.code for t in axe_item_type.all_types()))

        assert all_axe_types == expected_axe_types

    def test_axe_equippable(self, axe_item_type: Diablo2ItemType) -> None:
        """
        Verifies that the axe item type is equippable.
        """

        assert axe_item_type.equippable()

    def test_weap_not_equippable(self, weap_item_type: Diablo2ItemType) -> None:
        """
        Verifies that the weap item type is *not* equippable.
        """

        assert not weap_item_type.equippable()
