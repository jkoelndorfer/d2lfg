"""
``d2lfg.d2core.d2types.skill``
==============================

This module contains the model for a Diablo 2 skill.
"""

from dataclasses import dataclass
from typing import Optional

from .playerclass import Diablo2PlayerClass
from ...util import Diablo2Collection


@dataclass
class Diablo2Skill:
    """
    Represents a Diablo 2 skill.

    Skills are defined in ``Skills.txt`` with some data also in ``SkillDesc.txt``.

    See also the
    `Phrozen Keep Skills.txt Guide <https://d2mods.info/forum/kb/viewarticle?a=440>`_.
    """

    #: The integer ID of the skill.
    id: int

    #: The character class that can use the skill.
    charclass: Optional[Diablo2PlayerClass]

    #: The *unlocalized* name of the skill as it appears in ``Skills.txt``.
    skill: str

    #: The skill tab that this skill appears on as it appears in ``SkillDesc.txt`.
    #: Note: this is not a unique identifier. It functions like an "offset".
    skillpage: int

    def __hash__(self) -> int:
        return hash(self.id)


class Diablo2SkillTab(Diablo2Collection[Diablo2Skill]):
    """
    Represents a Diablo 2 skill tab.

    See the
    `Phrozen Keep Skill Tab Modifier Values <https://d2mods.info/forum/kb/viewarticle?a=45`_.
    """

    #: The integer ID used with skilltab modifiers.
    mod_id: int

    #: The name of the skill tab.
    name: str

    #: The character class that the skill tab belongs to.
    charclass: Diablo2PlayerClass

    #: The skill page ID referencing this skill tab as it appears in ``SkillDesc.txt``.
    skillpage: int
