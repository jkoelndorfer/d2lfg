"""
``d2lfg.gamedata.bh``
=====================

This module contains classes provide game data which is
also usable as a BHFilterExpression.

The expressions can be used in BHLootFilter rules.
"""

from .database import Diablo2GameDatabase
from .datasource import Diablo2TxtDataSource


class Diablo2BHDatabase(Diablo2GameDatabase):
    def __init__(self, datasource:
