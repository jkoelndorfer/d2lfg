#!/usr/bin/env python3

from pathlib import Path
import sys

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

for a in db.armors(where=lambda a: a.is_normal):
    upgrade = db.armor(a.uber_code)
    print(f"{a.name} -> {upgrade.name} (lvl/str req: {upgrade.lvl_req}/{upgrade.str_req})")
