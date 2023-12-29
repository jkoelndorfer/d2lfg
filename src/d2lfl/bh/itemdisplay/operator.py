"""
d2lfl.bh.itemdisplay.operator
=============================

This module contains code that defines valid operators in
the BH maphack loot filter language.
"""


class BHOperator:
    def __init__(self, name: str, symbol: str, unary: bool) -> None:
        self.name = name
        self.symbol = symbol
        self.unary = unary


class BHOperators:
    ADD = BHOperator("add", "+", False)
    AND = BHOperator("and", " ", False)
    NOT = BHOperator("not", "!", True)
    LT = BHOperator("less than", "<", False)
    GT = BHOperator("greater than", ">", False)
    EQ = BHOperator("equals", "=", False)
    OR = BHOperator("or", " OR ", False)
    BTWN = BHOperator("between", "~", False)
