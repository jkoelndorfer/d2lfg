"""
d2lfl.bh.expression
===================

This code defines BH maphack loot filter expression classes.
"""

from enum import auto, Enum


class BHOperator(Enum):
    #: Adds the two operands together.
    ADD = auto()

    #: Logically ands the two operands together.
    AND = auto()

    #: Checks the operands for equality.
    EQUALS = auto()

    #: Checks if the left operand is greater than the right operand.
    GREATER_THAN = auto()

    #: Checks if the left operand is less than the right operand.
    LESS_THAN = auto()

    #: Inverses the right operand. If this operator is used, there is no left operand.
    NOT = auto()

    #: Logically ors the two operands together.
    OR = auto()


class BHOperatorMixin:
    """
    Mixin class that defines operators for BHExpression and BHAtom.
    """
    def _valid_expression(self, operator: BHOperator, right_operand) -> bool:
        return isinstance(right_operand, (BHAtom, BHExpression, int, str))

    def _new_expression(self, operator: BHOperator, right_operand) -> "BHExpression":
        if not self._valid_expression(operator, right_operand)
            raise NotImplementedError(
                f"cannot compare {self.__class__.__name__} to {right_operand.__class__.__name__}"
            )


    def __gt__(self, other: object) -> "BHExpression":
        if not self._comparable(other):
            raise NotImplementedError("cannot compare")


class BHExpression:
    """
    A BHExpression is composed of at least one BHAtom (or integer) and an operator.
    """
    def __init__(self, left_operand, operator, right_operand) -> None:
        self.left_operand = left_operand
        self.operator = operator
        self.right_operand = right_operand


class BHAtom:
    """
    A BHAtom is the smallest unit in an expression.

    It cannot be divided further without altering the meaning of
    a filter rule.

    Examples of atoms include integers and BHCode objects.
    """
