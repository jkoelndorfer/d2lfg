"""
``d2lfg.bh.lootfilter``
=======================

This module contains code that assists users in building a
BH maphack loot filter configuration.
"""

from io import StringIO
from textwrap import dedent as tw_dedent
from typing import Optional

from .config.configentry import (
    BHComment,
    BHEmptyLine,
    BHItemDisplay,
    BHItemDisplayFilterName,
)
from .config.configfile import BHConfigurationFile, BHConfigurationEncoding
from .config.itemdisplay.filterexpr import BHFilterExpression, BHFilterExpressionLiteral
from .config.itemdisplay.outputcode import BHOutputCode
from .config.itemdisplay.standardcodes import BHCoreCodes


class BHLootFilter:
    """
    Implementation of a BH maphack loot filter.

    :param name: the name of this loot filter
    :param continue_code: BH code that causes rule processing to continue
    """

    def __init__(
        self,
        name: str,
        continue_code: BHOutputCode = BHCoreCodes.CONTINUE,
    ) -> None:
        self.name = name
        self.continue_code = continue_code
        self._filtlvl = 0
        self._bh_config = BHConfigurationFile()

    def comment(self, comment_text: str, dedent: bool = False) -> None:
        """
        Adds a comment to the loot filter.

        :param comment_text: the text of the comment *without* leading "//"; \
            may be multiple lines
        :param dedent: if ``True``, comment text will be passed to \
            :py:meth:`~textwrap.dedent`
        """
        if dedent:
            c = tw_dedent(comment_text)
        else:
            c = comment_text
        self._bh_config.add(BHComment(c))

    def empty_lines(self, count: int) -> None:
        """
        Adds `count` empty lines to the loot filter.

        :param count: the number of empty lines to add
        """
        self._bh_config.add(BHEmptyLine(count))

    def filter_level(self, name: str) -> int:
        """
        Adds a filter level to the loot filter.

        :return: the integer value of the filter value usable in ``FILTLVL`` expressions
        """
        new_filtlvl_val = self._filtlvl
        self._bh_config.add(BHItemDisplayFilterName(name, new_filtlvl_val))
        self._filtlvl += 1
        return new_filtlvl_val

    def hide(self, filterexpr: BHFilterExpression) -> None:
        """
        Adds a rule to hide items matching the given ``filterexpr``.

        :param filterexpr: the filter expression used to match items
        """
        self.rule_raw(filterexpr.bhexpr(), "")

    def rule(
        self,
        filterexpr: BHFilterExpression,
        item_name: str,
        item_description: Optional[str],
        terminate: bool = False,
    ) -> None:
        """
        Adds a rule to the loot filter.

        :param filterexpr: the filter expression used to match items
        :param item_name: the displayed item name for items matching `condition`
        :param item_description: the displayed item description for items matching \
            `condition`
        :param terminate: if ``True``, rule processing will stop for items matching \
            this rule
        """
        o = StringIO()
        o.write(item_name)
        if item_description is not None:
            o.write("{")
            o.write(str(item_description))
            o.write("}")
        if not terminate:
            o.write(str(self.continue_code))

        output = o.getvalue()
        o.close()
        self.rule_raw(filterexpr.bhexpr(), output)

    def rule_raw(self, filter_str: str, output: str) -> None:
        """
        Adds a "raw" rule to the loot filter. This method can be used if
        the ItemDisplay configuration produced by ``rule`` is unsuitable
        for some reason.

        :param filter_str: the condition string used to match items
        :param output: the output of the rule
        """
        self._bh_config.add(
            BHItemDisplay(BHFilterExpressionLiteral(filter_str), output)
        )

    def render(self, encoding: BHConfigurationEncoding = "windows-1252") -> bytes:
        """
        Renders this loot filter's configuration.
        """
        return self._bh_config.render(encoding)
