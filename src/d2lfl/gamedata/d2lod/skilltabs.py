from ...game.playerclass import Diablo2PlayerClasses
from ...game.skill import Diablo2SkillTab


class Diablo2AmazonSkillTabs:
    BOW_AND_CROSSBOW = Diablo2SkillTab(0, "Bow and Crossbow Skills", Diablo2PlayerClasses.AMAZON)
    PASSIVE_AND_MAGIC = Diablo2SkillTab(1, "Passive and Magic Skills", Diablo2PlayerClasses.AMAZON)
    JAVELIN_AND_SPEAR = Diablo2SkillTab(2, "Javelin and Spear Skills", Diablo2PlayerClasses.AMAZON)


class Diablo2SorceressSkillTabs:
    FIRE = Diablo2SkillTab(8, "Fire Spells", Diablo2PlayerClasses.SORCERESS)
    LIGHTNING = Diablo2SkillTab(9, "Lightning Spells", Diablo2PlayerClasses.SORCERESS)
    COLD = Diablo2SkillTab(10, "Cold Spells", Diablo2PlayerClasses.SORCERESS)


class Diablo2NecromancerSkillTabs:
    CURSES = Diablo2SkillTab(16, "Curses", Diablo2PlayerClasses.NECROMANCER)
    POISON_AND_BONE = Diablo2SkillTab(17, "Poison and Bone Spells", Diablo2PlayerClasses.NECROMANCER)
    SUMMONING = Diablo2SkillTab(18, "Summoning Spells", Diablo2PlayerClasses.NECROMANCER)


class Diablo2PaladinSkillTabs:
    COMBAT_SKILLS = Diablo2SkillTab(24, "Combat Skills", Diablo2PlayerClasses.PALADIN)
    OFFENSIVE_AURAS = Diablo2SkillTab(25, "Offensive Auras", Diablo2PlayerClasses.PALADIN)
    DEFENSIVE_AURAS = Diablo2SkillTab(25, "Defensive Auras", Diablo2PlayerClasses.PALADIN)


class Diablo2BarbarianSkillTabs:
    COMBAT_SKILLS = Diablo2SkillTab(32, "Combat Skills", Diablo2PlayerClasses.BARBARIAN)
    COMBAT_MASTERIES = Diablo2SkillTab(33, "Combat Masteries", Diablo2PlayerClasses.BARBARIAN)
    WARCRIES = Diablo2SkillTab(34, "Warcries", Diablo2PlayerClasses.BARBARIAN)


class Diablo2DruidSkillTabs:
    SUMMONING = Diablo2SkillTab(40, "Summoning", Diablo2PlayerClasses.DRUID)
    SHAPE_SHIFTING = Diablo2SkillTab(41, "Shape Shifting", Diablo2PlayerClasses.DRUID)
    ELEMENTAL = Diablo2SkillTab(42, "Elemental", Diablo2PlayerClasses.DRUID)


class Diablo2AssassinSkillTabs:
    TRAPS = Diablo2SkillTab(48, "Traps", Diablo2PlayerClasses.ASSASSIN)
    SHADOW_DISCIPLINES = Diablo2SkillTab(49, "Shadow Disciplines", Diablo2PlayerClasses.ASSASSIN)
    MARTIAL_ARTS = Diablo2SkillTab(50, "Martial Arts", Diablo2PlayerClasses.ASSASSIN)


class Diablo2SkillTabs:
    AMAZON = Diablo2AmazonSkillTabs
    SORCERESS = Diablo2SorceressSkillTabs
    NECROMANCER = Diablo2NecromancerSkillTabs
    PALADIN = Diablo2PaladinSkillTabs
    BARBARIAN = Diablo2BarbarianSkillTabs
    DRUID = Diablo2DruidSkillTabs
    ASSASSIN = Diablo2AssassinSkillTabs
