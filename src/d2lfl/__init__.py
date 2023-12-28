"""
Project Diablo 2 Filter Library (pd2fl)
=======================================

This library is a helper that aims to make maintenance of Project
Diablo 2 loot filters easier.

Using this library, loot filters can be constructed using a Python
script and then rendered into the format that Project Diablo 2's BH
expects. This enables users to define their own helper functions, use
loops to define rules, and allow filter users to pass parameters to
the rendering script which control loot filter behavior.
"""

from .lootfilter import LootFilter
