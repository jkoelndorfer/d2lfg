"""
d2lfl.bh.itemdisplay.codetypes
==============================

This module contains the type definitions for loot filter codes.
"""

from .expression import BHExpression
from .operator import BHOperator


class BHCode:
    """
    The base class for BH loot filter output codes.
    """
    def __init__(self, code: str) -> None:
        self._code = code

    @property
    def code(self) -> str:
        """
        The code's value, as a string.

        For output codes, this *MUST NOT* include wrapping "%" symbols.
        """
        return self._code

    def __str__(self) -> str:
        return f"%{self.code}%"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.code}"


class BHFilterCode(BHCode, BHExpression):
    """
    A BH loot filter output code that can also be used in a filter expression.

    For use in output strings, simply interpolate this object into
    the string. The required "%" symbols will be included automatically.
    """
    def bhexpr(self) -> str:
        return self.code


class BHChargeSkill(BHFilterCode):
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

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.parent.skill_num}, {self.parent.skill_name})"


class BHOSkill(BHFilterCode):
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

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.parent.skill_num}, {self.parent.skill_name})"


class BHRegularSkill(BHFilterCode):
    """
    Class implementing a BH regular +skill code.

    This can be used in a "+X to Skill (*class* only)" filter.
    """
    def __init__(self, parent: "BHSkill") -> None:
        self.parent = parent

    @property
    def code(self) -> str:
        return f"SK{self.parent.skill_num}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.parent.skill_num}, {self.parent.skill_name})"


class BHSkill:
    """
    Wrapper for BHRegularSkill, BHOSkill, and BHChargeSkill.

    This class is a "dispatch" by which loot filter authors can
    access regular skill, oskill, and skill charge codes.
    """
    def __init__(self, skill_num: int, skill_name: str) -> None:
        self.skill_num = skill_num
        self.skill_name = skill_name

        self.sk = BHRegularSkill(self)
        self.os = BHOSkill(self)
        self.chsk = BHChargeSkill(self)

    def __str__(self) -> str:
        raise NotImplementedError(
            f"{repr(self)} *NOT FOR USE IN STRING INTERPOLATION!* "
            "Call .sk, .os, or .chsk to get regular skill, oskill, "
            "or charge skill, respectively, for use in output. "
            "For debug output, call repr() on this object."
        )

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

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.parent.stat_num}, {self.parent.stat_name})"


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

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.parent.stat_num}, {self.parent.stat_name})"


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

    def __str__(self) -> str:
        raise NotImplementedError(
            f"{repr(self)} *NOT FOR USE IN STRING INTERPOLATION!* "
            "Call .char or .item to get a character or item stat for use in output. "
            "For debug output, call repr() on this object."
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.stat_num}, {self.stat_name})"
