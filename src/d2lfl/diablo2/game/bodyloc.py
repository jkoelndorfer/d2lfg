"""
d2lfl.diablo2.game.bodyloc
==========================

This module contains code defining body locations that
equipment can occupy.
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
    def from_string(cls, s: str) -> Optional["Diablo2BodyLoc"]:
        return getattr(cls, s.upper(), None)
