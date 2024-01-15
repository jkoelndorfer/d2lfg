"""
``d2lfg.bh.config.configfile``
==============================

This module contains code modeling a BH maphack config file.
"""

from io import StringIO
from typing import List, Literal

from .configentry import BHConfigurationEntry


BHConfigurationEncoding = Literal["windows-1252", "utf-8"]


class BHConfigurationFile:
    """
    Object representing a BH maphack configuration.

    BHConfiguration objects are composed of zero or more
    BHConfigurationEntry objects.
    """

    def __init__(self) -> None:
        self._config_items: List[BHConfigurationEntry] = []

    def add(self, configentry: BHConfigurationEntry) -> None:
        """
        Adds the given configuration entry to this configuration file.

        :param configentry: the configuration entry to add
        """
        self._config_items.append(configentry)

    def render(self, encoding: BHConfigurationEncoding = "windows-1252") -> bytes:
        """
        Renders this configuration file.

        :param encoding: the encoding to use for the rendered file; \
            you probably should not change this
        """
        sio = StringIO()
        for r in self._config_items:
            sio.write(r.render())

        # The Project Diablo 2 wiki says that to support special characters,
        # we must encode the file using "ANSI" (see below). This is a
        # misnomer [1] and is probably intended to mean windows-1252.
        # To support all the fancy characters in Diablo 2, we default
        # to the "ANSI" encoding. But we also allow users to override
        # the encoding, just in case they would need to do that for
        # some reason.
        #
        # From the wiki [2]:
        #
        # > [...]
        # > other symbols:             µ¶¢£¥®©§¿¡¯¨¬­¦«»÷×±ªº´¤°¹²³¼½¾·¸
        # > other capital letters:     ÐÞÆØÁÀÂÄÃÅÇÉÈÊËÍÌÎÏÑÓÒÔÖÕÚÙÛÜÝ
        # > other small letters:       ðþæøáàâäãåçéèêëíìîïñóòôöõúùûüýÿß
        # >
        # > - The last three categories require the filter file to be
        # >   encoded in ANSI rather than the default UTF-8
        # >
        # > - The soft hyphen character doesn't display correctly in many
        # >   places (including this wiki) but does show up in-game
        # >
        # > - These characters display as "?" if HD text is disabled: ·¸
        # >
        # > - These characters aren't displayed at all if HD text is
        # >   enabled: ¬­÷±¤ (including soft hyphen)
        #
        # [1]: https://stackoverflow.com/a/701920
        # [2]: https://wiki.projectdiablo2.com/wiki/Item_Filtering#Output.
        # [3]: Previous categories were omitted for brevity; the last three
        #      are "other symbols", "other capital letters", and
        #      "other small letters".
        return sio.getvalue().encode(encoding)
