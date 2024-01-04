"""
d2lfl.diablo2.data.generic
==========================

This module contains generics for Diablo 2 object types.
"""

from typing import TypeVar

from ..game.item import IDiablo2Armor, IDiablo2Equipment, IDiablo2Item, IDiablo2Weapon
from ..game.skill import IDiablo2Skill

IT = TypeVar("IT", bound=IDiablo2Item)
AT = TypeVar("AT", bound=IDiablo2Armor)
ET = TypeVar("ET", bound=IDiablo2Equipment)
ST = TypeVar("ST", bound=IDiablo2Skill)
WT = TypeVar("WT", bound=IDiablo2Weapon)
