#!/usr/bin/env python3

from pathlib import Path
import sys

from d2lfl import (
    BHLootFilter,
    BHCodes,
    bh_data_factory,
    bh_and as AND,
    bh_or as OR,
    bh_not as NOT,
)
from d2lfl.diablo2.data.txt import Diablo2TxtFile, Diablo2TxtDatabase

diablo2_base = Path("/home/kdorf/diablo2/ProjectD2/data/global/excel")
def txt(f: str) -> Diablo2TxtFile:
    return Diablo2TxtFile(diablo2_base / f)

db = Diablo2TxtDatabase(
    bh_data_factory,
    txt("ItemTypes.txt"),
    txt("Armor.txt"),
    txt("Misc.txt"),
    txt("Skills.txt"),
    txt("Weapons.txt"),
)
db.initialize()
f = BHLootFilter("Kryszard's PD2 Loot Filter - d2lfl Demo")

f.add_comment(
    """
    pd2lfl demo loot filter
    =======================

    Generate Diablo 2 BH loot filter rules using Python!
    """,
    dedent=True
)
f.add_blank_lines(1)

filtlvl_hide_trash = f.add_filter_level("Hide Just Trash Items")
filtlvl_more_notify = f.add_filter_level("Item Filter - More Notify")
filtlvl_recommended = f.add_filter_level("Item Filter - Recommended")
filtlvl_strict = f.add_filter_level("Strict Filter")
filtlvl_max_strict = f.add_filter_level("Max-Strictness Filter")

assassin_skills = list(db.skills_for_class(BHCodes.ASSASSIN))

def any_skill(skills):
    skill_present = (s.sk > 0 for s in skills)
    return OR(*skill_present)

f.add_display_rule(
    AND(
        BHCodes.NMAG,
        NOT(BHCodes.RW),
        any_skill(assassin_skills)
    ),
    f"{BHCodes.GRAY}] {BHCodes.NAME}"
)
assassin_reversed = list(reversed(assassin_skills))
while len(assassin_reversed) > 0:
    current_skill = assassin_reversed.pop()
    f.add_display_rule(
        AND(
            BHCodes.NMAG,
            NOT(BHCodes.RW),
        ),
        "not magic runeword",
    )

t11_item = db.item("t11")
f.add_display_rule(t11_item, f"a {t11_item.name} thing")
# f.add_comment("my comment\nand another line")

sys.stdout.buffer.write(f.render())
