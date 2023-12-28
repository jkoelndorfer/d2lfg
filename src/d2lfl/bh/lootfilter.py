"""
d2lfl.bh.lootfilter
===================

This module contains BH lootfilter APIs intended for user consumption.
"""

from io import StringIO
from typing import Optional

from .config import BHConfiguration, BHItemDisplay, BHItemDisplayFilterName
from .expression import bh_and, bh_not, bh_or


class BHLootFilter:
    """
    Represents a BH maphack loot filter.
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self._filter_level_num = 0
        self._bh_config = BHConfiguration()

    def add_filter_level(self, name: str) -> int:
        """
        Adds a new filter level with the given `name`. Returns
        the integer value of the filter that is used in
        `FILTLVL` conditions.

        :param name: the name of the filter level
        """
        level_num = self._filter_level_num
        self._bh_config.add(BHItemDisplayFilterName(name))
        self._filter_level_num += 1
        return level_num

    def add_display_rule_raw(self, condition: str, output: str) -> None:
        """
        Adds a "raw" display rule to this loot filter.
        """
        self._bh_config.add(BHItemDisplay(condition, output))

    def add_display_rule(
        self,
        condition: str,
        name: str,
        description: Optional[str] = None,
        terminate: bool = False,
    ) -> None:
        """
        Adds a display rule to this loot filter.

        :param condition: the item matching condition
        :param name: the displayed item name
        :param description: the displayed item description
        :param terminate: if True, this display rule is terminal (the "%CONTINUE%" keyword is not included)
        """
        sio = StringIO()
        sio.write("{name}")
        if description is not None:
            sio.write("{{{description}}}")
        if not terminate:
            sio.write("%CONTINUE%")
        output = sio.getvalue().format(name=name, description=description)
        self.add_display_rule_raw(condition, output)

    @classmethod
    def eand(cls, *expressions: str) -> str:
        """
        Combines loot filter expressons using logical AND.
        """
        return bh_and(*expressions)

    @classmethod
    def eor(cls, *expressions: str) -> str:
        """
        Combines loot filter expressions using logical OR.
        """
        return bh_or(*expressions)

    @classmethod
    def enot(cls, expression: str) -> str:
        """
        Inverts a loot filter expression using logical NOT.
        """
        return bh_not(expression)

    def hide(self, condition: str) -> None:
        """
        Hides item matching the given `condition`.

        :param condition: the item matching condition
        """
        return self.add_display_rule_raw(condition=condition, output="")

    def render(self) -> bytes:
        """
        Renders this loot filter. The result can be written to a file and used
        as a BH maphack loot filter, assuming added conditions and outputs
        are valid.
        """
        return self._bh_config.render() + b"\n"
