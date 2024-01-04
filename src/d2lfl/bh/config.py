"""
d2lfl.bh.config
===============

Contains code to model BH configuration.

While this library is targeted specifically at loot filter generation,
it should be easy to add support for other configuration types here.
"""

# Notes from someone stumbling on this "BH" thing for the first time:
#
# "BH" seems to be shorthand for "blizzhackers", a site which does
# not exist anymore. "BH" is used as a shorthand for the "BH maphack",
# which is the software that provides the loot filtering capability
# used by Project Diablo 2 and SlashDiablo. Of course, it also provided
# a maphack.
#
# The maphack's configuration file had a number of different options;
# the ItemDisplay option is what we're interested in for the purpose
# of loot filtering.
#
# This module implements a small API for creating BH maphack
# configurations without making loot filter specific
# design choices. In the future, if additional configuration
# for BH maphack is needed, it should be relatively easy to
# support.
#
# References:
#     * https://www.reddit.com/r/Diablo/comments/q2f7cu/i_miss_blizzhackers/
#     * https://github.com/blizzhackers
#     * https://github.com/planqi/slashdiablo-maphack
#     * http://forum.europebattle.net/threads/bh-maphack-loot-filters.544928/
#     * https://github.com/Project-Diablo-2/BH/tree/0070b0776e8e50500b52ac87c002a68f750ae98c/BH

from abc import ABCMeta, abstractmethod
from io import StringIO
import os
import re
from typing import List, Literal


class BHConfigurationItem(metaclass=ABCMeta):
    def trailing_newline(self) -> bool:
        """
        If True, the configuration item should
        """
        return True

    @abstractmethod
    def render(self) -> str:
        """
        Renders the given BH configuration element.
        """


class BHBlankLines(BHConfigurationItem):
    def __init__(self, count: int) -> None:
        self.count = count

    def render(self) -> str:
        return "\n" * self.count

    def trailing_newline(self) -> bool:
        return False


class BHComment(BHConfigurationItem):
    #: Regular expression used to insert comment characters.
    comment_replace_re = re.compile("^", re.MULTILINE)

    def __init__(self, comment: str) -> None:
        self.comment = comment

    def render(self) -> str:
        return self.comment_replace_re.sub("// ", self.comment.strip("\n"))


class BHItemDisplay(BHConfigurationItem):
    """
    BHConfigurationItem representing an ItemDisplay configuration.

    This is used to generate loot filter rules.
    """
    def __init__(self, condition: str, output: str) -> None:
        self.condition = condition
        self.output = output

    def render(self) -> str:
        return f"ItemDisplay[{self.condition}]: {self.output}"


class BHItemDisplayFilterName(BHConfigurationItem):
    """
    BHConfigurationItem representing an ItemDisplayFilterName configuration.

    This is used to create filter strictness levels.
    """
    def __init__(self, name: str) -> None:
        self.name = name

    def render(self) -> str:
        return f"ItemDisplayFilterName[]: {self.name}"


class BHConfiguration:
    """
    Object representing a BH maphack configuration.

    BHConfiguration objects are composed of zero or more
    BHConfigurationItem objects.
    """
    def __init__(self, encoding: Literal["windows-1252", "utf-8"] = "windows-1252") -> None:
        # The Project Diablo 2 wiki says that to support special characters,
        # we must encode the file using "ANSI" (see below). This is a
        # misnomer [1] and is probably intended to mean Windows-1252.
        # To support all the fancy characters in Diablo 2, let's default
        # to the "ANSI" encoding.
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
        # TODO: Is this windows-1252 encoding scheme specific to Project
        #       Diablo 2 or does it generalize to BH maphack?
        #
        # [1]: https://stackoverflow.com/a/701920
        # [2]: https://wiki.projectdiablo2.com/wiki/Item_Filtering#Output.
        # [3]: Previous categories were omitted for brevity; the last three
        #      are "other symbols", "other capital letters", and
        #      "other small letters".
        self.encoding = encoding

        self._config_items: List[BHConfigurationItem] = []

    def add(self, rule: BHConfigurationItem) -> None:
        self._config_items.append(rule)

    def render(self) -> bytes:
        sio = StringIO()
        for r in self._config_items:
            sio.write(r.render())
            if r.trailing_newline():
                sio.write("\n")

        # Chop off the last "\n".
        #
        # For some reason neither:
        #
        # sio.seek(-1, os.SEEK_CUR)
        #
        # nor
        #
        # sio.seek(-1, os.SEEK_END)
        #
        # are valid here. They both raise the same exception:
        #     OSError: Can't do nonzero cur-relative seeks
        sio.seek(sio.tell() - 1, os.SEEK_SET)
        sio.truncate()

        return sio.getvalue().encode(self.encoding)
