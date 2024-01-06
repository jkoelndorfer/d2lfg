"""
``d2lfg.d2core.d2types.item``
=============================

This module contains models for Diablo 2 item types.
"""

from dataclasses import dataclass
from typing import Optional

from .bodyloc import Diablo2BodyLoc


@dataclass
class Diablo2ItemType:
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
    equiv1: Optional["Diablo2ItemType"]

    #: One of the parent item types.
    equiv2: Optional["Diablo2ItemType"]

    #: Whether the item type can be equipped or not.
    body: bool

    #: One of the body locations where the item type can be equipped.
    bodyloc1: Optional[Diablo2BodyLoc]

    #: One of the body locations where the item type can be equipped.
    bodyloc2: Optional[Diablo2BodyLoc]

    #: The ammunition for this item type. For example, items with type
    #: "bow" use "bowq" (bow quiver) item types as ammunition.
    shoots: Optional["Diablo2ItemType"]

    #: The item type that consumes this item type as ammunition.
    #: For example, items with type "bowq" (bow quiver) are used
    #: by "bow" item types.
    quiver: Optional["Diablo2ItemType"]

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
    staffmods: None  # TODO Diablo2PlayerClass

    #: The character class that can use this item type.
    #: NOTE: ``class`` is a reserved Python keyword and
    #: not usable here.
    class_: None  # TODO Diablo2PlayerClass

    #: The code of the store page that this item type will appear
    #: on when sold.
    storepage: str


@dataclass
class Diablo2Item:
    """
    Represents a Diablo 2 item.

    Items are defined in ``Armor.txt``, ``Misc.txt``, or ``Weapons.txt``. The fields on
    this class are named the same as the fields in those files. If a field from the
    text file starts with an integer, it is prefixed by "f", since attributes that
    start with an integer are not allowed in Python.

    While all fields on this object do not appear in every aforementioned text file,
    Diablo 2 treats ``Armor.txt``, ``Misc.txt``, and ``Weapons.txt`` interchangeably. So
    we model this class after that behavior. From the ``Misc.txt`` guide:

    > Armor.txt ,Misc.txt and Weapons.txt have many identical columns. That's because in
    > fact these 3 text files are, in truth, three parts of a single big file : when the
    > game reads these 3 tables, it merges them all, one after another, into one and
    > unique table.

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
    type: Diablo2ItemType

    #: One of the item's types.
    type2: Optional[Diablo2ItemType]

    #: The minimum damage that a weapon can do.
    mindam: int | None

    #: The maximum damage that a weapon can do.
    maxdam: int | None

    #: Indicates an item may be wielded one or two handed by a Barbarian.
    f1or2handed: bool

    #: Whether the weapon is two handed.
    f2handed: bool

    #: The minimum damage a weapon does when wielded two handed.
    f2handmindam: int | None

    #: The maximum damage a weapon does when wielded two handed.
    f2handmaxdam: int | None

    #: The range of a melee weapon, with 1 equivalent to bare-handed range.
    rangeadder: int | None

    #: The speed modifier for a weapon (lower values are faster).
    speed: int | None

    #: If True, this item does not have durability.
    nodurability: bool

    #: Strength required to improve weapon damage.
    strbonus: int | None

    #: Dexterity required to improve weapon damage.
    dexbonus: int | None

    #: The maximum durability of the item.
    durability: int

    #: The base item level of the item.
    level: int

    #: The level requirement to use the item.
    levelreq: int

    #: The base cost of the item.
    cost: int

    #: The code of the normal-tier variant of this item.
    normcode: str | None

    #: The code of the exceptional-tier variant of this item.
    ubercode: str | None

    #: The code of the elite-tier variant of this item.
    ultracode: str | None

    #: The width of this item in the inventory.
    invwidth: int

    #: The height of this item in the inventory.
    invheight: int

    #: The maximum number of sockets the item can have.
    gemsockets: int

    @property
    def equippable(self) -> bool:
        """
        Returns ``True`` if the item is equippable, ``False`` otherwise.
        """
        return self.type.body or (self.type2 is not None and self.type2.body)

    @property
    def is_normal(self) -> bool:
        """
        ``True`` if the item is of normal tier, ``False`` otherwise.
        """
        return self.code == self.normcode

    @property
    def is_exceptional(self) -> bool:
        """
        ``True`` if the item is of exceptional tier, ``False`` otherwise.
        """
        return self.code == self.ubercode

    @property
    def is_elite(self) -> bool:
        """
        ``True`` if the item is of elite tier, ``False`` otherwise.
        """
        return self.code == self.ultracode
