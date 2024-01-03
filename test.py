#!/usr/bin/env python3

from d2lfl import (
    BHLiteralExpression,
    BHLootFilter,
    BHCodes,
    bh_and as AND,
    bh_or as OR,
    bh_not as NOT,
)
import sys

f = BHLootFilter("Kryszard's PD2 Loot Filter - d2lfl Demo")

filtlvl_hide_trash = f.add_filter_level("Hide Just Trash Items")
filtlvl_more_notify = f.add_filter_level("Item Filter - More Notify")
filtlvl_recommended = f.add_filter_level("Item Filter - Recommended")
filtlvl_strict = f.add_filter_level("Strict Filter")
filtlvl_max_strict = f.add_filter_level("Max-Strictness Filter")

NMAG = BHLiteralExpression("NMAG")
RW = BHLiteralExpression("RW")
ASSASSIN = BHLiteralExpression("ASSASSIN")

assassin_skills = tuple(
    BHLiteralExpression(s) for s in [
        "SK251",
        "SK252",
        "SK253",
        "SK254",
        "SK255",
        "SK256",
        "SK257",
        "SK258",
        "SK259",
        "SK260",
        "SK261",
        "SK262",
        "SK263",
        "SK264",
        "SK265",
        "SK266",
        "SK267",
        "SK268",
        "SK269",
        "SK270",
        "SK271",
        "SK272",
        "SK273",
        "SK274",
        "SK275",
        "SK276",
        "SK277",
        "SK278",
        "SK279",
        "SK280",
        "SK366",
    ]
)

def any_skill(skills):
    skill_present = (s > 0 for s in skills)
    return OR(*skill_present)

f.add_display_rule(
    AND(
        NMAG,
        NOT(RW),
        any_skill(assassin_skills)
    ),
    f"{BHCodes.GRAY}] {BHCodes.NAME}"
)
assassin_reversed = list(reversed(assassin_skills))
while len(assassin_reversed) > 0:
    current_skill = assassin_reversed.pop()
    f.add_display_rule(
        AND(
            NMAG,
            NOT(RW),
        ),
        "not magic runeword",
    )

sys.stdout.buffer.write(f.render())
