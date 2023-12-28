"""
d2lfl.bh.codes.output
=====================

This module contains definitions for output codes, i.e.
codes that are used in the name or description of an
item.
"""

from enum import Enum


class BaseOutputCode(Enum):
    """
    Enumeration of standard BH item output codes.
    """
    #: Current value of the item's name (or description)
    #: as configured by previous loot filter rules using
    #: %CONTINUE%. Uses the item's default game values if
    #: they have not yet been modified.
    NAME = "%NAME%"

    #: The short code that is used to identify the item
    #: in game data files and loot filter rules.
    #: Possible values: lots! Usually a 3 or 4 character code,
    #: e.g. "ssd" for a short sword.
    #:
    #: See https://wiki.projectdiablo2.com/wiki/Item_Filtering#Item_Codes
    CODE = ITEM_CODE = "%CODE%"

    #: The item's item level ("ilvl").
    #: Possible values: integers 1 - 99, inclusive.
    ILVL = ITEM_LEVEL = "%ILVL%"

    #: The item's affix level ("alvl"). This determines
    #: what affixes a piece of gear can have.
    #: Possible values: integers 1 - 99, inclusive.
    ALVL = AFFIX_LEVEL = "%ALVL%"

    #: If the item is used in crafting, this will be the
    #: affix level of the crafting result.
    #: Possible values: integers 1 - 99, inclusive.
    CRAFTALVL = CRAFTING_AFFIX_LEVEL = "%CRAFTALVL%"

    #: The level requirement of the item.
    #: Possible values: integers 0 - 99, inclusive.
    LVLREQ = LEVEL_REQUIREMENT = "%LVLREQ%"

    #: The vendor price of the item.
    #: Possible values: integers 1 - 35000, inclusive.
    PRICE = VENDOR_PRICE = "%PRICE%"

    #: The number of items in the stack.
    #: Possible values: integers 1 - 350, inclusive.
    QTY = QUANTITY = "%QTY%"

    #: Melee weapon range.
    #: Possible values: integers 0 - 5, inclusive.
    RANGE = "%RANGE%"

    #: The if the item is a weapon, the speed modifier.
    #: Possible values: integers -60 - 20, inclusive.
    WPNSPD = WEAPON_SPEED = "%WPNSPD%"


class SocketableOutputCode(Enum):
    """
    Enumeration of output codes for socketables, i.e. gems and runes.
    """
    #: The rune number.
    #: Possible values: integers 1 - 33, inclusive.
    RUNENUM = RUNE_NUMBER = "%RUNENUM%"

    #: The rune's name, excluding "Rune".
    #: Possible values: "El", "Eld", "Tir", ...
    RUNENAME = RUNE_NAME = "%RUNENAME%"

    #: The gem's quality.
    #: Possible values: "Chipped", "Flawed", "Normal", "Flawless", "Perfect"
    GEMLEVEL = GEM_LEVEL = "%GEMLEVEL%"

    #: The type of gem.
    #: Possible values: "Amethyst", "Diamond", "Emerald", "Ruby",
    #:                  "Sapphire", "Topaz", "Skull"
    GEMTYPE = GEM_TYPE = "%GEMTYPE%"
