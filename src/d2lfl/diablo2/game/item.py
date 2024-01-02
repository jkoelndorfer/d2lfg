"""
d2lfl.diablo2.game.item
=======================

This module contains item type classes.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Diablo2BodyLoc(Enum):
    """
    Represents a Diablo 2 equipment slot.
    """

    BELT = "belt"
    FEET = "feet"
    GLOV = "glov"
    HEAD = "head"
    LARM = "larm"
    LRIN = "lrin"
    NECK = "neck"
    RARM = "rarm"
    RRIN = "rrin"
    TORS = "tors"

    @classmethod
    def from_string(cls, s: str) -> Optional["Diablo2BodyLoc"]:
        return getattr(cls, s.upper(), None)


@dataclass
class Diablo2ItemType:
    """
    Diablo2ItemType defines an item type.

    Item types are defined in ItemTypes.txt.
    """

    name: str
    code: str
    equiv1: Optional[str]
    equiv2: Optional[str]
    bodyloc1: Optional[Diablo2BodyLoc]
    bodyloc2: Optional[Diablo2BodyLoc]


@dataclass
class Diablo2Item:
    """
    Diablo2Item is the base definition for a Diablo 2 item.

    Diablo 2 items are things that exist in your inventory.

    Items include potions, the Horadric Cube, tomes of town
    portal and identify, charms, quest items, and equipment.
    """

    code: str
    item_type: Diablo2ItemType
    item_type2: Optional[Diablo2ItemType]
    name: str
    ilvl: int
    lvl_req: int


@dataclass
class Diablo2Equipment(Diablo2Item):
    """
    Diablo2Equipment is an equippable Diablo2Item.
    """

    max_sockets: int
    max_dur: int
    norm_code: str
    uber_code: str
    ultra_code: str

    @property
    def is_normal(self) -> bool:
        return self.code == self.norm_code

    @property
    def is_exceptional(self) -> bool:
        return self.code == self.uber_code

    @property
    def is_elite(self) -> bool:
        return self.code == self.ultra_code


@dataclass
class Diablo2Armor(Diablo2Equipment):
    """
    Diablo2Armor is Diablo2Equipment that is an armor.
    """

    str_req: int
    min_def: int
    max_def: int


@dataclass
class Diablo2Weapon(Diablo2Equipment):
    """
    Diablo2Weapon is Diablo2Equipment that is a weapon.
    """

    str_req: int
    dex_req: int
