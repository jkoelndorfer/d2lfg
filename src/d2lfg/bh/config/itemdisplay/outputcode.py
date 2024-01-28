"""
``d2lfg.bh.config.itemdisplay.outputcode``
==========================================

This module contains the definition of a BH maphack ItemDisplay output code.

Output codes can be used in item names and descriptions.
"""

from abc import ABCMeta, abstractproperty
from typing import final


class BHOutputCode(metaclass=ABCMeta):
    """
    Object representing a code that can be used in a BH maphack
    ItemDisplay item name or description.
    """

    @abstractproperty
    def code(self) -> str:
        """
        The value of this BH output code.

        The value *MUST NOT* include wrapping ``%`` symbols.
        """
        raise NotImplementedError("subclasses must implement the code property")

    @final
    def __str__(self) -> str:
        """
        The BH code suitable for use in an ItemDisplay name or item description.

        This code will be surrounded by ``%`` characters so it is properly
        substituted.
        """
        return f"%{self.code}%"


class BHOutputCodeLiteral(BHOutputCode):
    """
    A literal :py:class:`BHOutputCode`.

    :param code: the code to return via the ``code`` property
    """

    def __init__(self, code: str) -> None:
        self._code = code

    @property
    def code(self) -> str:
        """
        Returns the code provided when this object was initialized.
        """
        return self._code
