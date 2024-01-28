"""
``d2lfg.bh.config.itemdisplay.standardcodes``
=============================================

This module contains standard BH ItemDisplay filter expressions, output codes,
and filter output codes. These are not strongly tied to game data, rather they
are a core part of BH ItemDisplay filtering and output.

See `Project Diablo 2's item filtering page
<https://wiki.projectdiablo2.com/wiki/Item_Filtering>`.
"""

from ....d2core.d2types.playerclass import Diablo2PlayerClasses as PC
from .d2types import (
    BHDiablo2CurrentPlayerClass as CurClass,
    BHDiablo2PlayerClassItemRestriction as ClassRestricted,
)
from .filterexpr import BHFilterExpressionLiteral as F
from .filteroutputcode import BHFilterOutputCodeLiteral as FC
from .outputcode import BHOutputCodeLiteral as C


class BHCoreCodes:
    """
    This class contains core BH codes.
    """

    #: Current value of the item's name (or description)
    #: as configured by previous loot filter rules using
    #: %CONTINUE%. Uses the item's default game values if
    #: they have not yet been modified.
    NAME = C("NAME")

    #: Code indicating that ItemDisplay rule processing
    #: should continue with the next matching rule.
    #: If this code is absent and the rule matches, rule
    #: processing terminates.
    CONTINUE = C("CONTINUE")

    #: Code that inserts a newline.
    NL = C("NL")


class BHMutableCodes:
    """
    Class that contain codes whose values are "mutable", i.e.
    depend on the state of the game, not just the item.
    """

    #: Current character is an amazon.
    AMAZON = CurClass.copy(PC.AMAZON)

    #: Current character is an assassin.
    ASSASSIN = CurClass.copy(PC.ASSASSIN)

    #: Current character is a barbarian.
    BARBARIAN = CurClass.copy(PC.BARBARIAN)

    #: Current character is a druid.
    DRUID = CurClass.copy(PC.DRUID)

    #: Current character is a necromancer.
    NECROMANCER = CurClass.copy(PC.NECROMANCER)

    #: Current character is a paladin.
    PALADIN = CurClass.copy(PC.PALADIN)

    #: Current character is a sorceress.
    SORCERESS = CurClass.copy(PC.SORCERESS)

    #: Item is in a merchant's shop window.
    SHOP = F("SHOP")

    #: Item is currently equipped by the character.
    EQUIPPED = F("EQUIPPED")

    #: The character's current level.
    #: Possible values: integers 1 - 99, inclusive.
    CLVL = CHARACTER_LEVEL = FC("CLVL")

    #: The current difficulty.
    #: Possible values: 0 - 2, inclusive.
    #: 0 = Normal, 1 = Nightmare, 2 = Hell.
    DIFF = DIFFICULTY = F("DIFF")


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
    CODE = ITEM_CODE = C("CODE")

    #: The level requirement of the item.
    #: Possible values: integers 0 - 99, inclusive.
    LVLREQ = LEVEL_REQUIREMENT = FC("LVLREQ")

    #: The number of items in the stack.
    #: Possible values: integers 1 - 350, inclusive.
    QTY = QUANTITY = FC("QTY")

    #: The vendor price of the item.
    #: Possible values: integers 1 - 35000, inclusive.
    PRICE = VENDOR_PRICE = FC("PRICE")

    #: Amount of gold in a gold pile.
    #: Per https://wiki.projectdiablo2.com/wiki/Item_Filtering#Info_Codes,
    #: gold's "item name" may not be modified.
    #: Possible values: positive integers.
    GOLD = FC("GOLD")  # NOTE: It's a "filter code" here because GOLD is a color code.

    #: Items of non-magic quality.
    NMAG = NON_MAGIC = F("NMAG")

    #: Items of magic quality.
    MAG = MAGIC = F("MAG")

    #: Items of rare quality.
    RARE = F("RARE")

    #: Items of unique quality.
    UNI = UNIQUE = F("UNI")

    #: Items of set quality.
    SET = F("SET")

    #: Items of crafted quality.
    #: These are only created through Horadric Cube recipes.
    CRAFT = CRAFTED = F("CRAFT")

    #: Item is identified.
    ID = IDENTIFIED = F("ID")


class BHColorCodes:
    """
    Class that defines BH output color codes.

    See https://wiki.projectdiablo2.com/wiki/Item_Filtering#Colors.
    """

    #: Used by default for regular, non-magic items
    #: which ARE NOT socketed or ethereal.
    WHITE = C("WHITE")

    #: Used by default for regular, non-magic items
    #: which ARE socketed or ethereal.
    GRAY = C("GRAY")

    #: Used by default for magic items.
    BLUE = C("BLUE")

    #: Used by default for rare items
    YELLOW = C("YELLOW")

    #: Used by default for unique items and runewords.
    GOLD = FC("GOLD")  # NOTE: It's a filter code here because GOLD is a valid filter.

    #: Used by default for set items.
    GREEN = C("GREEN")

    #: Not used by default.
    DARK_GREEN = C("DARK_GREEN")

    #: Not used by default.
    TAN = C("TAN")

    #: Not used by default.
    BLACK = C("BLACK")

    #: Not used by default.
    PURPLE = C("PURPLE")

    #: Used by default for broken and unusable items.
    RED = C("RED")

    #: Used by default for crafted items, endgame quest
    #: items, and runes.
    ORANGE = C("ORANGE")

    #: This color is custom and only works in 3dfx (Glide) mode.
    CORAL = C("CORAL")

    #: This color is custom and only works in 3dfx (Glide) mode.
    SAGE = C("SAGE")

    #: This color is custom and only works in 3dfx (Glide) mode.
    TEAL = C("TEAL")

    #: This color is custom and only works in 3dfx (Glide) mode.
    LIGHT_GRAY = C("LIGHT_GRAY")


class BHEquipmentCodes:
    """
    Class that defines BH output codes for equippable items.
    """

    #: The item's item level ("ilvl").
    #: Possible values: integers 1 - 99, inclusive.
    ILVL = ITEM_LEVEL = FC("ILVL")

    #: The item's affix level ("alvl"). This determines
    #: what affixes a piece of gear can have.
    #: Possible values: integers 1 - 99, inclusive.
    ALVL = AFFIX_LEVEL = FC("ALVL")

    #: The item's quality level.
    #: TODO: Possible values
    QLVL = QUALITY_LEVEL = FC("QLVL")

    #: If the item is used in crafting, this will be the
    #: affix level of the crafting result.
    #: Possible values: integers 1 - 99, inclusive.
    CRAFTALVL = CRAFTING_AFFIX_LEVEL = FC("CRAFTALVL")

    #: Melee weapon range.
    #: Possible values: integers 0 - 5, inclusive.
    RANGE = FC("RANGE")

    #: The if the item is a weapon, the speed modifier.
    #: Possible values: integers -60 - 20, inclusive.
    WPNSPD = WEAPON_SPEED = FC("WPNSPD")

    #: Item is of the "normal" tier. This is the lowest tier.
    NORM = NORMAL = F("NORM")

    #: Item is of the "exceptional" tier. This is the tier above normal.
    EXC = EXCEPTIONAL = F("EXC")

    #: Item is of the "elite" tier. This is the highest tier.
    ELT = ELITE = F("ELT")

    #: Whether the item is ethereal.
    ETH = ETHEREAL = F("ETH")

    #: Item is of inferior quality.
    INF = INFERIOR = F("INF")

    #: Item is of superior quality.
    SUP = SUPERIOR = F("SUP")

    #: Item has a runeword.
    RW = RUNEWORD = F("RW")

    #: Item has had a gem, jewel, or rune inserted into sockets.
    GEMMED = F("GEMMED")

    #: Item is a helm. This includes class-specific helms.
    EQ1 = HELM = F("HELM")

    #: Item is a chest armor.
    EQ2 = CHEST = F("CHEST")

    #: Item is a shield. This includes class-specific shields.
    EQ3 = SHIELD = F("SHIELD")

    #: Item is a pair of gloves.
    EQ4 = GLOVES = F("GLOVES")

    #: Item is a pair of boots.
    EQ5 = BOOTS = F("BOOTS")

    #: Item is a belt.
    EQ6 = BELT = F("BELT")

    #: Item is a circlet.
    EQ7 = CIRC = CIRCLET = F("CIRC")

    #: Item is any armor. This includes class-specific armor.
    ARMOR = F("ARMOR")

    #: Item is an axe. This includes throwing axes.
    WP1 = AXE = F("AXE")

    #: Item is a mace.
    WP2 = MACE = F("MACE")

    #: Item is a sword.
    WP3 = SWORD = F("SWORD")

    #: Item is a dagger. This includes throwing knives.
    WP4 = DAGGER = F("DAGGER")

    #: Item is a throwing item. Includes throwing knives, axes, javelins, and potions.
    WP5 = THROWING = F("THROWING")

    #: Item is a javelin. Includes Amazon-only javelins.
    WP6 = JAV = JAVELIN = F("JAV")

    #: Item is a spear. Includes Amazon-only spears.
    WP7 = SPEAR = F("SPEAR")

    #: Item is a polearm.
    WP8 = POLEARM = F("POLEARM")

    #: Item is a bow. Includes Amazon-only bows.
    WP9 = BOW = F("BOW")

    #: Item is a crossbow.
    WP10 = XBOW = CROSSBOW = F("XBOW")

    #: Item is a staff.
    WP11 = STAFF = F("STAFF")

    #: Item is a wand.
    WP12 = WAND = F("WAND")

    #: Item is a scepter.
    WP13 = SCEPTER = F("SCEPTER")

    #: Item is a weapon.
    WEAPON = F("WEAPON")

    #: Item is a one-handed weapon.
    WEAPON_1H = F("1H")  # attribute names cannot start with an integer

    #: Item is a two-handed weapon.
    WEAPON_2H = F("2H")  # attribute names cannot start with an integer

    #: Item is a club (a subtype of mace).
    CLUB = F("CLUB")

    #: Item is a tipped mace (a subtype of mace).
    TMACE = TIPPED_MACE = F("TMACE")

    #: Item is a hammer (a subtype of mace).
    HAMMER = F("HAMMER")

    #: Item is restricted to druids only (druid pelts).
    CL1 = DRU = DRUID_ONLY = ClassRestricted.copy(PC.DRUID)

    #: Item is restricted to barbarians only (barbarian helms).
    CL2 = BAR = BARBARIAN_ONLY = ClassRestricted.copy(PC.BARBARIAN)

    #: Item is restricted to paladins only (paladin shields).
    CL3 = DIN = PALADIN_ONLY = ClassRestricted.copy(PC.PALADIN)

    #: Item is restricted to necromancers only (necromancer shields).
    CL4 = NEC = NECROMANCER_ONLY = ClassRestricted.copy(PC.NECROMANCER)

    #: Item is restricted to assassins only (assassin weapons).
    CL5 = SIN = ASSASSIN_ONLY = ClassRestricted.copy(PC.ASSASSIN)

    #: Item is restricted to sorceresses only (sorceress weapons).
    CL6 = SOR = SORCERESS_ONLY = ClassRestricted.copy(PC.SORCERESS)

    #: Item is restricted to amazons only (amazon weapons).
    CL7 = ZON = AMAZON_ONLY = ClassRestricted.copy(PC.AMAZON)

    #: Item is class-restricted. Includes all class-restricted items.
    CLASS = CLASS_RESTRICTED = F("CLASS")


class BHCodes(
    BHCoreCodes,
    BHMutableCodes,
    BHItemCodes,
    BHEquipmentCodes,
    BHColorCodes,
):
    """
    Composite class that contains all BH codes that are not mod-specific.
    """

    #: As a filter: amount of gold in a gold pile.
    #: Per https://wiki.projectdiablo2.com/wiki/Item_Filtering#Info_Codes,
    #: gold's "item name" may not be modified.
    #: Possible values: positive integers.
    #:
    #: As a code: the color gold.
    GOLD = FC("GOLD")
