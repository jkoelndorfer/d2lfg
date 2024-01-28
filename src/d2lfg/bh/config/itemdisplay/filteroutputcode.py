"""
``d2lfg.bh.config.itemdisplay.filteroutputcode``
================================================

This module contains the definition of a BH maphack ItemDisplay filter output code.

Filter output codes are both filter expressions and output codes. They can be used
for filtering items and in item names or descriptions.
"""

from .filterexpr import BHFilterExpression
from .outputcode import BHOutputCode


class BHFilterOutputCode(BHOutputCode, BHFilterExpression):
    """
    Object that is both a
    :py:class:`~d2lfg.bh.config.itemdisplay.filterexpr.BHFilterExpression` and a
    :py:class:`~d2lfg.bh.config.itemdisplay.outputcode.BHOutputCode`.
    """

    def bhexpr(self) -> str:
        return self.code


class BHFilterOutputCodeLiteral(BHFilterOutputCode):
    """
    A literal :py:class:`BHFilterOutputCode`.

    :param code: the code and filter expression
    """

    def __init__(self, code: str) -> None:
        self._code = code

    @property
    def code(self) -> str:
        """
        Returns the code provided when this object was initialized.
        """
        return self._code
