"""
d2lfl.game.projectd2.base
=========================

Contains base definitions for Project Diablo 2.
"""

from ...bh.itemdisplay.expression import BHLiteralExpression


class ProjectDiablo2Item(BHLiteralExpression):
    def __init__(self, code: str, name: str, num: int) -> None:
        super().__init__(code)
        self.name = name

    @property
    def charges(self) -> str:
        return f"CHSK{self.num}"

    def __str__(self) -> str:
        return f"SK{self.num}"
