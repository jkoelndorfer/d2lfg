"""
``tests.bh.config.test_configentry``
====================================

This module contains test code for :py:mod:`d2lfg.bh.config.configentry`.
"""

import pytest

from d2lfg.bh.config.itemdisplay.filterexpr import BHFilterExpressionLiteral as L
from d2lfg.bh.config.configentry import (
    BHComment,
    BHEmptyLine,
    BHItemDisplay,
    BHItemDisplayFilterName,
    BHLiteralText,
)


class TestBHComment:
    """
    Tests :py:class:`~d2lfg.bh.config.configentry.BHComment`.
    """

    def test_ignored(self) -> None:
        """
        Verifies that comments are ignored.
        """
        assert BHComment("test comment").ignored

    def test_render_single_line(self) -> None:
        """
        Verifies that single line comments are rendered correctly.
        """
        comment_text = "d2lfg -- single line comment test"
        comment = BHComment(comment_text)

        assert comment.render() == f"// {comment_text}\n"

    def test_render_multi_line(self) -> None:
        """
        Verifies that comments spanning multiple lines are rendered correctly.
        """
        comment_line_1 = "d2lfg -- comment line 1"
        comment_line_2 = "comment line 2 for d2lfg test"
        comment_text = "\n".join([comment_line_1, comment_line_2])
        comment = BHComment(comment_text)

        assert comment.render() == f"// {comment_line_1}\n// {comment_line_2}\n"

    def test_multi_line_no_trailing_whitespace(self) -> None:
        """
        Verifies that comments spanning multiple lines do not have trailing whitespace.
        """
        comment = BHComment("line 1  \nline 2 ")

        assert comment.render() == "// line 1\n// line 2\n"

    def test_multi_line_empty_no_trailing_whitespace(self) -> None:
        """
        Verifies that an empty comment spanning multiple lines does not have trailing
        whitespace.
        """
        comment = BHComment(" \n  ")

        assert comment.render() == "//\n//\n"

    def test_single_line_empty_no_trailing_whitespace(self) -> None:
        """
        Verifies that a single line empty comment does not have trailing whitespace.
        """
        comment = BHComment("")

        assert comment.render() == "//\n"

    def test_single_line_no_trailing_whitespace(self) -> None:
        """
        Verifies that a single line comment does not end with trailing whitespace.
        """
        comment = BHComment("comment text ")

        assert comment.render() == "// comment text\n"


class TestBHEmptyLine:
    """
    Tests :py:class:`~d2lfg.bh.config.configentry.BHEmptyLine`.
    """

    def test_ignored(self) -> None:
        """
        Verifies that empty lines are ignored.
        """
        assert BHEmptyLine(1).ignored

    @pytest.mark.parametrize("count", [0, 1, 2, 3])
    def test_render(self, count: int) -> None:
        """
        Verifies that empty lines are rendered correctly.
        """
        assert BHEmptyLine(count).render() == "\n" * count


class TestBHLiteralText:
    """
    Tests :py:class:`~d2lfg.bh.config.configentry.BHLiteralText`.
    """

    def test_ignored(self) -> None:
        """
        Verifies that literal text is not ignored.
        """
        assert not BHLiteralText("TestConfig").ignored

    @pytest.mark.parametrize(
        "text",
        [
            "ItemDisplay[amu]: amulet\n",
            "// comment text\n",
            "InlineWithNoNewline",
        ],
    )
    def test_render(self, text: str) -> None:
        """
        Verifies that literal text is rendered correctly.
        """

        assert BHLiteralText(text).render() == text


class TestBHItemDisplay:
    """
    Tests :py:class:`~d2lfg.bh.config.configentry.BHItemDisplay`.
    """

    def test_ignored(self) -> None:
        """
        Verifies that BHItemDisplay entries are not ignored.
        """
        item_display = BHItemDisplay(L("amu"), "Amulet")

        assert not item_display.ignored

    @pytest.mark.parametrize(
        "filterexpr, output",
        [
            (L("amu"), "Amulet"),
            (L("box"), "Horadric Cube"),
        ],
    )
    def test_render(self, filterexpr: L, output: str) -> None:
        """
        Verifies that BHItemDisplay entries are rendered correctly.
        """
        f, o = filterexpr, output
        item_display = BHItemDisplay(f, o)
        expected = f"ItemDisplay[{f.bhexpr()}]: {o}\n"

        assert item_display.render() == expected

    def test_render_empty_output(self) -> None:
        """
        Verifies that BHItemDisplay entries with empty output do not have
        trailing whitespace.
        """
        item_display = BHItemDisplay(L("GOLD<100"), "")

        assert item_display.render() == "ItemDisplay[GOLD<100]:\n"


class TestBHItemDisplayFilterName:
    """
    Tests :py:class:`~d2lfg.bh.config.configentry.BHItemDisplayFilterName`.
    """

    def test_ignored(self) -> None:
        """
        Verifies that BHItemDisplayFilterName entries are not ignored.
        """
        filter_name = BHItemDisplayFilterName("Hide Trash", 0)

        assert not filter_name.ignored

    @pytest.mark.parametrize(
        "filter_name, filtlvl",
        [
            ("Show All Items", 0),
            ("Hide Trash", 1),
            ("Show Decent Stuff", 2),
        ],
    )
    def test_render(self, filter_name: str, filtlvl: int) -> None:
        """
        Verifies that BHItemDisplayFilterNames are rendered correctly.
        """

        filter = BHItemDisplayFilterName(filter_name, filtlvl)

        assert filter.render() == f"ItemDisplayFilterName[]: {filter_name}\n"
