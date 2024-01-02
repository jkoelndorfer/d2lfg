"""
d2lfl.diablo2.data.database
===========================

This module contains the definition of a Diablo 2 database.
"""

from abc import ABCMeta, abstractmethod
from pathlib import Path
from typing import Dict

from ..game.item import (
    Diablo2Item,
    Diablo2ItemType,
    Diablo2Armor,
    Diablo2Weapon,
)
from ..game.skill import Diablo2Skill


class Diablo2Database(metaclass=ABCMeta):
    """
    A Diablo2Database provides a mechanism to access Diablo 2 game data.
    """
    @abstractmethod
    def armor(self, code: str) -> Diablo2Armor:
        """
        Returns a Diablo2Armor with the given `code`.
        """

    @abstractmethod
    def item(self, code: str) -> Diablo2Item:
        """
        Returns a Diablo2Item with the given `code`.
        """

    @abstractmethod
    def item_type(self, code: str) -> Diablo2ItemType:
        """
        Returns a Diablo2ItemType with the given `code`.
        """

    @abstractmethod
    def skill(self, id: int) -> Diablo2Skill:
        """
        Returns a Diablo2Skill with the given `id`.
        """

    @abstractmethod
    def weapon(self, code: str) -> Diablo2Weapon:
        """
        Returns a Diablo2Weapon with the given `code`.
        """
