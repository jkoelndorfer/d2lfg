"""
``tests.bh.test_lootfilter``
============================

This module contains test code for :py:mod:`d2lfg.bh.lootfilter`.
"""

from textwrap import dedent

import pytest

from d2lfg.bh.config.configfile import BHConfigurationEncoding
from d2lfg.bh.config.itemdisplay.filterexpr import (
    BHFilterExpression,
    BHFilterExpressionLiteral,
)
from d2lfg.bh.config.itemdisplay.standardcodes import BHCodes
from d2lfg.bh.lootfilter import BHLootFilter


@pytest.fixture
def encoding() -> BHConfigurationEncoding:
    return "windows-1252"


@pytest.fixture
def filterexpr() -> BHFilterExpression:
    return BHFilterExpressionLiteral("UNID")


@pytest.fixture
def loot_filter() -> BHLootFilter:
    return BHLootFilter("test_lootfilter")


class TestBHLootFilter:
    """
    Tests :py:class:`~d2lfg.bh.lootfilter.BHLootFilter`.
    """

    def test_comment(
        self, loot_filter: BHLootFilter, encoding: BHConfigurationEncoding
    ) -> None:
        """
        Validates that comments are correctly added to loot filters.
        """
        comment_text = "TestBHLootFilter comment"
        loot_filter.comment(comment_text)

        assert loot_filter.render(encoding) == f"// {comment_text}\n".encode(encoding)

    def test_comment_no_dedent(
        self, loot_filter: BHLootFilter, encoding: BHConfigurationEncoding
    ) -> None:
        """
        Validates that multiline comments are correctly added to loot filters
        with dedent turned off.
        """
        comment_text = "  comment line 1\n  comment line 2"
        expected_comment = "//   comment line 1\n//   comment line 2\n"

        loot_filter.comment(comment_text, dedent=False)

        assert loot_filter.render(encoding) == expected_comment.encode(encoding)

    def test_comment_with_dedent(
        self, loot_filter: BHLootFilter, encoding: BHConfigurationEncoding
    ) -> None:
        """
        Validates that multiline comments are correctly added to loot filters
        with dedent turned on.
        """
        comment_text = "  comment line 1\n  comment line 2"
        expected_comment = "// comment line 1\n// comment line 2\n"

        loot_filter.comment(comment_text, dedent=True)

        assert loot_filter.render(encoding) == expected_comment.encode(encoding)

    def test_empty_lines(
        self, loot_filter: BHLootFilter, encoding: BHConfigurationEncoding
    ) -> None:
        """
        Validates that empty lines are correctly added to loot filters.
        """
        expected_filter = dedent(
            """
            // comment 1



            // comment 2
            """
        ).lstrip()

        loot_filter.comment("comment 1")
        loot_filter.empty_lines(3)
        loot_filter.comment("comment 2")

        assert loot_filter.render(encoding) == expected_filter.encode(encoding)

    def test_filter_lvl_increments(self, loot_filter: BHLootFilter) -> None:
        """
        Validates the returned filter level increments each time a new filter level
        is added.
        """
        show_all_lvl = loot_filter.filter_level("Show All Items")
        hide_trash_lvl = loot_filter.filter_level("Hide Trash Items")
        show_good_lvl = loot_filter.filter_level("Show Good Items")

        assert show_all_lvl == 0
        assert hide_trash_lvl == 1
        assert show_good_lvl == 2

    def test_filter_lvl_added(
        self, loot_filter: BHLootFilter, encoding: BHConfigurationEncoding
    ) -> None:
        """
        Validates that loot filter levels are correctly added to loot filters.
        """
        filter_name = "Show All Items"
        expected_filter = f"ItemDisplayFilterName[]: {filter_name}\n"

        loot_filter.filter_level(filter_name)

        assert loot_filter.render(encoding) == expected_filter.encode(encoding)

    def test_hide(
        self,
        loot_filter: BHLootFilter,
        encoding: BHConfigurationEncoding,
        filterexpr: BHFilterExpression,
    ) -> None:
        """
        Validates that item hide rules are correctly added to loot filters.
        """
        expected_filter = f"ItemDisplay[{filterexpr.bhexpr()}]:\n"
        loot_filter.hide(filterexpr)

        assert loot_filter.render(encoding) == expected_filter.encode(encoding)

    def test_rule_terminate(
        self,
        loot_filter: BHLootFilter,
        encoding: BHConfigurationEncoding,
        filterexpr: BHFilterExpression,
    ) -> None:
        """
        Validates that terminating item rules are correctly added to loot filters.
        """
        filter_s = filterexpr.bhexpr()
        name = "My Test Item"
        description = "+10 Strength%NL%+10 Dexterity"
        expected_filter = f"ItemDisplay[{filter_s}]: {name}{{{description}}}\n"

        loot_filter.rule(filterexpr, name, description, terminate=True)

        assert loot_filter.render(encoding) == expected_filter.encode(encoding)

    def test_rule_nonterminating(
        self,
        loot_filter: BHLootFilter,
        encoding: BHConfigurationEncoding,
        filterexpr: BHFilterExpression,
    ) -> None:
        """
        Validates that non-terminating item rules are correctly added to loot filters.
        """
        filter_s = filterexpr.bhexpr()
        cc = loot_filter.continue_code
        name = "My Test Item"
        description = "+10 Strength%NL%+10 Dexterity"
        expected_filter = f"ItemDisplay[{filter_s}]: {name}{{{description}}}{cc}\n"

        loot_filter.rule(filterexpr, name, description, terminate=False)

        assert loot_filter.render(encoding) == expected_filter.encode(encoding)

    def test_rule_raw(
        self,
        loot_filter: BHLootFilter,
        encoding: BHConfigurationEncoding,
    ) -> None:
        """
        Validates that raw rules are correctly added to loot filters.
        """
        filter_s = "UNID"
        output_s = "Test Item{+10 Strength}"
        expected_filter = f"ItemDisplay[{filter_s}]: {output_s}\n"

        loot_filter.rule_raw(filter_s, output_s)

        assert loot_filter.render(encoding) == expected_filter.encode(encoding)

    def test_complex_loot_filter(
        self,
        loot_filter: BHLootFilter,
        encoding: BHConfigurationEncoding,
    ) -> None:
        """
        Validates that a complex loot filter is correctly rendered.
        """
        lf = loot_filter
        expected_loot_filter = dedent(
            """
            // d2lfg test_complex_loot_filter
            //
            // Validates rendering of a complex loot filter.

            ItemDisplayFilterName[]: Show All Items
            ItemDisplayFilterName[]: Hide Trash Items
            ItemDisplayFilterName[]: Show Good Items


            ItemDisplay[box]: %NAME%{d2lfg test_complex_loot_filter}
            ItemDisplay[GOLD<100]:
            """
        ).lstrip()

        lf.comment(
            """
            d2lfg test_complex_loot_filter

            Validates rendering of a complex loot filter.
            """,
            dedent=True,
        )
        lf.empty_lines(1)
        lf.filter_level("Show All Items")
        lf.filter_level("Hide Trash Items")
        lf.filter_level("Show Good Items")
        lf.empty_lines(2)
        lf.rule_raw("box", "%NAME%{d2lfg test_complex_loot_filter}")
        lf.hide(BHCodes.GOLD.lt(100))

        assert loot_filter.render(encoding) == expected_loot_filter.encode(encoding)
