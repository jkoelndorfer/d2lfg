"""
``d2lfg.d2core.d2types.item``
=============================

This module contains models for Diablo 2 item types.
"""

from dataclasses import dataclass
from typing import List, Generator, Optional

from .bodyloc import Diablo2BodyLoc
from .playerclass import Diablo2PlayerClass


@dataclass
class Diablo2ItemType:
    """
    Represents a Diablo 2 item type.

    Item types are defined in ``ItemTypes.txt``.

    See also the
    `Phrozen Keep ItemTypes.txt Guide <https://d2mods.info/forum/viewtopic.php?t=34876>`_.
    """

    #: The name of the item type.
    name: str

    #: The code associated with the item type.
    code: str

    #: One of the parent item types.
    equiv1: Optional["Diablo2ItemType"]

    #: One of the parent item types.
    equiv2: Optional["Diablo2ItemType"]

    #: Whether the item type can be equipped or not.
    body: bool

    #: One of the body locations where the item type can be equipped.
    bodyloc1: Optional[Diablo2BodyLoc]

    #: One of the body locations where the item type can be equipped.
    bodyloc2: Optional[Diablo2BodyLoc]

    #: The ammunition for this item type. For example, items with type
    #: "bow" use "bowq" (bow quiver) item types as ammunition.
    shoots: Optional["Diablo2ItemType"]

    #: The item type that consumes this item type as ammunition.
    #: For example, items with type "bowq" (bow quiver) are used
    #: by "bow" item types.
    quiver: Optional["Diablo2ItemType"]

    #: Whether the item type is throwable.
    throwable: bool

    #: Whether this item can have its quantity increased by dragging-and-dropping
    #: more of the same item on top.
    reload: bool

    #: Whether this item type will be re-equipped automatically from
    #: a picked up drop when ammunition runs out.
    reequip: bool

    #: Whether identical stacks of an item are automatically combined
    #: on pickup.
    autostack: bool

    #: Whether this item can be placed into sockets.
    gem: bool

    #: Whether this item can be placed into the player's belt.
    beltable: bool

    #: The maximum number of sockets this item can have from
    #: item level 1 to 24.
    maxsock1: int

    #: The maximum number of sockets this item can have from
    #: item level 25 to 39.
    maxsock25: int

    #: The maximum number of sockets this item can have over
    #: item level 40.
    maxsock40: int

    #: The character class that will receive +skill bonuses
    #: from this item type.
    staffmods: Optional[Diablo2PlayerClass]

    #: The character class that can use this item type.
    #: NOTE: ``class`` is a reserved Python keyword and
    #: not usable here.
    class_: Optional[Diablo2PlayerClass]

    #: The code of the store page that this item type will appear
    #: on when sold.
    storepage: Optional[str]

    def all_types(self) -> Generator["Diablo2ItemType", None, None]:
        """
        Yields all of this item's types recursively.

        For example, the "axe" type also has type "mgen", which
        in turn has types "mele" and "gen". "mele" has type "weap".
        This method would yield all five types.
        """
        stack: List[Optional[Diablo2ItemType]] = list()
        stack.append(self)
        while len(stack) > 0:
            current_type = stack.pop()
            if current_type is None:
                continue
            yield current_type
            stack.append(current_type.equiv1)
            stack.append(current_type.equiv2)

    def equippable(self) -> bool:
        """
        Returns ``True`` if this item is equippable, ``False`` otherwise.
        """
        return any(it.body for it in self.all_types())
