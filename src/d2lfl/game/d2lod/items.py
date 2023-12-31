"""
d2lfl.game.d2lod.items
======================

Contains definitions for items found in
Diablo II - Lord of Destruction vanilla.
"""

from ..base import Diablo2Item as I

class Diablo2LordOfDestructionNormalHelms:
    CAP = I(
        code="cap",
        name="Cap",
        lower_tier_code=None,
        higher_tier_code="xap",
        lvl_req=0,
        str_req=0,
        dex_req=0,
        max_sockets=2,
        set_versions=["Sander's Paragon"],
        unique_versions=["Biggin's Bonnet"],
    )

    XAP = WAR_HAT = I(
        code="xap",
        name="War Hat",
        lower_tier_code="cap",
        higher_tier_code="uap",
        lvl_req=22,
        str_req=20,
        dex_req=0,
        max_sockets=2,
        set_versions=["Cow King's Horns"],
        unique_versions=["Peasant Crown"],
    )

    UAP = SHAKO = I(
        code="uap",
        name="Shako",
        lower_tier_code="uap",
        lvl_req=43,
        str_req=50,
        dex_req=0,
        max_sockets=2,
    )

    SKP = SKULL_CAP = I(
        code="skp",
        name="Skull Cap",
        lower_tier_code=None,
        higher_tier_code="xkp",
        lvl_req=0,
        str_req=15,
        dex_req=0,
        max_sockets=2,
    ),

    XKP = SALLET = I(
        code="xkp",
        name="Sallet",
        lower_tier_code="skp",
        higher_tier_code="ukp",
        lvl_req=25,
        str_req=43,
        dex_req=0,
        max_sockets=2,
    )

    UKP = HYDRASKULL = I(
        code="ukp",
        name="Hydraskull",
        lower_tier_code="ukp",
        higher_tier_code=None,
        lvl_req=47,
        str_req=84,
        dex_req=0,
        max_sockets=2,
    )
