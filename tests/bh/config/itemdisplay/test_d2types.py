"""
``tests.bh.config.itemdisplay.test_d2types``
============================================

This module contains test code for :py:mod:`d2lfg.bh.config.itemdisplay.filterexpr`.
"""

import pytest

from tests.testhelper.typing import FixtureRequest

from d2lfg.d2core.d2types.playerclass import Diablo2PlayerClasses, Diablo2PlayerClass
from d2lfg.bh.config.itemdisplay.d2types import (
    BHDiablo2ItemType,
    BHDiablo2CurrentPlayerClass,
    BHDiablo2PlayerClassItemRestriction,
    BHDiablo2Item,
)


@pytest.fixture(params=[Diablo2PlayerClasses.AMAZON, Diablo2PlayerClasses.PALADIN])
def player_class(request: FixtureRequest[Diablo2PlayerClass]) -> Diablo2PlayerClass:
    return request.param


@pytest.fixture
def misc_item_type() -> BHDiablo2ItemType:
    """
    A :py:class:`~d2lfg.d2core.d2types.item.Diablo2ItemType` representing
    the "misc" (Miscellaneous) type.
    """
    return BHDiablo2ItemType(
        name="Miscellaneous",
        code="misc",
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
def amulet(misc_item_type: BHDiablo2ItemType) -> BHDiablo2Item:
    """
    A :py:class:`~d2lfg.bh.config.itemdisplay.d2types.BHDiablo2Item`
    for testing.
    """
    return BHDiablo2Item(
        code="amu",
        name="amulet",
        type=misc_item_type,
        type2=None,
        mindam=None,
        maxdam=None,
        f1or2handed=None,
        f2handed=None,
        f2handmindam=None,
        f2handmaxdam=None,
        rangeadder=None,
        speed=None,
        strbonus=None,
        dexbonus=None,
        reqstr=0,
        reqdex=0,
        durability=0,
        nodurability=True,
        level=1,
        levelreq=0,
        cost=2400,
        normcode=None,
        ubercode=None,
        ultracode=None,
        invwidth=1,
        invheight=1,
        stackable=False,
        gemsockets=0,
    )


class TestBHDiablo2Item:
    """
    Tests :py:class:`~d2lfg.bh.config.itemdisplay.d2types.BHDiablo2Item`.
    """

    def test_bhexpr(self, amulet: BHDiablo2Item) -> None:
        """
        Verifies that :py:class:`~d2lfg.bh.config.itemdisplay.d2types.BHDiablo2Item`
        produces the correct filter expression.
        """
        assert amulet.bhexpr() == amulet.code


class TestBHDiablo2CurrentPlayerClass:
    """
    Tests :py:class:`~d2lfg.bh.config.itemdisplay.d2types.BHDiablo2CurrentPlayerClass`.
    """

    def test_bhexpr(self, player_class: Diablo2PlayerClass) -> None:
        """
        Verifies that
        :py:class:`~d2lfg.bh.config.itemdisplay.d2types.BHDiablo2CurrentPlayerClass`
        produces the correct filter expression.
        """
        pc = BHDiablo2CurrentPlayerClass.copy(player_class)

        assert pc.bhexpr() == pc.name


class TestBHDiablo2PlayerClassItemRestriction:
    """
    Tests
    :py:class:`~d2lfg.bh.config.itemdisplay.d2types.BHDiablo2PlayerClassItemRestriction`.
    """

    def test_bhexpr(self, player_class: Diablo2PlayerClass) -> None:
        """
        Verifies that
        :py:class:`~d2lfg.bh.config.itemdisplay.d2types.BHDiablo2PlayerClassItemRestriction`
        produces the correct filter expression.
        """
        pc = BHDiablo2PlayerClassItemRestriction.copy(player_class)

        assert pc.bhexpr() == pc.code
