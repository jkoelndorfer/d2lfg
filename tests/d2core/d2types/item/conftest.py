import pytest

from d2lfg.d2core.d2types.bodyloc import Diablo2BodyLoc, Diablo2BodyLocs
from d2lfg.d2core.d2types.item import Diablo2Item, Diablo2ItemType
from d2lfg.d2core.d2types.playerclass import Diablo2PlayerClass

ItemType = Diablo2ItemType[Diablo2BodyLoc, Diablo2PlayerClass]
Item = Diablo2Item[ItemType]


@pytest.fixture
def weap_item_type() -> ItemType:
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
def gen_item_type() -> ItemType:
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
def mele_item_type(weap_item_type: ItemType) -> ItemType:
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
def mgen_item_type(gen_item_type: ItemType, mele_item_type: ItemType) -> ItemType:
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
def axe_item_type(mgen_item_type: ItemType) -> ItemType:
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


@pytest.fixture
def axe_item(axe_item_type: ItemType) -> Item:
    """
    A :py:class:`d2lfg.d2core.d2types.item.Diablo2Item` representing the
    ``axe`` item. This item is modeled after actual data taken from
    ``Weapons.txt``.
    """
    return Diablo2Item(
        code="axe",
        name="Axe",
        type=axe_item_type,
        type2=None,
        mindam=4,
        maxdam=11,
        f1or2handed=None,
        f2handed=None,
        f2handmindam=None,
        f2handmaxdam=None,
        rangeadder=2,
        speed=10,
        strbonus=100,
        dexbonus=None,
        reqstr=32,
        reqdex=0,
        durability=48,
        nodurability=False,
        level=7,
        levelreq=0,
        cost=403,
        normcode="axe",
        ubercode="9ax",
        ultracode="7ax",
        invwidth=2,
        invheight=3,
        stackable=False,
        gemsockets=4,
    )


@pytest.fixture
def cleaver_item(axe_item_type: ItemType) -> Item:
    """
    A :py:class:`d2lfg.d2core.d2types.item.Diablo2Item` representing the
    ``9ax`` (Cleaver) item. This item is modeled after actual data taken
    from ``Weapons.txt``.
    """
    return Diablo2Item(
        code="9ax",
        name="Cleaver",
        type=axe_item_type,
        type2=None,
        mindam=14,
        maxdam=47,
        f1or2handed=None,
        f2handed=None,
        f2handmindam=None,
        f2handmaxdam=None,
        rangeadder=2,
        speed=10,
        strbonus=100,
        dexbonus=None,
        reqstr=68,
        reqdex=0,
        durability=48,
        nodurability=False,
        level=34,
        levelreq=22,
        cost=1509,
        normcode="axe",
        ubercode="9ax",
        ultracode="7ax",
        invwidth=2,
        invheight=3,
        stackable=False,
        gemsockets=4,
    )


@pytest.fixture
def small_crescent_item(axe_item_type: ItemType) -> Item:
    """
    A :py:class:`d2lfg.d2core.d2types.item.Diablo2Item` representing the
    ``7ax`` (Small Crescent) item. This item is modeled after actual data
    taken from ``Weapons.txt``.
    """
    return Diablo2Item(
        code="7ax",
        name="Cleaver",
        type=axe_item_type,
        type2=None,
        mindam=47,
        maxdam=75,
        f1or2handed=None,
        f2handed=None,
        f2handmindam=None,
        f2handmaxdam=None,
        rangeadder=2,
        speed=10,
        strbonus=100,
        dexbonus=None,
        reqstr=115,
        reqdex=0,
        durability=72,
        nodurability=False,
        level=61,
        levelreq=45,
        cost=15781,
        normcode="axe",
        ubercode="9ax",
        ultracode="7ax",
        invwidth=2,
        invheight=3,
        stackable=False,
        gemsockets=4,
    )


@pytest.fixture
def misc_item_type() -> ItemType:
    """
    A :py:class:`d2lfg.d2core.d2types.item.Diablo2ItemType` representing
    the "misc" (Miscellaneous) type.
    """
    return Diablo2ItemType(
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
def amul_item_type(misc_item_type: ItemType) -> ItemType:
    """
    A :py:class:`d2lfg.d2core.d2types.item.Diablo2ItemType` representing
    the "amul" (Amulet) type.
    """
    return Diablo2ItemType(
        name="Amulet",
        code="amul",
        equiv1=misc_item_type,
        equiv2=None,
        body=True,
        bodyloc1=Diablo2BodyLocs.NECK,
        bodyloc2=Diablo2BodyLocs.NECK,
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
def amulet_item(amul_item_type: ItemType) -> Item:
    """
    A :py:class:`d2lfg.d2core.d2types.item.Diablo2Item` representing an
    ``amu`` (amulet). This item is modeled after actual data from Misc.txt.
    """
    return Diablo2Item(
        code="amu",
        name="amulet",
        type=amul_item_type,
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
