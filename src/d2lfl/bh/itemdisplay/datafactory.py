"""
d2lfl.bh.itemdisplay.datafactory
================================

This module contains a data factory that converts
standard Diablo 2 game types into BH maphack expression
and code types.
"""

from ...diablo2.data import TypeConfigurableDiablo2DataFactory
from .expression.game import (
    BHDiablo2EquipmentExpression,
    BHDiablo2ItemExpression,
    BHDiablo2ArmorExpression,
    BHDiablo2WeaponExpression,
)
from .codetype import BHSkill


bh_data_factory = TypeConfigurableDiablo2DataFactory(
    armor_type=BHDiablo2ArmorExpression,
    item_type=BHDiablo2ItemExpression,
    equipment_type=BHDiablo2EquipmentExpression,
    weapon_type=BHDiablo2WeaponExpression,
    skill_type=BHSkill,
)
