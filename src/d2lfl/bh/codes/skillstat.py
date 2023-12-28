"""
d2lfl.bh.codes.skillstat
========================

This module contains skill and stat helper classes.
"""

class Stat:
    def __init__(self, name: str, num: int) -> None:
        """
        Creates a new Stat.

        :param name: the name of the stat
        :param num:  the number of the stat
        """
        self.name = name
        self.num = num

    @property
    def char(self) -> str:
        """
        Returns the expression used to check for a character stat (i.e. "CHARSTAT").

        This checks whether the *character*, not the item, has the stat.
        """
        return f"CHARSTAT{self.num}"

    def __str__(self) -> str:
        return f"STAT{self.num}"

    def __repr__(self) -> str:
        return f"STAT{self.num} ({self.name})"
