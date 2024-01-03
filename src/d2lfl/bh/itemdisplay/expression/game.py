"""
d2lfl.bh.itemdisplay.expression.game
====================================

This code defines BH expressions for Diablo 2 game types.
"""

from .expression import BHExpression
from ....diablo2.game import (
    Diablo2Armor,
    Diablo2Equipment,
    Diablo2Item,
    Diablo2PlayerClass,
    Diablo2Weapon,
)


class BHDiablo2ItemExpressionMixin(BHExpression):
    """
    Mix-in class for objects which are both a BHExpression and a Diablo2Item.
    """
    def bhexpr(self) -> str:
        return self.code


class BHDiablo2PlayerClassExpression(BHExpression, Diablo2PlayerClass):
    """
    BHExpression representing a Diablo2PlayerClass.

    This allows for its instances to be used both as BH filter expressions
    and as arguments to Diablo2Database skill lookup methods.
    """
    def bhexpr(self) -> str:
        return self.name.upper()

    @classmethod
    def copyclass(cls, c: Diablo2PlayerClass) -> "BHDiablo2PlayerClassExpression":
        return cls(c.name, c.code)


class BHDiablo2ItemExpression(BHDiablo2ItemExpressionMixin, Diablo2Item):
    """
    BHExpression representing a Diablo2Item.
    """


class BHDiablo2EquipmentExpression(BHDiablo2ItemExpressionMixin, Diablo2Equipment):
    """
    BHExpression representing a Diablo2Equipment.
    """


class BHDiablo2ArmorExpression(BHDiablo2ItemExpressionMixin, Diablo2Armor):
    """
    BHExpression representing a Diablo2Armor.
    """


class BHDiablo2WeaponExpression(BHDiablo2ItemExpressionMixin, Diablo2Weapon):
    """
    BHExpression representing a Diablo2Weapon.
    """
