"""
d2lfl.bh.itemdisplay.database
=============================

This module contains a database wrapper class which
converts Diablo 2 game types into BH expressions.
"""

from ...diablo2.data import Diablo2Database
from .expression.game import (
    BHDiablo2EquipmentExpression as Equipment,
    BHDiablo2ItemExpression as Item,
    BHDiablo2ArmorExpression as Armor,
    BHDiablo2WeaponExpression as Weapon,
)
from .codetype import (
    BHSkill as Skill
)


class BHDiablo2Database(Diablo2Database):
    def __init__(self, source_db: Diablo2Database) -> None:
        self.source_db = source_db

    def armor(self, code: str) -> Armor:
        """
        Returns a Diablo2Armor with the given `code`.
        """
        return Armor(self.source_db.armor(code))
