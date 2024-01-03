"""
d2lfl.bh.itemdisplay.expression.expression
==========================================

This module defines basic BH ItemDisplay expressions.
"""

from abc import ABCMeta, abstractmethod

from typing import Optional, Union

from ..operator import BHOperator, BHOperators


BHOperand = Union[int, "BHExpression"]


# See Project Diablo 2's ItemDisplay code during
# initial d2lfl development:
# https://github.com/Project-Diablo-2/BH/blob/b2f94ed72a9926b62d1c461ef5b10078d12999bb/BH/Modules/Item/ItemDisplay.cpp
#
# Current Project Diablo 2 ItemDisplay code:
# https://github.com/Project-Diablo-2/BH/blob/main/BH/Modules/Item/ItemDisplay.cpp
#
#
# ITEMDISPLAY EXPRESSION TESTING NOTES
# ====================================
#
# Tested with Project Diablo 2 Season 8 on 2023-12-29.
#
# --------------------
#
# The rule:
#    key QTY=1 OR QTY=2
#
# - Applied to keys with QTY=1
# - Applied to keys with QTY=2
# - Applied to other stackables with QTY=2
#
# equivalent rule with parens:
#    (key QTY=1) OR QTY=2
#
# --------------------
#
# The rule:
#    QTY=1 OR key QTY=2
#
# - Applied to keys with QTY=2.
# - *DID NOT* apply to other stackables with QTY=1 or QTY=2.
#
# equivalent rule with parens:
#    (QTY=1 OR key) AND QTY=2
#
# --------------------
#
# The rule:
#    QTY=1 OR key QTY=2 OR QTY=3
#
# - Applied to keys with QTY=2 or QTY=3
# - Applied to other stackables with QTY=3
# - *DID NOT* apply to keys with QTY=1
# - *DID NOT* apply to other stackables with QTY=1 or QTY=2
#
# equivalent rule with parens:
#    ((QTY=1 OR key) QTY=2) OR QTY=3
#
# --------------------
#
# The rule:
#    ALVL>ILVL
#
# Applied to *ALL ITEMS*.
#
# Clearly this is bugged. Some BH ItemDisplay expressions
# don't work.


class BHExpression(metaclass=ABCMeta):
    """
    A BHExpression is a loot filtering expression.
    """

    # The BHExpression interface *does not* use __str__ for this purpose
    # for a couple of reasons:
    #
    # 1. Objects implicitly implement some version of __str__, which
    #    would make the interface definition pointless.
    #
    # 2. Some BHCode objects can be used in filter expressions *AND*
    #    output strings (i.e. item names and descriptions). Because
    #    output strings are completely unstructured from the perspective
    #    of this library, reserving __str__ for use in string templating
    #    outputs makes good sense.
    @abstractmethod
    def bhexpr(self) -> str:
        """
        Converts this BHExpression into a string suitable for use as an
        ItemDisplay condition.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} implementers must define bhexpr()"
        )

    def eq(self, other: BHOperand) -> "BHExpression":
        return self == other

    def lt(self, other: BHOperand) -> "BHExpression":
        return self < other

    def gt(self, other: BHOperand) -> "BHExpression":
        return self > other

    def between(self, low: int, high: int) -> "BHExpression":
        return BHCompoundExpression(BHOperators.BTWN, self, BHLiteralExpression(f"{low}-{high}"))

    def _compare_to(self, operator: BHOperator, operand: BHOperand) -> "BHExpression":
        """
        Compares this BHExpression to the given `operand` using the given `operator`.

        Because operator methods are always called on the left-side operand,
        it is assumed that this object is the left operand in all expressions.
        """
        return BHCompoundExpression(operator, self, operand)

    def __eq__(self, other: BHOperand) -> "BHExpression":
        return self._compare_to(BHOperators.EQ, other)

    def __lt__(self, other: BHOperand) -> "BHExpression":
        return self._compare_to(BHOperators.LT, other)

    def __gt__(self, other: BHOperand) -> "BHExpression":
        return self._compare_to(BHOperators.GT, other)

    def __add__(self, other: BHOperand) -> "BHExpression":
        return self._compare_to(BHOperators.ADD, other)

    def __str__(self) -> str:
        # BH expressions and output codes intermingle in enum classes. While
        # many filter codes are *also* output codes, some are not (specifically
        # "ETH").
        #
        # To prevent mishaps, explicitly prevent string interpolation.
        raise NotImplementedError(
            f"Using {self.__class__.__name__}({self.bhexpr()}) "
            "in string interpolation is an error. This expression *CANNOT* "
            "be used in BH loot filter output text. Use bhexpr() "
            "to convert this expression to a string."
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.bhexpr()})"


class BHLiteralExpression(BHExpression):
    """
    A BHLiteralExpression allows for supporting arbitary text in
    BH loot filter expressions.

    Use of this class is in loot filters discouraged. Prefer using
    d2lfl's built-in codes and operators instead.
    """
    def __init__(self, expression: str) -> None:
        self._expression = expression

    def bhexpr(self) -> str:
        return self._expression


class BHCompoundExpression(BHExpression):
    """
    A BHCompoundExpression is a BHExpression that consists of an operator
    and at least one operand.

    Valid operands include basic Python integers and any BHExpression.
    """
    def __init__(
        self,
        operator: BHOperator,
        *operands: BHOperand,
    ) -> None:
        if len(operands) > 1 and operator.unary:
            raise ValueError("operator is unary but more than one operand provided")

        self.operator = operator
        self.operands = operands
        self._condition_str: Optional[str] = None

    def bhexpr(self) -> str:
        if self._condition_str is not None:
            return self._condition_str

        if self.operator.unary:
            unary_operand = self.operands[0]
            self._condition_str = \
                f"{self.operator.symbol}{self.operand_bhexpr(unary_operand)}"
        else:
            self._condition_str = self.operator.symbol.join(
                self.operand_bhexpr(o) for o in self.operands
            )
        return self._condition_str


    def operand_bhexpr(self, operand: BHOperand):
        if isinstance(operand, int):
            return str(operand)

        if _expr_requires_parens(outer_expr=self, inner_expr=operand):
            return f"({operand.bhexpr()})"
        else:
            return operand.bhexpr()


def bh_and(*expressions: BHExpression) -> BHExpression:
    """
    Joins BHExpression objects using logical AND.
    """
    return BHCompoundExpression(BHOperators.AND, *expressions)


def bh_or(*expressions: BHExpression) -> BHExpression:
    """
    Joins BHExpression objects using logical OR.
    """
    return BHCompoundExpression(BHOperators.OR, *expressions)


def bh_not(expression: BHExpression) -> BHExpression:
    """
    Negates a BHExpression object using logical NOT.
    """
    return BHCompoundExpression(BHOperators.NOT, expression)


def _expr_requires_parens(outer_expr: "BHCompoundExpression", inner_expr: BHOperand) -> bool:
    """
    Returns True if `inner_expr` must be surrounded by parenthesis to maintain
    its meaning when incorporated into `outer_expr`.
    """
    if not isinstance(inner_expr, BHCompoundExpression):
        # If the inner expression is not a compound expression, parenthesis
        # are never required.
        return False

    if outer_expr.operator is BHOperators.NOT:
        # Logical NOT *always* requires parens if the expression
        # is compound.
        return True

    paren_req_operators = (BHOperators.AND, BHOperators.OR)
    if inner_expr.operator not in paren_req_operators:
        # Inner expressions like less than, greater than, equals,
        # and between never need to be surrounded by parenthesis.
        return False

    return True
