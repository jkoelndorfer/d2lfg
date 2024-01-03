#!/usr/bin/env python3

from pathlib import Path
import sys

from d2lfl import (
    BHLiteralExpression,
    BHLootFilter,
    BHCodes,
    bh_and as AND,
    bh_or as OR,
    bh_not as NOT,
)
from d2lfl.diablo2.data.txt import Diablo2TxtFile, Diablo2TxtDatabase

diablo2_base = Path("/home/kdorf/diablo2/ProjectD2/data/global/excel")
def txt(f: str) -> Diablo2TxtFile:
    return Diablo2TxtFile(diablo2_base / f)

db = Diablo2TxtDatabase(
    txt("ItemTypes.txt"),
    txt("Armor.txt"),
    txt("Misc.txt"),
    txt("Skills.txt"),
    txt("Weapons.txt"),
)
f = BHLootFilter("Kryszard's PD2 Loot Filter - d2lfl Demo")

filtlvl_hide_trash = f.add_filter_level("Hide Just Trash Items")
filtlvl_more_notify = f.add_filter_level("Item Filter - More Notify")
filtlvl_recommended = f.add_filter_level("Item Filter - Recommended")
filtlvl_strict = f.add_filter_level("Strict Filter")
filtlvl_max_strict = f.add_filter_level("Max-Strictness Filter")

NMAG = BHLiteralExpression("NMAG")
RW = BHLiteralExpression("RW")
ASSASSIN = BHLiteralExpression("ASSASSIN")

assassin_skills = list(db.skills_for_class(BHCodes.ASSASSIN))

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
