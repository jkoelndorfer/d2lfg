"""
``d2lfg.bh.config.itemdisplay.d2types``
=======================================

This module contains compositions of types defined in :py:mod:`~d2lfg.d2core.d2types`
with BH ItemDisplay filter expressions and output codes.

These composed types allow for users to interact with a single object that
represents an in-game concept, access its properties, and also use that object
to define BH filter expressions and outputs.

Game databases should return types defined in this file.
"""

from ....d2core.d2types.item import Diablo2Item
from ....d2core.d2types.playerclass import Diablo2PlayerClass
from .filterexpr import BHFilterExpression


class BHDiablo2Item(BHFilterExpression, Diablo2Item):
    """
    A :py:class:`~d2lfg.d2core.d2types.item.Diablo2Item` that is also
    a :py:class:`~d2lfg.bh.config.itemdisplay.filterexpr.BHFilterExpression`.
    """

    def bhexpr(self) -> str:
        """
        Returns a BH filter expression string that will match the item by its code.
        """
        return self.code


class BHDiablo2CurrentPlayerClass(BHFilterExpression, Diablo2PlayerClass):
    """
    A :py:class:`~d2lfg.d2core.d2types.playerclass.Diablo2PlayerClass` that is also
    a :py:class:`~d2lfg.bh.config.itemdisplay.filterexpr.BHFilterExpression`.

    As a filter expression it filters based on the *class of the currently
    playing character*.
    """

    def bhexpr(self) -> str:
        """
        Returns a BH filter expression string that will match the class of the
        currently playing character.
        """
        return self.name


class BHDiablo2PlayerClassItemRestriction(BHFilterExpression, Diablo2PlayerClass):
    """
    A :py:class:`~d2lfg.d2core.d2types.playerclass.Diablo2PlayerClass` that is also
    a :py:class:`~d2lfg.bh.config.itemdisplay.filterexpr.BHFilterExpression`.

    As a filter expression it filters based on the *class restriction of the
    dropped item*.
    """

    def bhexpr(self) -> str:
        """
        Returns a BH filter expression string that will match an item based
        on its class restriction.
        """
        return self.code
