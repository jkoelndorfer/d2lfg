"""
d2lfl.diablo2.game.skill
========================

This module contains skill type classes.
"""

from dataclasses import dataclass

from .playerclass import Diablo2PlayerClass


@dataclass
class Diablo2Skill:
    id: int
    name: str
    charclass: Diablo2PlayerClass
