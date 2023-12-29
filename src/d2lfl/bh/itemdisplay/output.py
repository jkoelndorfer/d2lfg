"""
d2lfl.bh.itemdisplay.output
===========================

This module contains definitions for BH output codes
which are *core to Diablo II* and whose meaning will
not vary between different mods.
"""

from .code import BHCode, BHFilterCode


class BHStandardCodes:
    """
    Class that defines BH standard output codes.

    See https://wiki.projectdiablo2.com/wiki/Item_Filtering#Value_References
    """

    #: Current value of the item's name (or description)
    #: as configured by previous loot filter rules using
    #: %CONTINUE%. Uses the item's default game values if
    #: they have not yet been modified.
    NAME = BHCode("NAME")

    #: Code indicating that ItemDisplay rule processing
    #: should continue with the next matching rule.
    #: If this code is absent and the rule matches, rule
    #: processing terminates.
    CONTINUE = BHCode("CONTINUE")

    #: The character's current level.
    #: Possible values: integers 1 - 99, inclusive.
    CLVL = CHARACTER_LEVEL = BHFilterCode("CLVL")

    #: The current difficulty.
    #: Possible values: 0 - 2, inclusive.
    #: 0 = Normal, 1 = Nightmare, 2 = Hell.
    DIFF = DIFFICULTY = BHFilterCode("DIFF")

    #: The level requirement of the item.
    #: Possible values: integers 0 - 99, inclusive.
    LVLREQ = LEVEL_REQUIREMENT = BHFilterCode("LVLREQ")


class BHItemCodes:
    """
    Class that defines BH output codes for items.
    """

    #: The short code that is used to identify the item
    #: in game data files and loot filter rules.
    #: Possible values: lots! Usually a 3 or 4 character code,
    #: e.g. "ssd" for a short sword.
    #:
    #: See https://wiki.projectdiablo2.com/wiki/Item_Filtering#Item_Codes
    CODE = ITEM_CODE = BHCode("CODE")

    #: The number of items in the stack.
    #: Possible values: integers 1 - 350, inclusive.
    QTY = QUANTITY = BHFilterCode("QTY")

    #: The vendor price of the item.
    #: Possible values: integers 1 - 35000, inclusive.
    PRICE = VENDOR_PRICE = BHFilterCode("PRICE")

    #: Amount of gold in a gold pile.
    #: Per https://wiki.projectdiablo2.com/wiki/Item_Filtering#Info_Codes,
    #: gold's "item name" may not be modified.
    #: Possible values: positive integers.
    GOLD = BHFilterCode("GOLD")


class BHEquipmentCodes:
    """
    Class that defines BH output codes for equippable items.
    """

    #: The item's item level ("ilvl").
    #: Possible values: integers 1 - 99, inclusive.
    ILVL = ITEM_LEVEL = BHFilterCode("ILVL")

    #: The item's affix level ("alvl"). This determines
    #: what affixes a piece of gear can have.
    #: Possible values: integers 1 - 99, inclusive.
    ALVL = AFFIX_LEVEL = BHFilterCode("ALVL")

    #: The item's quality level.
    #: TODO: Possible values
    QLVL = QUALITY_LEVEL = BHFilterCode("QLVL")

    #: If the item is used in crafting, this will be the
    #: affix level of the crafting result.
    #: Possible values: integers 1 - 99, inclusive.
    CRAFTALVL = CRAFTING_AFFIX_LEVEL = BHFilterCode("CRAFTALVL")

    #: Melee weapon range.
    #: Possible values: integers 0 - 5, inclusive.
    RANGE = BHFilterCode("RANGE")

    #: The if the item is a weapon, the speed modifier.
    #: Possible values: integers -60 - 20, inclusive.
    WPNSPD = WEAPON_SPEED = BHFilterCode("WPNSPD")



class BHColorCodes:
    """
    Class that defines BH output color codes.

    See https://wiki.projectdiablo2.com/wiki/Item_Filtering#Colors.
    """
    #: Used by default for regular, non-magic items
    #: which ARE NOT socketed or ethereal.
    WHITE = BHCode("WHITE")

    #: Used by default for regular, non-magic items
    #: which ARE socketed or ethereal.
    GRAY = BHCode("GRAY")

    #: Used by default for magic items.
    BLUE = BHCode("BLUE")

    #: Used by default for rare items
    YELLOW = BHCode("YELLOW")

    #: Used by default for unique items and runewords.
    GOLD = BHCode("GOLD")

    #: Used by default for set items.
    GREEN = BHCode("GREEN")

    #: Not used by default.
    DARK_GREEN = BHCode("DARK_GREEN")

    #: Not used by default.
    TAN = BHCode("TAN")

    #: Not used by default.
    BLACK = BHCode("BLACK")

    #: Not used by default.
    PURPLE = BHCode("PURPLE")

    #: Used by default for broken and unusable items.
    RED = BHCode("RED")

    #: Used by default for crafted items, endgame quest
    #: items, and runes.
    ORANGE = BHCode("ORANGE")

    #: This color is custom and only works in 3dfx (Glide) mode.
    CORAL = BHCode("CORAL")

    #: This color is custom and only works in 3dfx (Glide) mode.
    SAGE = BHCode("SAGE")

    #: This color is custom and only works in 3dfx (Glide) mode.
    TEAL = BHCode("TEAL")

    #: This color is custom and only works in 3dfx (Glide) mode.
    LIGHT_GRAY = BHCode("LIGHT_GRAY")
