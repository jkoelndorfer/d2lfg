"""
d2lfl.diablo2.data.database
===========================

This module contains the definition of a Diablo 2 database.
"""

from abc import ABCMeta, abstractmethod
from typing import Callable, Generic, Iterable, Union

from ..game.item import Diablo2ItemType
from ..game.playerclass import Diablo2PlayerClass
from .datafactory import Diablo2DataFactory
from .generic import AnyItem, AT, ET, IT, ST, WT


class Diablo2Database(Generic[AT, ET, IT, ST, WT], metaclass=ABCMeta):
    """
    A Diablo2Database provides a mechanism to access Diablo 2 game data.
    """

    @abstractmethod
    def initialize(self) -> None:
        """
        Initializes the database.

        The database must be initialized before calling methods to get game data.
        """

    @abstractmethod
    def armor(self, code: str) -> AT:
        """
        Returns a Diablo2Armor with the given `code`.
        """

    @abstractmethod
    def all_armors(self) -> Iterable[AT]:
        """
        Returns an iterable over all Diablo2Armor objects in this database.
        """

    def armors_where(self, cond: Callable[[AT], bool]) -> Iterable[AT]:
        """
        Returns an iterable over Diablo2Armor objects matching the given condition.
        """
        return filter(cond, self.all_armors())

    @abstractmethod
    def item(self, code: str) -> AnyItem:
        """
        Returns a Diablo2Item with the given `code`.
        """

    @abstractmethod
    def all_items(self) -> Iterable[AnyItem]:
        """
        Returns an iterable over all Diablo2Item objects in this database.

        Items are things that exist in your inventory. Items include
        things like armor, weapons, potions, quest items, and the
        Horadric Cube.
        """

    def items_where(self, cond: Callable[[AnyItem], bool]) -> Iterable[AnyItem]:
        """
        Returns an iterable Diablo2Item objects matching the given condition.

        Items are things that exist in your inventory. Items include
        things like armor, weapons, potions, quest items, and the
        Horadric Cube.
        """
        return filter(cond, self.all_items())

    @abstractmethod
    def item_type(self, code: str) -> Diablo2ItemType:
        """
        Returns a Diablo2ItemType with the given `code`.
        """

    @abstractmethod
    def skill(self, id: int) -> ST:
        """
        Returns a Diablo2Skill with the given `id`.
        """

    @abstractmethod
    def all_skills(self) -> Iterable[ST]:
        """
        Returns an iterable over all Diablo2Skill objects in this database.
        """

    @abstractmethod
    def skills_for_class(self, d2class: Diablo2PlayerClass) -> Iterable[ST]:
        """
        Returns an iterable over Diablo2Skill objects for the given class.
        """

    def skills_where(self, cond: Callable[[ST], bool]) -> Iterable[ST]:
        """
        Returns an iterable over Diablo2Skill objects matching the given condition.
        """
        return filter(cond, self.all_skills())

    @abstractmethod
    def weapon(self, code: str) -> WT:
        """
        Returns a Diablo2Weapon with the given `code`.
        """

    @abstractmethod
    def all_weapons(self) -> Iterable[WT]:
        """
        Returns an iterable over all Diablo2Weapon objects in this database.
        """

    def weapons_where(self, cond: Callable[[WT], bool]) -> Iterable[WT]:
        """
        Returns an iterable over Diablo2Weapon objects matching the given condition.
        """
        return filter(cond, self.all_weapons())
