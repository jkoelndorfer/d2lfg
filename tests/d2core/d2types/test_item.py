"""
``tests.d2core.d2types.test_item``
==================================

Tests code in :py:mod:`d2lfg.d2core.d2types.item`.
"""

import pytest

from d2lfg.d2core.d2types.bodyloc import Diablo2BodyLocs
from d2lfg.d2core.d2types.item import Diablo2ItemType, Diablo2Item


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
    )


@pytest.fixture
def axe_item(axe_item_type: Diablo2ItemType) -> Diablo2Item:
    """
    A :py:class:`d2lfg.d2core.d2types.item.Diablo2Item` representing the
    ``axe`` item. This item is modeled after actual data taken from
    ``Weapons.txt``.
    """
    return Diablo2Item(
        code="axe",
        type=axe_item_type,
        type2=None,
        name="Axe",
        level=7,
        levelreq=0,
        gemsockets=2,
        durability=48,
        normcode="axe",
        ubercode="9ax",
        ultracode="7ax",
        reqstr=32,
        reqdex=0,
    )


@pytest.fixture
def normal_item() -> Diablo2Equipment:
    """
    A normal-tier :py:class:`d2lfg.d2core.d2types.item.Diablo2Equipment`.
    """
    return Diablo2Equipment(test="hello")


class TestDiablo2Equipment:
    """
    Tests :py:class:`d2lfg.d2core.d2types.item.Diablo2Equipment`.
    """

    def test_is_normal_when_item_is_normal(self) -> None:
        """
        Verifies that ``is_normal`` returns ``True`` when the given item is normal.
        """
        pass
