"""
d2lfl.game.base
===============

This module contains definitions for classes used across games.
"""

from typing import Optional

from ..bh.itemdisplay.expression import BHLiteralExpression


class Diablo2Item(BHLiteralExpression):
    def __init__(
        self,
        code: str,
        name: str,
        lower_tier_code: Optional[str] = None,
        higher_tier_code: Optional[str] = None,
        lvl_req: int = 0,
        str_req: int = 0,
        dex_req: int = 0,
        max_sockets: int = 0,
    ) -> None:
        super().__init__(code)
        self.name = name

        # Notes about item tiers:
        #
        # Generally, normal tier has a unique 3-letter code that
        # is an abbreviation of the item name.
        #
        # For armor, the exceptional item code can be attained by
        # replacing the first character with "x". The elite item
        # code can be attained by replacing the first character
        # with "u".
        #
        # For weapons, the exceptional item code can be attained by
        # replacing the first character with "9". The elite item
        # code can be attained by replacing the first character with
        # "7". Staves use "8" and "6", respectively.
        #
        # This is *NOT ALWAYS TRUE*. Class-specific items are an
        # exception, for example.

        #: The item code of the lower-tiered version of this item.
        #: i.e. if this item is a Shako (elite tier), the lower-tier
        #: item is a War Hat (exceptional tier) whose code is xap.
        self.lower_tier_code = lower_tier_code

        #: The item code of the higher-tiered version of this item.
        #: i.e. if this item is a War Hat (exceptional tier), the
        #: higher-tier item is a Shako (elite tier) whose code
        #: is uap.
        self.higher_tier_code = higher_tier_code

        #: The level requirement for the item.
        self.lvl_req = lvl_req

        #: The strength requirement for the item.
        self.str_req = str_req

        #: The dexterity requirement for the item.
        self.dex_req = dex_req

        #: The maximum number of sockets the item can have.
        self.max_sockets = max_sockets