"""
``d2lfg.d2core.d2types.playerclass``
====================================

This module contains the model for a Diablo 2 player class.
"""

from dataclasses import dataclass
from typing import Type, TypeVar

from ...util import Diablo2Collection


D2Class = TypeVar("D2Class", bound="Diablo2PlayerClass")


@dataclass
class Diablo2PlayerClass:
    """
    Model for a Diablo 2 player class.
    """

    name: str
    code: str

    @classmethod
    def copy(cls: Type[D2Class], other: "Diablo2PlayerClass") -> D2Class:
        return cls(other.name, other.code)

    def __hash__(self) -> int:
        return hash(f"{self.name}.{self.code}")


class Diablo2PlayerClasses(Diablo2Collection[Diablo2PlayerClass]):
    """
    Collection of valid :py:class:`Diablo2PlayerClass` objects.

    These *could* be looked up dynamically in ``PlayerClass.txt``.
    However, class information is hardcoded into Diablo 2 itself,
    so code edits are required to modify these per the Phrozen
    Keep file guide `[1]`_:

        Hardcoded reference tables:
        These files are lookup tables that link hardcoded data with
        the txt files, you need to edit the code to edit these

        [...]

        PlayerClass.txt - lookup table for class codes

    .. _[1]: https://www.d2mods.info/forum/viewtopic.php?t=34455
    """

    AMA = AMAZON = Diablo2PlayerClass("Amazon", "ama")
    ASS = ASSASSIN = Diablo2PlayerClass("Assassin", "ass")
    BAR = BARBARIAN = Diablo2PlayerClass("Barbarian", "bar")
    DRU = DRUID = Diablo2PlayerClass("Druid", "dru")
    NEC = NECROMANCER = Diablo2PlayerClass("Necromancer", "nec")
    PAL = PALADIN = Diablo2PlayerClass("Paladin", "pal")
    SOR = SORCERESS = Diablo2PlayerClass("Sorceress", "sor")

    @classmethod
    def collection_type(cls) -> Type[Diablo2PlayerClass]:
        return Diablo2PlayerClass
