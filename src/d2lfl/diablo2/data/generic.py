"""
d2lfl.diablo2.data.generic
==========================

This module contains generics for Diablo 2 object types.
"""

from typing import TypeVar, Union

from ..game.item import IDiablo2Armor, IDiablo2Equipment, IDiablo2Item, IDiablo2Weapon
from ..game.skill import IDiablo2Skill, IDiablo2CharacterSkillTabs, IDiablo2SkillTab

IT = TypeVar("IT", bound=IDiablo2Item)
AT = TypeVar("AT", bound=IDiablo2Armor)
CST = TypeVar("CST", bound=IDiablo2CharacterSkillTabs)
ET = TypeVar("ET", bound=IDiablo2Equipment)
ST = TypeVar("ST", bound=IDiablo2Skill)
STT = TypeVar("STT", bound=IDiablo2SkillTab)
WT = TypeVar("WT", bound=IDiablo2Weapon)

AnyItem = Union[IT, ET, AT, WT]
