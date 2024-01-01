"""
d2lfl.d2data.database
=====================

This module contains the definition of a Diablo 2 database.
"""

from abc import ABCMeta, abstractmethod
from pathlib import Path
from typing import Dict

from .dataset import Diablo2TxtDataSet
from .item import Diablo2BodyLoc, Diablo2Item, Diablo2ItemType
from .util import case_insensitive_filepath as cifp


class Diablo2Database(metaclass=ABCMeta):
    @abstractmethod
    def item(self, code: str) -> Diablo2Item:
        pass

    @abstractmethod
    def skill(self, code: int) -> Diablo2Skill:
        pass


class Diablo2TxtDatabase(Diablo2Database):
    """
    A Diablo2Database backed by raw .txt files on the filesystem.
    """

    def __init__(self, txt_dir: Path) -> None:
        """
        Creates a new Diablo2TxtDatabase.

        :param txt_dir: path to directory containing the "data/global/excel" directory
        """
        self.txt_dir = txt_dir
        data_dir = cifp(self.txt_dir, "data")
        global_dir = cifp(data_dir, "global")
        self._excel_dir = cifp(global_dir, "excel")

        self._itemtypes_by_code: Dict[str, Diablo2ItemType] = dict()
        self._items_by_code: Dict[str, Diablo2Item] = dict()

    def _initialize_db(self) -> None:
        self._initialize_item_types()
        return
        armor_file = cifp(self._excel_dir, "armor.txt")
        misc_file = cifp(self._excel_dir, "misc.txt")
        skills_file = cifp(self._excel_dir, "skills.txt")
        weapons_file = cifp(self._excel_dir, "weapons.txt")

    def _initialize_item_types(self) -> None:
        item_type_data = self._load_txt("ItemTypes.txt")
        for r in item_type_data:
            self._itemtypes_by_code[r["Code"]] = Diablo2ItemType(
                name=r["ItemType"],
                code=r["Code"],
                equiv1=r["Equiv1"],
                equiv2=r["Equiv2"],
                bodyloc1=Diablo2BodyLoc.from_string(r["BodyLoc1"]),
                bodyloc2=Diablo2BodyLoc.from_string(r["BodyLoc2"]),
            )

    def _load_txt(self, filename: str) -> Diablo2TxtDataSet:
        return Diablo2TxtDataSet(cifp(self._excel_dir, filename))
