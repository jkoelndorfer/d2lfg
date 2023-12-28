"""
Diablo 2 Loot Filter Library (d2lfl)
====================================

This library is a helper that aims to make maintenance of BH
loot filtering configurations easier.

Using this library, loot filters can be constructed using a
Python script and then rendered into the format that BH expects.

Having a script render the configuration allows filter authors
to define their own helper functions, employ looping logic, and
even allow filter users to pass parameters to control how the
loot filter operates.
"""

from .lootfilter import LootFilter
