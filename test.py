#!/usr/bin/env python3

from d2lfl import LootFilter

f = LootFilter("Kryszard's PD2 Loot Filter - d2lfl Demo")
AND = f.eand
NOT = f.enot
OR = f.eor

filtlvl_hide_trash = f.add_filter_level("Hide Just Trash Items")
filtlvl_more_notify = f.add_filter_level("Item Filter - More Notify")
filtlvl_recommended = f.add_filter_level("Item Filter - Recommended")
filtlvl_strict = f.add_filter_level("Strict Filter")
filtlvl_max_strict = f.add_filter_level("Max-Strictness Filter")

assassin_skills = (
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
)

def any_skill(skills):
    skill_present = (f"{s}>0" for s in skills)
    return OR(*skill_present)

f.add_display_rule(
    AND("NMAG", "!RW", any_skill(assassin_skills)),
    "%GRAY%] %NAME%"
)
for s in assassin_skills.reverse():
    pass
