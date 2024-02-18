"""
``d2lfg.d2core.d2types.item``
=============================

This module contains models for Diablo 2 item types.
"""

from dataclasses import dataclass
from typing import List, Generator, Generic, Optional, Self, Type, TypeVar

from ...util.d2collection import Diablo2Collection
from .bodyloc import Diablo2BodyLoc
from .playerclass import Diablo2PlayerClass


BodyLoc = TypeVar("BodyLoc", bound=Diablo2BodyLoc, covariant=True)
ItemType = TypeVar(
    "ItemType",
    bound="Diablo2ItemType[Diablo2BodyLoc, Diablo2PlayerClass]",
)
PlayerClass = TypeVar("PlayerClass", bound=Diablo2PlayerClass, covariant=True)


@dataclass
class Diablo2ItemType(Generic[BodyLoc, PlayerClass]):
    """
    Represents a Diablo 2 item type.

    Item types are defined in ``ItemTypes.txt``.

    See also the
    `Phrozen Keep ItemTypes.txt Guide <https://d2mods.info/forum/viewtopic.php?t=34876>`_.
    """

    #: The name of the item type.
    name: str

    #: The code associated with the item type.
    code: str

    #: One of the parent item types.
    equiv1: Optional[Self]

    #: One of the parent item types.
    equiv2: Optional[Self]

    #: Whether the item type can be equipped or not.
    body: bool

    #: One of the body locations where the item type can be equipped.
    bodyloc1: Optional[BodyLoc]

    #: One of the body locations where the item type can be equipped.
    bodyloc2: Optional[BodyLoc]

    #: The ammunition for this item type. For example, items with type
    #: "bow" use "bowq" (bow quiver) item types as ammunition.
    shoots: Optional[Self]

    #: The item type that consumes this item type as ammunition.
    #: For example, items with type "bowq" (bow quiver) are used
    #: by "bow" item types.
    quiver: Optional[Self]

    #: Whether the item type is throwable.
    throwable: bool

    #: Whether this item can have its quantity increased by dragging-and-dropping
    #: more of the same item on top.
    reload: bool

    #: Whether this item type will be re-equipped automatically from
    #: a picked up drop when ammunition runs out.
    reequip: bool

    #: Whether identical stacks of an item are automatically combined
    #: on pickup.
    autostack: bool

    #: Whether this item can be placed into sockets.
    gem: bool

    #: Whether this item can be placed into the player's belt.
    beltable: bool

    #: The maximum number of sockets this item can have from
    #: item level 1 to 24.
    maxsock1: int

    #: The maximum number of sockets this item can have from
    #: item level 25 to 39.
    maxsock25: int

    #: The maximum number of sockets this item can have over
    #: item level 40.
    maxsock40: int

    #: The character class that will receive +skill bonuses
    #: from this item type.
    staffmods: Optional[PlayerClass]

    #: The character class that can use this item type.
    #: NOTE: ``class`` is a reserved Python keyword and
    #: not usable here.
    class_: Optional[PlayerClass]

    #: The code of the store page that this item type will appear
    #: on when sold.
    storepage: Optional[str]

    def all_types(self) -> Generator[Self, None, None]:
        """
        Yields all of this item's types recursively.

        For example, the "axe" type also has type "mgen", which
        in turn has types "mele" and "gen". "mele" has type "weap".
        This method would yield all five types.
        """
        stack: List[Optional[Self]] = list()
        stack.append(self)
        while len(stack) > 0:
            current_type = stack.pop()
            if current_type is None:
                continue
            yield current_type
            stack.append(current_type.equiv1)
            stack.append(current_type.equiv2)

    def equippable(self: ItemType) -> bool:
        """
        Returns ``True`` if this item is equippable, ``False`` otherwise.
        """
        return any(it.body for it in self.all_types())


@dataclass
class Diablo2ItemTier:
    """
    Represents a Diablo 2 item tier.
    """

    #: The name of the item tier.
    name: str

    #: The code of the item tier (i.e. how it is referred to in .txt file columns).
    code: str

    def __hash__(self) -> int:
        return hash(f"{self.name}{self.code}")


class Diablo2ItemTiers(Diablo2Collection[Diablo2ItemTier]):
    """
    A collection describing the item tiers an item can have.
    """

    NORM = NORMAL = Diablo2ItemTier("normal", "norm")
    UBER = EXCEPTIONAL = Diablo2ItemTier("exceptional", "uber")
    ULTRA = ELITE = Diablo2ItemTier("elite", "ultra")

    @classmethod
    def collection_type(cls) -> Type[Diablo2ItemTier]:
        return Diablo2ItemTier


@dataclass
class Diablo2Item(Generic[ItemType]):
    """
    Represents a Diablo 2 item.

    Items are defined in ``Armor.txt``, ``Misc.txt``, or ``Weapons.txt``. The fields on
    this class are named the same as the fields in those files. If a field from the
    text file starts with an integer, it is prefixed by "f", since attributes that
    start with an integer are not allowed in Python.

    While all fields on this object do not appear in every aforementioned text file,
    Diablo 2 treats ``Armor.txt``, ``Misc.txt``, and ``Weapons.txt`` interchangeably. So
    we model this class after that behavior. From the ``Misc.txt`` guide:

        Armor.txt ,Misc.txt and Weapons.txt have many identical columns. That's because
        in fact these 3 text files are, in truth, three parts of a single big file :
        when the game reads these 3 tables, it merges them all, one after another, into
        one and unique table.

    See also:
    * `Phrozen Keep Armor.txt Guide <https://d2mods.info/forum/kb/viewarticle?a=2>`_.
    * `Phrozen Keep Misc.txt Guide <https://d2mods.info/forum/kb/viewarticle?a=317>`_.
    * `Phrozen Keep Weapons.txt Guide <https://d2mods.info/forum/kb/viewarticle?a=346>`_.
    """

    #: The code associated with the item. The code is an ID used to reference the item
    # elsewhere.
    code: str

    #: The name of the item as it appears in the txt files.
    #: This is *not the localized name and may not be what appears in game.*
    name: str

    #: One of the item's types.
    type: ItemType

    #: One of the item's types.
    type2: Optional[ItemType]

    #: The minimum damage that a weapon can do.
    mindam: Optional[int]

    #: The maximum damage that a weapon can do.
    maxdam: Optional[int]

    #: Indicates an item may be wielded one or two handed by a Barbarian.
    f1or2handed: Optional[bool]

    #: Whether the weapon is two handed.
    f2handed: Optional[bool]

    #: The minimum damage a weapon does when wielded two handed.
    f2handmindam: Optional[int]

    #: The maximum damage a weapon does when wielded two handed.
    f2handmaxdam: Optional[int]

    #: The range of a melee weapon, with 1 equivalent to bare-handed range.
    rangeadder: Optional[int]

    #: The speed modifier for a weapon (lower values are faster).
    speed: Optional[int]

    #: Strength required to improve weapon damage.
    strbonus: Optional[int]

    #: Dexterity required to improve weapon damage.
    dexbonus: Optional[int]

    #: Strength required to use the item.
    reqstr: int

    #: Dexterity required to use the item.
    reqdex: int

    #: The maximum durability of the item.
    durability: int

    #: If True, this item does not have durability.
    nodurability: bool

    #: The base item level of the item.
    level: int

    #: The level requirement to use the item.
    levelreq: int

    #: The base cost of the item.
    cost: int

    #: The code of the normal-tier variant of this item.
    normcode: Optional[str]

    #: The code of the exceptional-tier variant of this item.
    ubercode: Optional[str]

    #: The code of the elite-tier variant of this item.
    ultracode: Optional[str]

    #: The width of this item in the inventory.
    invwidth: int

    #: The height of this item in the inventory.
    invheight: int

    #: Whether the item is stackable.
    stackable: bool

    #: The maximum number of sockets the item can have.
    gemsockets: int

    def equippable(self) -> bool:
        """
        Returns ``True`` if the item is equippable, ``False`` otherwise.
        """
        return self.type.equippable() or (
            self.type2 is not None and self.type2.equippable()
        )

    @property
    def tier(self) -> Diablo2ItemTier:
        """
        Returns the item tier of this item: one of normal, exceptional, or elite.
        """
        if self.code == self.normcode:
            return Diablo2ItemTiers.NORMAL
        elif self.code == self.ubercode:
            return Diablo2ItemTiers.EXCEPTIONAL
        elif self.code == self.ultracode:
            return Diablo2ItemTiers.ELITE

        # TODO: Items in Misc.txt do not have normcode, ubercode, or ultracode
        # specified. Are they considered "normal" tier or do they not have a
        # tier?
        return Diablo2ItemTiers.NORMAL
