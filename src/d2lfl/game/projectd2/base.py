"""
d2lfl.game.projectd2.base
=========================

Contains base definitions for Project Diablo 2.
"""

class Skill:
    def __init__(self, name: str, num: int) -> None:
        self.name = name
        self.num = num

    @property
    def charges(self) -> str:
        return f"CHSK{self.num}"

    def __str__(self) -> str:
        return f"SK{self.num}"
