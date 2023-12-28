"""
d2lfl.bh.expression
===================

This code defines BH maphack loot filter expression classes.
"""

from typing import Union

from .code import BHCode
from .itemdisplay import ItemDisplayConditionable
from .operator import BHOperator

Operand = Union[int, str, "BHCode", "BHExpression"]


class BHOperatorMixin:
    """
    Mixin class that defines operators for BHExpression and BHAtom.
    """
    def _new_expression(self, operator: BHOperator, right_operand) -> "BHExpression":
        if operator.unary:
            return BHExpression(
                left_operand=None,
                operator=operator,
                right_operand=right_operand
            )

    def __gt__(self, other: object) -> "BHExpression":
        if not self._comparable(other):
            raise NotImplementedError("cannot compare")


class BHExpression(ItemDisplayConditionable):
    """
    A BHExpression is composed of at least one Operand and an operator.
    """
    def __init__(self, left_operand, operator, right_operand) -> None:
        self.left_operand = left_operand
        self.operator = operator
        self.right_operand = right_operand

    def item_display_condition(self) -> str:
        return "TODO"

    @classmethod
    def _parens_required_for(cls, operator: BHOperator, operand: Operand) -> bool:
        """
        If an expression is formed with the given operator and operand,
        returns True if the operand requires the protection of parenthesis
        to maintain its intended meaning. Returns False if parenthesis are
        not required.
        """
        if isinstance(operand, str):
            # String expressions could be anything! Rather than try to parse
            # the string expression, let's just always wrap it in parenthesis.
            return True

        if isinstance(operand, (int, BHCode)):
            # Integers are atomic
