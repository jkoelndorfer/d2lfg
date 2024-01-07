"""
``tests.d2core.d2types.test_item``
==================================

Tests code in :py:mod:`d2lfg.d2core.d2types.item`.
"""

import pytest

from d2lfg.d2core.d2types.bodyloc import Diablo2BodyLocs
from d2lfg.d2core.d2types.item import Diablo2ItemType


@pytest.fixture
def weap_item_type() -> Diablo2ItemType:
    """
    A :py:class:`d2lfg.d2core.d2types.item.Diablo2ItemType` representing
    the "weap" (Weapon) type.
    """
    return Diablo2ItemType(
        name="Weapon",
        code="weap",
        equiv1=None,
        equiv2=None,
        body=False,
        bodyloc1=None,
        bodyloc2=None,
        shoots=None,
        quiver=None,
        throwable=False,
        reload=False,
        reequip=False,
        autostack=False,
        gem=False,
        beltable=False,
        maxsock1=0,
        maxsock25=0,
        maxsock40=0,
        staffmods=None,
        class_=None,
        storepage=None,
    )


@pytest.fixture
def gen_item_type() -> Diablo2ItemType:
    """
    A :py:class:`d2lfg.d2core.d2types.item.Diablo2ItemType` representing
    the "gen" (General Weapon) type.
    """
    return Diablo2ItemType(
        name="General Weapon",
        code="gen",
        equiv1=None,
        equiv2=None,
        body=True,
        bodyloc1=None,
        bodyloc2=None,
        shoots=None,
        quiver=None,
        throwable=False,
        reload=False,
        reequip=False,
        autostack=False,
        gem=False,
        beltable=False,
        maxsock1=0,
        maxsock25=0,
        maxsock40=0,
        staffmods=None,
        class_=None,
        storepage=None,
    )


@pytest.fixture
def mele_item_type(weap_item_type: Diablo2ItemType) -> Diablo2ItemType:
    """
    A :py:class:`d2lfg.d2core.d2types.item.Diablo2ItemType` representing
    the "mele" (Melee Weapon) type.
    """
    return Diablo2ItemType(
        name="Melee Weapon",
        code="mele",
        equiv1=weap_item_type,
        equiv2=None,
        body=False,
        bodyloc1=None,
        bodyloc2=None,
        shoots=None,
        quiver=None,
        throwable=False,
        reload=False,
        reequip=False,
        autostack=False,
        gem=False,
        beltable=False,
        maxsock1=0,
        maxsock25=0,
        maxsock40=0,
        staffmods=None,
        class_=None,
        storepage=None,
    )


@pytest.fixture
def mgen_item_type(
    gen_item_type: Diablo2ItemType, mele_item_type: Diablo2ItemType
) -> Diablo2ItemType:
    """
    A :py:class:`d2lfg.d2core.d2types.item.Diablo2ItemType` representing
    the "mgen" (general melee) type.
    """
    return Diablo2ItemType(
        name="General Melee",
        code="mgen",
        equiv1=mele_item_type,
        equiv2=gen_item_type,
        body=True,
        bodyloc1=None,
        bodyloc2=None,
        shoots=None,
        quiver=None,
        throwable=False,
        reload=False,
        reequip=False,
        autostack=False,
        gem=False,
        beltable=False,
        maxsock1=0,
        maxsock25=0,
        maxsock40=0,
        staffmods=None,
        class_=None,
        storepage=None,
    )


@pytest.fixture
def axe_item_type(mgen_item_type: Diablo2ItemType) -> Diablo2ItemType:
    """
    A :py:class:`d2lfg.d2core.d2types.item.Diablo2ItemType` representing
    the "axe" type.
    """
    return Diablo2ItemType(
        name="Axe",
        code="axe",
        equiv1=mgen_item_type,
        equiv2=None,
        body=True,
        bodyloc1=Diablo2BodyLocs.RIGHT_ARM,
        bodyloc2=Diablo2BodyLocs.LEFT_ARM,
        shoots=None,
        quiver=None,
        throwable=False,
        reload=False,
        reequip=False,
        autostack=False,
        gem=False,
        beltable=False,
        maxsock1=0,
        maxsock25=0,
        maxsock40=0,
        staffmods=None,
        class_=None,
        storepage=None,
    )


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
