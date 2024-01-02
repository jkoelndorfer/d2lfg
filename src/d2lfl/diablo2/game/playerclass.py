"""
d2lfl.diablo2.game.playerclass
==============================

This module defines Diablo 2 player classes.
"""

from dataclasses import dataclass
from enum import Enum


@dataclass
class Diablo2PlayerClass:
    name: str
    code: str


class Diablo2PlayerClasses(Enum):
    AMA = AMAZON = Diablo2PlayerClass("Amazon", "ama")
    ASS = ASSASSIN = Diablo2PlayerClass("Assassin", "ass")
    BAR = BARBARIAN = Diablo2PlayerClass("Barbarian", "bar")
    DRU = DRUID = Diablo2PlayerClass("Druid", "dru")
    NEC = NECROMANCER = Diablo2PlayerClass("Necromancer", "nec")
    PAL = PALADIN = Diablo2PlayerClass("Paladin", "pal")
    SOR = SORCERESS = Diablo2PlayerClass("Sorceress", "sor")
