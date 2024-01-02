"""
d2lfl.bh.itemdisplay.codes
==========================

This module contains definitions for BH output codes
which are *core to Diablo II* and whose meaning will
not vary between different mods.
"""

from .codetype import BHCode, BHFilterCode
from .expression import BHLiteralExpression as BHExpr


class _BHStandardCodes:
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

    #: Code that inserts a newline.
    NL = BHCode("NL")


class _BHMutableCodes:
    """
    Class that contain codes whose values are "mutable", i.e.
    depend on the state of the game, not just the item.
    """
    #: Current character is an amazon.
    AMAZON = BHExpr("AMAZON")

    #: Current character is an assassin.
    ASSASSIN = BHExpr("ASSASSIN")

    #: Current character is a barbarian.
    BARBARIAN = BHExpr("BARBARIAN")

    #: Current character is a druid.
    DRUID = BHExpr("DRUID")

    #: Current character is a necromancer.
    NECROMANCER = BHExpr("NECROMANCER")

    #: Current character is a paladin.
    PALADIN = BHExpr("PALADIN")

    #: Current character is a sorceress.
    SORCERESS = BHExpr("SORCERESS")

    #: Item is in a merchant's shop window.
    SHOP = BHExpr("SHOP")

    #: Item is currently equipped by the character.
    EQUIPPED = BHExpr("EQUIPPED")

    #: The character's current level.
    #: Possible values: integers 1 - 99, inclusive.
    CLVL = CHARACTER_LEVEL = BHFilterCode("CLVL")

    #: The current difficulty.
    #: Possible values: 0 - 2, inclusive.
    #: 0 = Normal, 1 = Nightmare, 2 = Hell.
    DIFF = DIFFICULTY = BHFilterCode("DIFF")


class _BHItemCodes:
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

    #: The level requirement of the item.
    #: Possible values: integers 0 - 99, inclusive.
    LVLREQ = LEVEL_REQUIREMENT = BHFilterCode("LVLREQ")

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

    #: Items of non-magic quality.
    NMAG = NON_MAGIC = BHExpr("NMAG")

    #: Items of magic quality.
    MAG = MAGIC = BHExpr("MAG")

    #: Items of rare quality.
    RARE = BHExpr("RARE")

    #: Items of unique quality.
    UNI = UNIQUE = BHExpr("UNI")

    #: Items of set quality.
    SET = BHExpr("SET")

    #: Items of crafted quality.
    #: These are only created through Horadric Cube recipes.
    CRAFT = CRAFTED = BHExpr("CRAFT")


class _BHEquipmentCodes:
    """
    Class that defines BH output codes for equippable items.
    """

    #: Whether the item is ethereal.
    #: *ETH CANNOT BE USED IN ITEM TEXT*!
    ETH = ETHEREAL = BHExpr("ETH")

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

    #: Item is of the "normal" tier. This is the lowest tier.
    NORM = NORMAL = BHExpr("NORM")

    #: Item is of the "exceptional" tier. This is the tier above normal.
    EXC = EXCEPTIONAL = BHExpr("EXC")

    #: Item is of the "elite" tier. This is the highest tier.
    ELT = ELITE = BHExpr("ELT")

    #: Item is a helm. This includes class-specific helms.
    EQ1 = HELM = BHExpr("HELM")

    #: Item is a chest armor.
    EQ2 = CHEST = BHExpr("CHEST")

    #: Item is a shield. This includes class-specific shields.
    EQ3 = SHIELD = BHExpr("SHIELD")

    #: Item is a pair of gloves.
    EQ4 = GLOVES = BHExpr("GLOVES")

    #: Item is a pair of boots.
    EQ5 = BOOTS = BHExpr("BOOTS")

    #: Item is a belt.
    EQ6 = BELT = BHExpr("BELT")

    #: Item is a circlet.
    EQ7 = CIRC = CIRCLET = BHExpr("CIRC")

    #: Item is any armor. This includes class-specific armor.
    ARMOR = BHExpr("ARMOR")

    #: Item is an axe. This includes throwing axes.
    WP1 = AXE = BHExpr("AXE")

    #: Item is a mace.
    WP2 = MACE = BHExpr("MACE")

    #: Item is a sword.
    WP3 = SWORD = BHExpr("SWORD")

    #: Item is a dagger. This includes throwing knives.
    WP4 = DAGGER = BHExpr("DAGGER")

    #: Item is a throwing item. Includes throwing knives, axes, javelins, and potions.
    WP5 = THROWING = BHExpr("THROWING")

    #: Item is a javelin. Includes Amazon-only javelins.
    WP6 = JAV = JAVELIN = BHExpr("JAV")

    #: Item is a spear. Includes Amazon-only spears.
    WP7 = SPEAR = BHExpr("SPEAR")

    #: Item is a polearm.
    WP8 = POLEARM = BHExpr("POLEARM")

    #: Item is a bow. Includes Amazon-only bows.
    WP9 = BOW = BHExpr("BOW")

    #: Item is a crossbow.
    WP10 = XBOW = CROSSBOW = BHExpr("XBOW")

    #: Item is a staff.
    WP11 = STAFF = BHExpr("STAFF")

    #: Item is a wand.
    WP12 = WAND = BHExpr("WAND")

    #: Item is a scepter.
    WP13 = SCEPTER = BHExpr("SCEPTER")

    #: Item is a weapon.
    WEAPON = BHExpr("WEAPON")

    #: Item is a one-handed weapon.
    WEAPON_1H = BHExpr("1H")  # attribute names cannot start with an integer

    #: Item is a two-handed weapon.
    WEAPON_2H = BHExpr("2H") # attribute names cannot start with an integer

    #: Item is a club (a subtype of mace).
    CLUB = BHExpr("CLUB")

    #: Item is a tipped mace (a subtype of mace).
    TMACE = TIPPED_MACE = BHExpr("TMACE")

    #: Item is a hammer (a subtype of mace).
    HAMMER = BHExpr("HAMMER")

    #: Item is restricted to druids only (druid pelts).
    CL1 = DRU = DRUID_ONLY = BHExpr("DRU")

    #: Item is restricted to barbarians only (barbarian helms).
    CL2 = BAR = BARBARIAN_ONLY = BHExpr("BAR")

    #: Item is restricted to paladins only (paladin shields).
    CL3 = DIN = PALADIN_ONLY = BHExpr("DIN")

    #: Item is restricted to necromancers only (necromancer shields).
    CL4 = NEC = NECROMANCER_ONLY = BHExpr("NEC")

    #: Item is restricted to assassins only (assassin weapons).
    CL5 = SIN = ASSASSIN_ONLY = BHExpr("SIN")

    #: Item is restricted to sorceresses only (sorceress weapons).
    CL6 = SOR = SORCERESS_ONLY = BHExpr("SOR")

    #: Item is restricted to amazons only (amazon weapons).
    CL7 = ZON = AMAZON_ONLY = BHExpr("ZON")

    #: Item is class-restricted. Includes all class-restricted items.
    CLASS = CLASS_RESTRICTED = BHExpr("CLASS")


class _BHColorCodes:
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


class BHCodes(
    _BHStandardCodes,
    _BHMutableCodes,
    _BHItemCodes,
    _BHEquipmentCodes,
    _BHColorCodes,
):
    """
    Composite class that contains all BH codes that are not mod-specific.
    """
