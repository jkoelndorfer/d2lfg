"""
d2lfl.diablo2.data.normalize
============================

This module contains code to normalize data lookups by name.
"""

import re
from typing import Dict


class Diablo2LookupNormalizer:
    """
    Diablo2LookupNormalizer provides a mechanism to normalize and alias named
    game data.

    Some data (like skills) have names in their .txt data files which don't
    reflect the name displayed in game. While it would be nice to use the
    localization data to get real names, that requires parsing .tbl files
    which will be a non-trivial effort.

    For now, we use a this class to provide aliases and data normalization.
    """
    skill_strip = re.compile(r"""[ "'-]""")

    def __init__(self) -> None:
        self.aliases: Dict[str, str] = dict()

    def add_alias(self, alias: str, actual_name: str) -> None:
        self.aliases[self.normalize(alias)] = self.normalize(actual_name)

    def lookup(self, skill_name: str) -> str:
        normalized_skill_name = self.normalize(skill_name)
        return self.aliases.get(normalized_skill_name, normalized_skill_name)

    @classmethod
    def normalize(cls, skill_name: str) -> str:
        return cls.skill_strip.sub("", skill_name).upper()
