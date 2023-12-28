"""
d2lfl.lootfilter
================

This module contains APIs intended for user consumption.
"""

from io import StringIO
from typing import Optional

from .bh import BHConfiguration, BHItemDisplay, BHItemDisplayFilterName


class LootFilter:
    """
    Represents a loot filter.
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
        if description is None:
            sio.write("{{{description}}}")
        if not terminate:
            sio.write("%CONTINUE%")
        item_display_output = sio.getvalue().format(name=name, description=description)
        self._bh_config.add(BHItemDisplay(condition, item_display_output))

    def hide(self, condition: str) -> None:
        """
        Hides item matching the given `condition`.

        :param condition: the item matching condition
        """
        return self.add_display_rule(condition=condition, name="", description=None, terminate=True)

    def render(self) -> bytes:
        """
        Renders this loot filter. The result can be written to a file and used
        as a BH maphack loot filter, assuming added conditions and outputs
        are valid.
        """
        return self._bh_config.render() + b"\n"
