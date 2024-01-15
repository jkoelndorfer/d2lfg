"""
``tests.bh.config.test_configfile``
===================================

This module contains test code for :py:mod:`d2lfg.bh.config.configfile`.
"""

from textwrap import dedent

import pytest

from tests.testhelper.typing import FixtureRequest

from d2lfg.bh.config.configentry import (
    BHComment,
    BHEmptyLine,
    BHItemDisplay,
    BHItemDisplayFilterName,
)
from d2lfg.bh.config.configfile import BHConfigurationFile, BHConfigurationEncoding
from d2lfg.bh.config.itemdisplay.filterexpr import BHFilterExpressionLiteral as FL
from d2lfg.bh.config.itemdisplay.standardcodes import BHCodes


@pytest.fixture
def configfile() -> BHConfigurationFile:
    return BHConfigurationFile()


@pytest.fixture(params=["windows-1252", "utf-8"])
def encoding(
    request: FixtureRequest[BHConfigurationEncoding],
) -> BHConfigurationEncoding:
    return request.param


class TestBHConfigurationFile:
    """
    Tests :py:class:`~d2lfg.bh.config.configfile.BHConfigurationFile`.
    """

    def test_render_01(
        self, configfile: BHConfigurationFile, encoding: BHConfigurationEncoding
    ) -> None:
        """
        Validates that a config file renders as expected with the given
        configuration entries.
        """

        # Note: ¿ is a character that is encoding differently in UTF-8 than
        # it is in windows-1252, so this test will detect if the file
        # is not rendered using the correct encoding.
        expected_config = dedent(
            """
            // this is
            // test render case 01
            ItemDisplayFilterName[]: Show All Items
            ItemDisplayFilterName[]: Hide Trash Items

            ItemDisplay[!ID]: ID¿: %NAME%
            """
        ).lstrip()

        configfile.add(BHComment("this is\ntest render case 01"))
        configfile.add(BHItemDisplayFilterName("Show All Items", 0))
        configfile.add(BHItemDisplayFilterName("Hide Trash Items", 1))
        configfile.add(BHEmptyLine(1))
        configfile.add(BHItemDisplay(FL("!ID"), f"ID¿: {BHCodes.NAME}"))

        assert configfile.render(encoding) == expected_config.encode(encoding)
