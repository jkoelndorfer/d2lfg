"""
``d2lfg.gamedata.database``
===========================

This module contains the base implementation for a Diablo 2 game database.
"""

from abc import ABCMeta, abstractmethod
from types import MappingProxyType
from typing import Callable, Dict, Generic, Iterator, Mapping, TypeVar

from ..d2core.d2types import (
    Diablo2BodyLoc,
    Diablo2Item,
    Diablo2ItemType,
    Diablo2PlayerClass,
    Diablo2Skill,
)
from ..d2core.data.txt import Diablo2TxtFile, Diablo2TxtRecord
from .datasource import Diablo2TxtDataSource


BodyLoc = TypeVar("BodyLoc", bound=Diablo2BodyLoc)
ItemType = TypeVar("ItemType", bound=Diablo2ItemType)
Item = TypeVar("Item", bound=Diablo2Item)
PlayerClass = TypeVar("PlayerClass", bound=Diablo2PlayerClass)
Skill = TypeVar("Skill", bound=Diablo2Skill)


class ItemTypeFactory(Generic[BodyLoc, ItemType, PlayerClass]):
    """
    Factory to produce item types.

    Diablo 2 item types reference other item types, which necessitates
    creating item type objects in two passes.

    In the first pass, objects are created without references to other item types.

    In the second pass, references are established.

    :param initializer: callable that *mostly* initializes an item type; \
        equiv1 and equiv2 fields should be left unset
    """

    def __init__(
        self,
        initializer: Callable[
            [Diablo2TxtRecord, Mapping[str, BodyLoc], Mapping[str, PlayerClass]],
            ItemType,
        ],
    ) -> None:
        self.initializer = initializer

    def itemtypes(
        self,
        txt: Diablo2TxtFile,
        bodylocs: Mapping[str, BodyLoc],
        playerclasses: Mapping[str, PlayerClass],
    ) -> Dict[str, ItemType]:
        # equiv1 and equiv2 correspond with the equiv1 and equiv2 attributes
        # of an item type.
        #
        # Suppose that:
        #   * IT is a valid Diablo2ItemType object
        #   * IT.equiv1 is a valid Diablo2ItemType object
        #   * IT.equiv2 is a valid Diablo2ItemType object
        #
        # then:
        #
        # equiv1[IT.code] == IT.equiv1.code
        # equiv2[IT.code] == IT.equiv2.code
        equiv1: Dict[str, str] = dict()
        equiv2: Dict[str, str] = dict()

        itemtypes: Dict[str, ItemType] = dict()

        for record in txt.records:
            it = self.initializer(record, bodylocs, playerclasses)
            if record["equiv1"]:
                equiv1[it.code] = record["equiv1"]
            if record["equiv2"]:
                equiv2[it.code] = record["equiv2"]
            itemtypes[it.code] = it

        for parent_code, child_code in equiv1.items():
            itemtypes[parent_code].equiv1 = itemtypes[child_code]

        for parent_code, child_code in equiv2.items():
            itemtypes[parent_code].equiv2 = itemtypes[child_code]

        return itemtypes


class Diablo2GameDatabase(
    Generic[BodyLoc, Item, ItemType, PlayerClass, Skill], metaclass=ABCMeta
):
    """
    Abstract base class for Diablo 2 game databases.

    Concrete implementations return data types suitable for use
    in loot filter construction.
    """

    @abstractmethod
    def all_items(self) -> Iterator[Item]:
        """
        Iterator over all Diablo2Item objects in this database.
        """

    @abstractmethod
    def item(self, code: str) -> Item:
        """
        Returns the Diablo2Item represented by the given ``code``.

        An item code is used in game data files as a unique identifier
        for the item. It is typically 3 or 4 characters.

        :param code: the item code of the item
        :return: the item with the given code
        """
        raise NotImplementedError("subclasses should implement item()")

    def items_where(self, cond: Callable[[Item], bool]) -> Iterator[Item]:
        """
        Returns an iterator over all Diablo2Item objects matching the given ``cond``.

        :param cond: the condition that items must match
        """
        return filter(cond, self.all_items())

    @abstractmethod
    def item_type(self, code: str) -> ItemType:
        """
        Returns a Diablo2ItemType represented by the given ``code``.

        :param code: the item type code
        :return: the item type with the given code
        """
        raise NotImplementedError("subclasses should implement item_type()")

    @abstractmethod
    def player_class(self, name_or_code: str) -> PlayerClass:
        """
        Returns the Diablo2PlayerClass represented by the given ``name_or_code``.

        :param name_or_code: the name or three-letter code of the player class
        :return: the player class
        """

    @abstractmethod
    def skill(self, id_or_name: int | str) -> Skill:
        """
        Returns the Diablo2Skill represented by the given ``id``.

        :param id_or_name: the integer ID or name of the skill as it appears \
            in ``Skills.txt``.
        :return: the skill with the given id
        """
        raise NotImplementedError("subclasses should implement skill()")


class Diablo2TxtGameDatabase(
    Diablo2GameDatabase[BodyLoc, Item, ItemType, PlayerClass, Skill]
):
    """
    Diablo 2 game database that is backed by a Diablo2TxtDataSource.
    """

    def __init__(
        self,
        datasource: Diablo2TxtDataSource,
        bodyloc_factory: Callable[[Diablo2TxtRecord], BodyLoc],
        itemtype_factory: ItemTypeFactory[BodyLoc, ItemType, PlayerClass],
        item_factory: Callable[[Diablo2TxtRecord, Mapping[str, ItemType]], Item],
        player_class_factory: Callable[[Diablo2TxtRecord], PlayerClass],
        skill_factory: Callable[[Diablo2TxtRecord], Skill],
    ) -> None:
        self.datasource = datasource
        self.bodyloc_factory = bodyloc_factory
        self.itemtype_factory = itemtype_factory
        self.item_factory = item_factory
        self.player_class_factory = player_class_factory
        self.skill_factory = skill_factory

        self._bodylocs: Dict[str, BodyLoc] = dict()
        self._items: Dict[str, Item] = dict()
        self._itemtypes: Dict[str, ItemType] = dict()
        self._playerclasses: Dict[str, PlayerClass] = dict()
        self._skills: Dict[int, Skill] = dict()

    def _initialize(self) -> None:
        """
        Initializes the database from the data source.
        """
        self._initialize_playerclasses()
        self._initialize_bodylocs()

    def _initialize_bodylocs(self) -> None:
        """
        Initializes the database's body locations from the data source.
        """
        for record in self.datasource.bodylocs_txt.records:
            bodyloc = self.bodyloc_factory(record)
            self._bodylocs[bodyloc.code] = bodyloc

    def _initialize_itemtypes(self) -> None:
        """
        Initializes the database's item types from the data source.
        """
        self._itemtypes = self.itemtype_factory.itemtypes(
            self.datasource.itemtypes_txt, MappingProxyType(self._bodylocs)
        )

    def _initialize_items(self) -> None:
        """
        Initializes the database's items from the data source.
        """
        item_txts = (
            self.datasource.armor_txt,
            self.datasource.misc_txt,
            self.datasource.weapons_txt,
        )
        itemtype_proxy = MappingProxyType(self._itemtypes)
        for txt in item_txts:
            for item_def in txt.records:
                item = self.item_factory(item_def, itemtype_proxy)
                self._items[item.code] = item

    def _initialize_playerclasses(self) -> None:
        """
        Initializes the database's player classes from the data source.
        """

    def all_items(self) -> Iterator[Item]:
        """
        Iterator over all Diablo2Item objects in this database.
        """
        for i in self._items.values():
            yield i

    def item(self, code: str) -> Item:
        """
        Returns the Diablo2Item represented by the given ``code``.

        An item code is used in game data files as a unique identifier
        for the item. It is typically 3 or 4 characters.

        :param code: the item code of the item
        :return: the item with the given code
        """
        raise NotImplementedError("subclasses should implement item()")

    def items_where(self, cond: Callable[[Item], bool]) -> Iterator[Item]:
        """
        Returns an iterator over all Diablo2Item objects matching the given ``cond``.

        :param cond: the condition that items must match
        """
        return filter(cond, self.all_items())

    def player_class(self, name_or_code: str) -> PlayerClass:
        """
        Returns the Diablo2PlayerClass represented by the given ``name_or_code``.

        :param name_or_code: the name or three-letter code of the player class
        :return: the player class
        """

    def skill(self, id_or_name: int | str) -> Skill:
        """
        Returns the Diablo2Skill represented by the given ``id``.

        :param id: the integer ID of the skill as it appears in ``Skills.txt``.
        :return: the skill with the given id
        """
        raise NotImplementedError("subclasses should implement skill()")
