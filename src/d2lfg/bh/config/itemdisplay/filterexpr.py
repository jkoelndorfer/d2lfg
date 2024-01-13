"""
``d2lfg.bh.config.itemdisplay.filterexpr``
==========================================

This module contains the definition of a BH maphack ItemDisplay filter expression.

Filter expressions are rules that select particular items.
"""

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from sys import maxsize
from typing import Optional, Sequence, Union

from ....error import InvalidStringConversionError, TooManyOperandsError


#: Type describing valid filter expression operands.
BHFilterOperand = Union["BHFilterExpression", int]


@dataclass
class BHFilterOperator:
    """
    Object representing an operator in a compound filter expression.
    """

    name: str
    symbol: str
    max_operands: int


class BHFilterOperators:
    """
    Collection of valid :py:class:`BHFilterOperator` objects.
    """

    #: Operator for the "addition" operation.
    ADD = BHFilterOperator("add", "+", maxsize)

    #: Operator for the "logical and" operation.
    AND = BHFilterOperator("and", " ", maxsize)

    #: Operator for the "logical not" operation.
    NOT = BHFilterOperator("not", "!", 1)

    #: Operator for the "less than" operation.
    LT = BHFilterOperator("less than", "<", 2)

    #: Operator for the "greater than" operation.
    GT = BHFilterOperator("greater than", ">", 2)

    #: Operator for the "equality" operation.
    EQ = BHFilterOperator("equals", "=", 2)

    #: Operator for the "logical or" operation.
    OR = BHFilterOperator("or", " OR ", maxsize)

    #: Operator for the "between" operation.
    BTWN = BHFilterOperator("between", "~", 2)


class BHFilterExpression(metaclass=ABCMeta):
    """
    Object representing a BH maphack ItemDisplay filter expression.

    This object can be composed with other filter expressions using
    operators and functions. The resulting object can be further
    composed, or it can be rendered into a string that is a valid
    BH maphack ItemDisplay filter expression.
    """

    @abstractmethod
    def bhexpr(self) -> str:
        """
        Renders this object into a string suitable for use in an
        ItemDisplay filter expression.
        """
        raise NotImplementedError("subclasses must implement bhexpr()")

    def add(self, other: BHFilterOperand) -> "BHCompoundFilterExpression":
        """
        Returns a :py:class:`BHFilterExpression` that represents the
        addition of this object and ``other``.

        :param other: the operand to add to this one.
        """
        return BHCompoundFilterExpression(BHFilterOperators.ADD, self, other)

    __add__ = add

    def between(self, low: int, high: int) -> "BHCompoundFilterExpression":
        """
        Returns a between :py:class:`BHFilterExpression` that checks
        if this expression is between two values.

        :param low: the minimum value of this expression
        :param high: the maximum value of this expression
        """
        return BHCompoundFilterExpression(
            BHFilterOperators.BTWN, self, BHFilterExpressionLiteral(f"{low}-{high}")
        )

    btwn = between

    def eq(self, other: BHFilterOperand) -> "BHCompoundFilterExpression":
        """
        Returns a :py:class:`BHFilterExpression` that represents an
        equality comparison between this object and ``other``.

        :param other: the other operand in the equality comparison
        """
        return BHCompoundFilterExpression(BHFilterOperators.EQ, self, other)

    def __eq__(self, other: object) -> bool:
        """
        Returns ``True`` if ``other`` is equal to this object.

        :param other: the object to compare to this one
        """
        if not isinstance(other, BHFilterExpression):
            return False
        return self.bhexpr() == other.bhexpr()

    def gt(self, other: int) -> "BHCompoundFilterExpression":
        """
        Returns a :py:class:`BHFilterExpression` that represents a
        greater than comparison between this object and ``other``.

        :param other: the other operand in the less than comparison
        """
        return BHCompoundFilterExpression(BHFilterOperators.GT, self, other)

    def lt(self, other: int) -> "BHCompoundFilterExpression":
        """
        Returns a :py:class:`BHFilterExpression` that represents a
        less than comparison between this object and ``other``.

        :param other: the other operand in the less than comparison
        """
        return BHCompoundFilterExpression(BHFilterOperators.LT, self, other)

    def __str__(self) -> str:
        # BH expressions and output codes intermingle in enum classes. While
        # many filter codes are *also* output codes, some are not (specifically
        # "ETH").
        #
        # To prevent mishaps, explicitly prevent string interpolation.
        raise InvalidStringConversionError(
            f"Using {repr(self)} in string interpolation is an error. "
            "This expression *CANNOT* be used in BH loot filter output text. "
            "Use bhexpr() to convert this expression to a string."
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.bhexpr()})"


class BHFilterExpressionLiteral(BHFilterExpression):
    """
    Object representing a literal BH ItemDisplay filter expression.

    When composed with other :py:class:`BHFilterExpression` objects and
    rendered, this object will appear literally in the resulting expression.

    It is incumbent on the initializer of this class to ensure that the
    expression provided is valid.

    :param s: the filter expression literal
    """

    def __init__(self, s: str) -> None:
        self.s = s

    def bhexpr(self) -> str:
        """
        Returns the literal value that this object was initialized with.
        """
        return self.s


class BHCompoundFilterExpression(BHFilterExpression):
    """
    Object representing a compound ItemDisplay filter expression.

    Compound expressions consist of one or more operands and an operator.

    :param operator: the operator of this compound expression
    :param operands: the operands of this compound expression
    """

    def __init__(
        self,
        operator: BHFilterOperator,
        *operands: BHFilterOperand,
    ) -> None:
        num_operands = len(operands)
        if num_operands > operator.max_operands:
            raise TooManyOperandsError(
                f"{num_operands} given, but {operator.name} supports at max "
                f"{operator.max_operands} operands"
            )

        self._operator = operator
        self._operands = operands
        self._expression: Optional[str] = None

    @property
    def operator(self) -> BHFilterOperator:
        """
        The :py:class:`BHFilterOperator` of this expression.
        """
        return self._operator

    @property
    def operands(self) -> Sequence[BHFilterOperand]:
        """
        The sequence of :py:class:`BHFilterOperand` objects in this expression.
        """
        return self._operands

    def bhexpr(self) -> str:
        """
        Renders this object into a string suitable for use in an
        ItemDisplay filter expression.
        """
        if self._expression is not None:
            return self._expression

        if self._operator.max_operands == 1:
            unary_operand = self._operands[0]
            self._expression = (
                f"{self._operator.symbol}{self._operand_bhexpr(unary_operand)}"
            )
        else:
            self._expression = self._operator.symbol.join(
                self._operand_bhexpr(o) for o in self._operands
            )
        return self._expression

    def _operand_bhexpr(self, operand: BHFilterOperand) -> str:
        """
        Returns the string represention of an operand within this expression.

        :param operand: the operand to be represented as part of this expression
        """
        if isinstance(operand, int):
            return str(operand)

        if self.expr_requires_parens(outer_expr=self, inner_expr=operand):
            return f"({operand.bhexpr()})"
        else:
            return operand.bhexpr()

    @classmethod
    def expr_requires_parens(
        cls, outer_expr: "BHCompoundFilterExpression", inner_expr: BHFilterOperand
    ) -> bool:
        """
        Returns ``True`` if ``inner_expr`` requires parenthesis to maintain
        its meaning when included in ``outer_expr``. Returns ``False`` otherwise.

        :param outer_expr: the expression containing ``inner_expr``
        :param inner_expr: the expression inside ``outer_expr``
        """
        if not isinstance(inner_expr, BHCompoundFilterExpression):
            # If the inner expression is not a compound expression, parenthesis
            # are never required.
            return False

        if outer_expr.operator is BHFilterOperators.NOT:
            # Logical NOT *always* requires parens if the expression
            # is compound.
            return True

        paren_req_operators = (BHFilterOperators.AND, BHFilterOperators.OR)
        if inner_expr.operator not in paren_req_operators:
            # Inner expressions like less than, greater than, equals,
            # and between don't need to be surrounded by parenthesis when
            # combined with AND and OR.
            return False

        # If there are any unhandled cases, assume parenthesis are
        # required to maintain meaning.
        return True


def bh_and(*operands: BHFilterExpression) -> BHCompoundFilterExpression:
    """
    Logically ands the given :py:class:`BHFilterExpression` objects together.
    """
    return BHCompoundFilterExpression(BHFilterOperators.AND, *operands)


def bh_not(operand: BHFilterExpression) -> BHCompoundFilterExpression:
    """
    Logically inverts the given :py:class:`BHFilterExpression`.
    """
    return BHCompoundFilterExpression(BHFilterOperators.NOT, operand)


def bh_or(*operands: BHFilterExpression) -> BHCompoundFilterExpression:
    """
    Logically ors the given :py:class:`BHFilterExpression` objects together.
    """
    return BHCompoundFilterExpression(BHFilterOperators.OR, *operands)
