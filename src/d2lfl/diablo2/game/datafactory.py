"""
d2lfl.diablo2.game.datafactory
==============================

This module contains code to create game data objects.
"""

from abc import ABCMeta, abstractmethod
from typing import Optional, Type

from .item import Diablo2Armor, Diablo2Equipment, Diablo2Item, Diablo2ItemType, Diablo2Weapon
from .playerclass import Diablo2PlayerClass
from .skill import Diablo2Skill


class Diablo2DataFactory(metaclass=ABCMeta):
    @abstractmethod
    def item(
        self,
        code: str,
        item_type: Diablo2ItemType,
        item_type2: Optional[Diablo2ItemType],
        name: str,
        ilvl: int,
        lvl_req: int,
    ) -> Diablo2Item:
        """
        Creates a new Diablo2Item.
        """

    @abstractmethod
    def equipment(
        self,
        code: str,
        item_type: Diablo2ItemType,
        item_type2: Optional[Diablo2ItemType],
        name: str,
        ilvl: int,
        lvl_req: int,
        max_sockets: int,
        max_dur: int,
        norm_code: str,
        uber_code: str,
        ultra_code: str,
    ) -> Diablo2Equipment:
        """
        Creates a new Diablo2Equipment.
        """

    @abstractmethod
    def armor(
        self,
        code: str,
        item_type: Diablo2ItemType,
        item_type2: Optional[Diablo2ItemType],
        name: str,
        ilvl: int,
        lvl_req: int,
        max_sockets: int,
        max_dur: int,
        norm_code: str,
        uber_code: str,
        ultra_code: str,
        str_req: int,
        min_def: int,
        max_def: int,
    ) -> Diablo2Armor:
        """
        Creates a new Diablo2Armor.
        """

    @abstractmethod
    def weapon(
        self,
        code: str,
        item_type: Diablo2ItemType,
        item_type2: Optional[Diablo2ItemType],
        name: str,
        ilvl: int,
        lvl_req: int,
        max_sockets: int,
        max_dur: int,
        norm_code: str,
        uber_code: str,
        ultra_code: str,
        str_req: int,
        dex_req: int,
    ) -> Diablo2Weapon:
        """
        Creates a new Diablo2Weapon.
        """

    @abstractmethod
    def skill(self, id: int, name: str, charclass: Diablo2PlayerClass) -> Diablo2Skill:
        """
        Creates a new Diablo2Skill.
        """


class TypeConfigurableDiablo2DataFactory(Diablo2DataFactory):
    def __init__(
        self,
        armor_type: Type[Diablo2Armor],
        item_type: Type[Diablo2Item],
        equipment_type: Type[Diablo2Equipment],
        weapon_type: Type[Diablo2Weapon],
        skill_type: Type[Diablo2Skill],
    ) -> None:
        self.armor_type = armor_type
        self.item_type = item_type
        self.equipment_type = equipment_type
        self.weapon_type = weapon_type
        self.skill_type = skill_type

    def item(
        self,
        code: str,
        item_type: Diablo2ItemType,
        item_type2: Optional[Diablo2ItemType],
        name: str,
        ilvl: int,
        lvl_req: int,
    ) -> Diablo2Item:
        """
        Creates a new Diablo2Item.
        """
        return self.item_type(code, item_type, item_type2, name, ilvl, lvl_req)

    def equipment(
        self,
        code: str,
        item_type: Diablo2ItemType,
        item_type2: Optional[Diablo2ItemType],
        name: str,
        ilvl: int,
        lvl_req: int,
        max_sockets: int,
        max_dur: int,
        norm_code: str,
        uber_code: str,
        ultra_code: str,
    ) -> Diablo2Equipment:
        """
        Creates a new Diablo2Equipment.
        """
        return self.equipment_type(
            code,
            item_type,
            item_type2,
            name,
            ilvl,
            lvl_req,
            max_sockets,
            max_dur,
            norm_code,
            uber_code,
            ultra_code,
        )

    def armor(
        self,
        code: str,
        item_type: Diablo2ItemType,
        item_type2: Optional[Diablo2ItemType],
        name: str,
        ilvl: int,
        lvl_req: int,
        max_sockets: int,
        max_dur: int,
        norm_code: str,
        uber_code: str,
        ultra_code: str,
        str_req: int,
        min_def: int,
        max_def: int,
    ) -> Diablo2Armor:
        """
        Creates a new Diablo2Armor.
        """
        return self.armor_type(
            code,
            item_type,
            item_type2,
            name,
            ilvl,
            lvl_req,
            max_sockets,
            max_dur,
            norm_code,
            uber_code,
            ultra_code,
            str_req,
            min_def,
            max_def,
        )

    def weapon(
        self,
        code: str,
        item_type: Diablo2ItemType,
        item_type2: Optional[Diablo2ItemType],
        name: str,
        ilvl: int,
        lvl_req: int,
        max_sockets: int,
        max_dur: int,
        norm_code: str,
        uber_code: str,
        ultra_code: str,
        str_req: int,
        dex_req: int,
    ) -> Diablo2Weapon:
        """
        Creates a new Diablo2Weapon.
        """
        return self.weapon_type(
            code,
            item_type,
            item_type2,
            name,
            ilvl,
            lvl_req,
            max_sockets,
            max_dur,
            norm_code,
            uber_code,
            ultra_code,
            str_req,
            dex_req,
        )

    def skill(self, id: int, name: str, charclass: Diablo2PlayerClass) -> Diablo2Skill:
        """
        Creates a new Diablo2Skill.
        """
        return self.skill_type(id, name, charclass)
