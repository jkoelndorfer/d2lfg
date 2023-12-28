"""
d2lfl.bh.code
=============

This module contains the definition for a BH maphack
loot filter codes.
"""

from .itemdisplay import ItemDisplayConditionable, ItemDisplayOutputable

from abc import abstractproperty


class BHCode(ItemDisplayConditionable, ItemDisplayOutputable):
    """
    The base class for BH loot filter codes.
    """

    @abstractproperty
    def code(self) -> str:
        """
        Returns the bare code, suitable for use in a BH ItemDisplay condition.
        """
        raise NotImplementedError("subclasses must implement BHCode.code")

    def item_display_condition(self) -> str:
        return self.code

    def item_display_output(self) -> str:
        return self.output

    @property
    def output(self) -> str:
        """
        Returns the code surrounded by "%" characters, suitable for use
        in a BH ItemDisplay output (i.e. item name or description).
        """
        return f"%{self.code}%"

    def __str__(self) -> str:
        raise NotImplementedError(
            f"can't convert {self.__class__.__name__} to string; must use code or output property"
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.code}"


class BHSimpleCode(BHCode):
    """
    Class implementing simple BH loot filter keyword codes.
    """

    def __init__(self, keyword: str) -> None:
        self.keyword = keyword

    @property
    def code(self) -> str:
        return self.keyword


class BHChargeSkill(BHCode):
    """
    Class implementing a BH charge skill code.

    This can be used to filter for items that grant skill charges,
    i.e. "Level X skill (Y/Z Charges)".
    """
    def __init__(self, parent: "BHSkill") -> None:
        self.parent = parent

    @property
    def code(self) -> str:
        return f"CHSK{self.parent.skill_num}"


class BHOSkill(BHCode):
    """
    Class implementing a BH oskill code.

    This can be used in an oskill filter. Unlike regular skills,
    oskills do not have a class restriction on the skill grant.
    """
    def __init__(self, parent: "BHSkill") -> None:
        self.parent = parent

    @property
    def code(self) -> str:
        return f"OS{self.parent.skill_num}"


class BHRegularSkill(BHCode):
    """
    Class implementing a BH regular +skill code.

    This can be used in a "+X to Skill (*class* only)" filter.
    """
    def __init__(self, parent: "BHSkill") -> None:
        self.parent = parent

    @property
    def code(self) -> str:
        return f"SK{self.parent.skill_num}"


class BHSkill:
    """
    Wrapper for BHRegularSkill, BHOSkill, and BHChargeSkill.

    This class is a "dispatch" by which loot filter authors can
    access regular skill, oskill, and skill charge codes.
    """
    def __init__(self, skill_num: int, skill_name: str) -> None:
        self.skill_num = skill_num
        self.skill_name = skill_name

        self.regular = BHRegularSkill(self)
        self.oskill = BHOSkill(self)
        self.charges = BHChargeSkill(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.skill_num}, {self.skill_name})"


class BHItemStat(BHCode):
    """
    Class implementing a BH item stat.

    This can be used to filter for stats on items.
    """
    def __init__(self, parent: "BHStat") -> None:
        self.parent = parent

    @property
    def code(self) -> str:
        return f"STAT{self.parent.stat_num}"


class BHCharStat(BHCode):
    """
    Class implementing a BH character stat.

    This can be used to filter for stats on the current character.
    """
    def __init__(self, parent: "BHStat") -> None:
        self.parent = parent

    @property
    def code(self) -> str:
        return f"CHARSTAT{self.parent.stat_num}"


class BHStat:
    """
    Wrapper class for BHItemStat and BHCharStat.

    This class is a "dispatch" by which loot filter authors can
    access item stat and character stat codes.
    """
    def __init__(self, stat_num: int, stat_name: str) -> None:
        self.stat_num = stat_num
        self.stat_name = stat_name

        self.char = BHCharStat(self)
        self.item = BHItemStat(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.stat_num}, {self.stat_name})"
