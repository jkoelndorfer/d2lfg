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


class IDiablo2SkillTab(Protocol):
    id: int
    name: str
    charclass: Diablo2PlayerClass


class IDiablo2CharacterSkillTabs(Protocol):
    AMAZON: IDiablo2SkillTab
    SORCERESS: IDiablo2SkillTab
    NECROMANCER: IDiablo2SkillTab
    PALADIN: IDiablo2SkillTab
    BARBARIAN: IDiablo2SkillTab
    DRUID: IDiablo2SkillTab
    ASSASSIN: IDiablo2SkillTab


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


@dataclass
class Diablo2SkillTab:
    id: int
    name: str
    charclass: Diablo2PlayerClass

    def _type_check(self) -> IDiablo2SkillTab:
        """
        Exists only to verify that this class implements `IDiablo2SkillTab`.
        """
        return self
