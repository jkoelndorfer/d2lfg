"""
bh.itemdisplay
==============

This module contains ItemDisplay-related interfaces.
"""

from abc import ABCMeta, abstractmethod

class ItemDisplayConditionable(metaclass=ABCMeta):
    """
    Base class for objects which can be used in a BH ItemDisplay filter.
    """

    @abstractmethod
    def item_display_condition(self) -> str:
        """
        Returns a string representing this object which is suitable for use
        in an ItemDisplay filter.

        ItemDisplay filters control which items an ItemDisplay applies to.
        """


class ItemDisplayOutputable(metaclass=ABCMeta):
    """
    Base class for objects which can be used in a BH ItemDisplay output
    (i.e. the name or description of an item).
    """

    @abstractmethod
    def item_display_output(self) -> str:
        """
        Returns a string representing this object which is suitable for use
        in an ItemDisplay output.

        ItemDisplay outputs control the item's name and description in game.
        """
