"""
d2lfl.diablo2.game.skill
========================

This module contains skill type classes.
"""

from dataclasses import dataclass
from typing import Protocol

from .playerclass import Diablo2PlayerClass


class IDiablo2Skill(Protocol):
    id: int
    name: str
    charclass: Diablo2PlayerClass


@dataclass
class Diablo2Skill:
    id: int
    name: str
    charclass: Diablo2PlayerClass

    def _type_check(self) -> IDiablo2Skill:
        """
        Exists only to verify that this class implements `IDiablo2Skill`.
        """
        return self

