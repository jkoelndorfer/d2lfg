#!/usr/bin/env python3

from d2lfl import LootFilter

f = LootFilter("Kryszard's PD2 Loot Filter - d2lfl Demo")

filtlvl_hide_trash = f.add_filter_level("Hide Just Trash Items")
filtlvl_more_notify = f.add_filter_level("Item Filter - More Notify")
filtlvl_recommended = f.add_filter_level("Item Filter - Recommended")
filtlvl_strict = f.add_filter_level("Strict Filter")
filtlvl_max_strict = f.add_filter_level("Max-Strictness Filter")
