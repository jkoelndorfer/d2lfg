"""
``d2lfg.d2core.d2types.bodyloc``
================================

This module contains the model for a Diablo 2 body location.
"""

from dataclasses import dataclass
from typing import Type

from ...util import Diablo2Collection


@dataclass
class Diablo2BodyLoc:
    """
    Represents a Diablo 2 body location (i.e. equipment slot).

    :param name: the name of the body location
    :param code: the code used to reference the body location
    """

    name: str
    code: str

    def __hash__(self) -> int:
        return hash(f"{self.name}.{self.code}")


class Diablo2BodyLocs(Diablo2Collection[Diablo2BodyLoc]):
    """
    Collection of all valid :py:class:`Diablo2BodyLoc` objects.

    Body locations are defined in ``BodyLocs.txt``.
    """

    #: The head body location. Helms are equipped here.
    HEAD = Diablo2BodyLoc("Head", "head")

    #: The neck body location. Amulets are equipped here.
    NECK = Diablo2BodyLoc("Neck", "neck")

    #: The torso body location. Chest armor is equipped here.
    TORS = TORSO = Diablo2BodyLoc("Torso", "tors")

    #: The right arm body location. Weapons and offhands are equipped here.
    RARM = RIGHT_ARM = Diablo2BodyLoc("Right Arm", "rarm")

    #: The left arm body location. Weapons and offhands are equipped here.
    LARM = LEFT_ARM = Diablo2BodyLoc("Left Arm", "larm")

    #: The right ring location. Rings are equipped here.
    RRIN = RIGHT_RING = Diablo2BodyLoc("Right Ring", "rrin")

    #: The left ring location. Rings are equipped here.
    LRIN = LEFT_RING = Diablo2BodyLoc("Left Ring", "lrin")

    #: The belt location. Belts are equipped here.
    BELT = Diablo2BodyLoc("Belt", "belt")

    #: The feet location. Boots are equipped here.
    FEET = Diablo2BodyLoc("Feet", "feet")

    #: The gloves location. Gloves are equipped here.
    GLOV = GLOVES = Diablo2BodyLoc("Gloves", "glov")

    @classmethod
    def collection_type(cls) -> Type[Diablo2BodyLoc]:
        return Diablo2BodyLoc
