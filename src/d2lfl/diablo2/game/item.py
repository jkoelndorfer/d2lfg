"""
d2lfl.diablo2.game.item
=======================

This module contains item type classes.
"""

from abc import abstractproperty
from dataclasses import dataclass
from typing import Optional, Protocol

from .bodyloc import Diablo2BodyLoc


class IDiablo2ItemType(Protocol):
    name: str
    code: str
    equiv1: Optional[str]
    equiv2: Optional[str]
    bodyloc1: Optional[Diablo2BodyLoc]
    bodyloc2: Optional[Diablo2BodyLoc]


class IDiablo2Item(Protocol):
    code: str
    item_type: IDiablo2ItemType
    item_type2: Optional[IDiablo2ItemType]
    name: str
    ilvl: int
    lvl_req: int


class IDiablo2Equipment(IDiablo2Item, Protocol):
    max_sockets: int
    max_dur: int
    norm_code: str
    uber_code: str
    ultra_code: str

    @abstractproperty
    def is_normal(self) -> bool:
        """
        If the item is normal tier, returns True. Otherwise, returns False.
        """
        raise NotImplementedError()

    @abstractproperty
    def is_exceptional(self) -> bool:
        """
        If the item is exceptional tier, returns True. Otherwise, returns False.
        """
        raise NotImplementedError()

    @property
    def is_elite(self) -> bool:
        """
        If the item is elite tier, returns True. Otherwise, returns False.
        """
        raise NotImplementedError()


class IDiablo2Armor(IDiablo2Equipment, Protocol):
    #: The minimum defense that the armor can roll.
    minac: int

    #: The maximum defense that the armor can roll.
    maxac: int

    #: The strength requirement for the armor.
    reqstr: int

    @abstractproperty
    def min_def(self) -> int:
        """
        An alias for `minac`.
        """
        raise NotImplementedError()

    @abstractproperty
    def max_def(self) -> int:
        """
        An alias for `maxac`.
        """
        raise NotImplementedError()

    @abstractproperty
    def str_req(self) -> int:
        """
        An alias `reqstr`.
        """
        raise NotImplementedError()


class IDiablo2Weapon(IDiablo2Equipment, Protocol):
    #: The strength requirement of the weapon.
    reqstr: int

    #: The dexterity requirement of the weapon.
    reqdex: int

    @abstractproperty
    def str_req(self) -> int:
        """
        An alias `reqstr`.
        """
        raise NotImplementedError()

    @abstractproperty
    def dex_req(self) -> int:
        """
        An alias `reqdex`.
        """
        raise NotImplementedError()


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

    def _type_check(self) -> IDiablo2ItemType:
        """
        Exists only to verify that this class implements `IDiablo2ItemType`.
        """
        return self


@dataclass
class Diablo2Item:
    """
    Diablo2Item is the base definition for a Diablo 2 item.

    Diablo 2 items are things that exist in your inventory.

    Items include potions, the Horadric Cube, tomes of town
    portal and identify, charms, quest items, and equipment.
    """

    code: str
    item_type: IDiablo2ItemType
    item_type2: Optional[IDiablo2ItemType]
    name: str
    ilvl: int
    lvl_req: int

    def _type_check(self) -> IDiablo2Item:
        """
        Exists only to verify that this class implements `IDiablo2Item`.
        """
        return self


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

    def _type_check(self) -> IDiablo2Equipment:
        """
        Exists only to verify that this class implements `IDiablo2Equipment`.
        """
        return self


@dataclass
class Diablo2Armor(Diablo2Equipment):
    """
    Diablo2Armor is Diablo2Equipment that is an armor.
    """
    minac: int
    maxac: int
    reqstr: int

    @property
    def min_def(self) -> int:
        return self.minac

    @property
    def max_def(self) -> int:
        return self.maxac

    @property
    def str_req(self) -> int:
        return self.reqstr

    def _type_check(self) -> IDiablo2Armor:
        """
        Exists only to verify that this class implements `IDiablo2Armor`.
        """
        return self



@dataclass
class Diablo2Weapon(Diablo2Equipment):
    """
    Diablo2Weapon is Diablo2Equipment that is a weapon.
    """

    reqstr: int
    reqdex: int

    @property
    def str_req(self) -> int:
        """
        An alias `reqstr`.
        """
        return self.reqstr

    @property
    def dex_req(self) -> int:
        """
        An alias `reqdex`.
        """
        return self.reqdex

    def _type_check(self) -> IDiablo2Weapon:
        """
        Exists only to verify that this class implements `IDiablo2Weapon`.
        """
        return self
