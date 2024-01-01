"""
d2lfl.diablo2.game.item
=======================

This module contains item type classes.
"""

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
    def from_string(cls, s: str) -> "Diablo2BodyLoc":
        return getattr(cls, s.upper())


class Diablo2ItemType:
    """
    Diablo2ItemType defines an item type.

    Item types are defined in ItemTypes.txt.
    """
    def __init__(
        self,
        name: str,
        code: str,
        equiv1: Optional[str],
        equiv2: Optional[str],
        bodyloc1: Optional[Diablo2BodyLoc],
        bodyloc2: Optional[Diablo2BodyLoc],
    ) -> None:
        self.name = name
        self.item_type = name

        self.code = code
        self.equiv1 = equiv1
        self.equiv2 = equiv2

        self.bodyloc1 = bodyloc1
        self.bodyloc2 = bodyloc2


class Diablo2Item:
    """
    Diablo2Item is the base definition for a Diablo 2 item.

    Diablo 2 items are things that exist in your inventory.

    Items include potions, the Horadric Cube, tomes of town
    portal and identify, charms, quest items, and equipment.
    """
    def __init__(self, code: str, item_type: Diablo2ItemType, name: str, item_lvl: int, lvl_req: int) -> None:
        self.code = code
        self.item_type = item_type
        self.name = name
        self.item_lvl = item_lvl
        self.lvl_req = lvl_req


class Diablo2Equipment(Diablo2Item):
    """
    Diablo2Equipment is an equippable Diablo2Item.
    """
    def __init__(
        self,
        code: str,
        item_type: Diablo2ItemType,
        name: str,
        item_lvl: int,
        lvl_req: int,
        max_dur: int,
        norm_code: str,
        uber_code: str,
        ultra_code: str,
    ) -> None:
        super().__init__(code, item_type, name, item_lvl, lvl_req)
        self.max_dur = max_dur
        self.norm_code = norm_code
        self.uber_code = uber_code
        self.ultra_code = ultra_code


class Diablo2Armor(Diablo2Equipment):
    """
    Diablo2Armor is Diablo2Equipment that is an armor.
    """
    def __init__(
        self,
        code: str,
        item_type: Diablo2ItemType,
        name: str,
        item_lvl: int,
        lvl_req: int,
        max_dur: int,
        norm_code: str,
        uber_code: str,
        ultra_code: str,
        str_req: int,
        min_def: int,
        max_def: int,
    ) -> None:
        super().__init__(
            code, item_type, name, item_lvl, lvl_req, max_dur, norm_code, uber_code, ultra_code
        )
        self.str_req = str_req
        self.min_def = min_def
        self.max_def = max_def


class Diablo2Weapon(Diablo2Equipment):
    """
    Diablo2Weapon is Diablo2Equipment that is a weapon.
    """
    def __init__(
        self,
        code: str,
        item_type: Diablo2ItemType,
        name: str,
        item_lvl: int,
        lvl_req: int,
        max_dur: int,
        norm_code: str,
        uber_code: str,
        ultra_code: str,
        str_req: int,
        dex_req: int,
    ) -> None:
        super().__init__(
            code,
            item_type,
            name,
            item_lvl,
            lvl_req,
            max_dur,
            norm_code,
            uber_code,
            ultra_code,
        )
        self.str_req = str_req
        self.dex_req = dex_req
