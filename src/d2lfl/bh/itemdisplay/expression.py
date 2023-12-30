"""
d2lfl.bh.itemdisplay.expression
===============================

This code defines BH maphack loot filter expression classes.
"""

from abc import ABCMeta, abstractmethod
from typing import Optional, Union

from .operator import BHOperator, BHOperators

BHOperand = Union[int, "BHExpression"]


# See Project Diablo 2's ItemDisplay code:
#
# Initial development of this d2lfl:
# https://github.com/Project-Diablo-2/BH/blob/b2f94ed72a9926b62d1c461ef5b10078d12999bb/BH/Modules/Item/ItemDisplay.cpp
#
# Current:
# https://github.com/Project-Diablo-2/BH/blob/main/BH/Modules/Item/ItemDisplay.cpp
#
# ITEMDISPLAY EXPRESSION TESTING NOTES
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
    def as_condition_str(self) -> str:
        """
        Converts this BHExpression into a string suitable for use as an
        ItemDisplay condition.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} implementers must define as_condition_str()"
        )

    @abstractmethod
    def requires_parens_for(self, operator: BHOperator) -> bool:
        """
        Determines if this expression requires the protection of parenthesis
        if operated on using the given `operator`. This method will be called
        by `BHCompoundExpression` objects.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} implementers must define requires_parens_for()"
        )

    def and_(self, other: "BHExpression") -> "BHExpression":
        return self & other

    def eq(self, other: BHOperand) -> "BHExpression":
        return self == other

    def between(self, low: int, high: int) -> "BHExpression":
        return BHCompoundExpression(self, BHOperators.BTWN, BHLiteralExpression(f"{low}-{high}"))

    def or_(self, other: "BHExpression") -> "BHExpression":
        return self | other

    def _compare_to(self, operator: BHOperator, operand: BHOperand) -> "BHExpression":
        """
        Compares this BHExpression to the given `operand` using the given `operator`.

        Because operator methods are always called on the left-side operand,
        it is assumed that this object is the left operand in all expressions.
        """
        return BHCompoundExpression(self, operator, operand)

    def __eq__(self, other: BHOperand) -> "BHExpression":
        return self._compare_to(BHOperators.EQ, other)

    def __lt__(self, other: BHOperand) -> "BHExpression":
        return self._compare_to(BHOperators.LT, other)

    def __gt__(self, other: BHOperand) -> "BHExpression":
        return self._compare_to(BHOperators.GT, other)

    def __invert__(self) -> "BHExpression":
        return BHCompoundExpression(None, BHOperators.NOT, self)

    def __add__(self, other: BHOperand) -> "BHExpression":
        return self._compare_to(BHOperators.ADD, other)

    def __and__(self, other: BHOperand) -> "BHExpression":
        return self._compare_to(BHOperators.AND, other)

    def __or__(self, other: BHOperand) -> "BHExpression":
        return self._compare_to(BHOperators.OR, other)

    def __str__(self) -> str:
        # BH expressions and codes intermingle in enum classes. While most
        # filter codes are *also* output codes, some are not (specifically
        # "ETH").
        #
        # To prevent mishaps, explicitly prevent string interpolation.
        raise NotImplementedError(
            f"Using {self.__class__.__name__}({self.as_condition_str()}) "
            "in string interpolation is an error. This expression *CANNOT* "
            "be used in BH loot filter output text. Use as_condition_str() "
            "to convert this expression to a string."
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.as_condition_str()})"


class BHLiteralExpression(BHExpression):
    """
    A BHLiteralExpression allows for supporting arbitary text in
    BH loot filter expressions.

    Use of this class is discouraged. Prefer using d2lfl's built-in
    codes and operators instead.
    """
    def __init__(self, value: str) -> None:
        self.value = value

    def as_condition_str(self) -> str:
        return self.value

    def requires_parens_for(self, operator: BHOperator) -> bool:
        # As this is a literal, this expression should never be
        # modified by wrapping it in parenthesis.
        #
        # If parenthesis are required, include them in the literal
        # directly.
        return False


class BHCompoundExpression(BHExpression):
    """
    A BHCompoundExpression is a BHExpression that consists of an operator
    and at least one operand.

    Valid operands include basic Python integers and any BHExpression.
    """
    def __init__(
        self,
        left_operand: Optional[BHOperand],
        operator: BHOperator,
        right_operand: BHOperand,
    ) -> None:
        if left_operand is None and not operator.unary:
            raise ValueError("a left operand is required for non-unary operators")
        elif left_operand is not None and operator.unary:
            raise ValueError("a left operand cannot be specified for unary operators")

        self.left_operand = left_operand
        self.operator = operator
        self.right_operand = right_operand
        self._condition_str: Optional[str] = None

    def as_condition_str(self) -> str:
        if self._condition_str is not None:
            return self._condition_str

        self._condition_str = f"{self._left_operand_str()}{self.operator.symbol}{self._right_operand_str()}"
        return self._condition_str

    def _left_operand_str(self) -> str:
        if isinstance(self.left_operand, int):
            return str(self.left_operand)

        if self.left_operand is None:
            return ""

        if self.left_operand.requires_parens_for(self.operator):
            return f"({self.left_operand.as_condition_str()})"
        else:
            return self.left_operand.as_condition_str()

    def _right_operand_str(self) -> str:
        if isinstance(self.right_operand, int):
            return str(self.right_operand)

        if self.right_operand.requires_parens_for(self.operator):
            return f"({self.right_operand.as_condition_str()})"
        else:
            return self.right_operand.as_condition_str()

    def requires_parens_for(self, operator: BHOperator) -> bool:
        # Note: I was not able to find good information about operator
        # precedence for BH expressions (are there precedence rules?)
        #
        # This method is based on my evaluation of current loot filters
        # and tries to be conservative.
        and_or_expr = (
            (self.operator is BHOperators.OR  and operator is BHOperators.AND) or
            (self.operator is BHOperators.AND and operator is BHOperators.OR)
        )
        if and_or_expr:
            # If this expression is of the form:
            #
            #     a OR b
            #
            # and we are joined by an AND operator, then we need to
            # wrap this expression in parenthesis to preserve the
            # logical meaning of this OR expression.
            #
            #     BAD:   c AND a OR B
            #     GOOD:  c AND (a OR b)
            return True
        elif operator is BHOperators.NOT:
            # If this expression is of the form
            #
            #    !a
            #
            # Then we skip parenthesis:
            #
            #    !!a
            #
            # This could expression simplified to just "a" but there
            # is not a great benefit to doing so and avoiding that can
            # of worms keeps this library simpler.
            if self.operator is BHOperators.NOT:
                return False

            # If this expression takes one of the forms:
            #
            #    a OR  b
            #    a AND b
            #    a+b>10
            #
            # and we invert it using logical NOT, we need
            # to wrap the expression in parenthesis.
            #
            #     BAD:   !a OR b
            #     GOOD:  !(a OR b)
            #
            #     BAD:   !a AND b
            #     GOOD:  !(a AND b)
            #
            #     BAD:   !a+b>10     <- this may also be syntactically invalid? not sure
            #     GOOD:  !(a+b>10)
            return True
        return False
