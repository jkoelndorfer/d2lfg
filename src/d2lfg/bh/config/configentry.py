"""
``d2lfg.bh.config.configentry``
===============================

This module contains the model for a BH maphack config file entry.

A config file is made up of config entries.
"""

from abc import ABCMeta, abstractproperty, abstractmethod
import re

from .itemdisplay.filterexpr import BHFilterExpression


def without_trailing_whitespace(a: str, b: str) -> str:
    """
    Produces a string that is the concatenation of ``a``, a space, ``b``, and
    a newline.

    If ``b`` is an empty string, produces ``a`` followed by a newline.
    """
    if not b:
        return f"{a}\n"

    return f"{a} {b}\n"


class BHConfigurationEntry(metaclass=ABCMeta):
    """
    Object representing a part of a BH maphack configuration.

    Any text that appears in a configuration file, including whitespace
    and comments, may be a configuration entry.
    """

    @abstractproperty
    def ignored(self) -> bool:
        """
        Whether or not this configuration entry is ignored by BH (i.e.
        it is only whitespace or a comment).
        """
        raise NotImplementedError("subclasses must implement ignored()")

    @abstractmethod
    def render(self) -> str:
        """
        Renders this configuration entry as a string.

        The rendered entry should include a trailing newline if required to
        terminate this entry.
        """


class BHComment(BHConfigurationEntry):
    """
    Object representing a comment in a BH maphack configuration.

    :param comment_text: the text of the comment; may be multiple lines
    """

    #: Regular expression used to insert comment characters.
    comment_replace_re = re.compile("^", re.MULTILINE)

    #: Regular expression used to clean up trailing whitespace.
    whitespace_cleanup_re = re.compile(r"[ \t]+$", re.MULTILINE)

    def __init__(self, comment_text: str) -> None:
        self.comment_text = comment_text

    @property
    def ignored(self) -> bool:
        return True

    def render(self) -> str:
        commented_text = self.comment_replace_re.sub(
            "// ", self.comment_text.strip("\r\n")
        )
        cleaned_up_text = self.whitespace_cleanup_re.sub("", commented_text)
        return "{}\n".format(cleaned_up_text)


class BHEmptyLine(BHConfigurationEntry):
    """
    Object representing one or more empty lines in a BH maphack configuration.

    :param count_empty_lines: the number of empty lines to display
    """

    def __init__(self, count_empty_lines: int) -> None:
        self.count_empty_lines = count_empty_lines

    @property
    def ignored(self) -> bool:
        return True

    def render(self) -> str:
        return "\n" * self.count_empty_lines


class BHLiteralText(BHConfigurationEntry):
    """
    Object representing a text literal that will appear in a BH maphack configuration.
    The text will be rendered into the configuration *exactly as it appears*.

    You probably do not need this. You should avoid using it unless you have good
    reason to.

    :param literal: the literal text to add to the configuration
    """

    def __init__(self, literal: str) -> None:
        self.literal = literal

    @property
    def ignored(self) -> bool:
        return False

    def render(self) -> str:
        return self.literal


class BHItemDisplay(BHConfigurationEntry):
    """
    Object representing an ItemDisplay configuration directive.

    :param filterexpr: the item filter expression
    :param output: the output of the rule
    """

    def __init__(self, filterexpr: BHFilterExpression, output: str) -> None:
        self.filterexpr = filterexpr
        self.output = output

    @property
    def ignored(self) -> bool:
        return False

    def render(self) -> str:
        return without_trailing_whitespace(
            f"ItemDisplay[{self.filterexpr.bhexpr()}]:",
            self.output,
        )


class BHItemDisplayFilterName(BHConfigurationEntry):
    """
    Object representing a BH ItemDisplayFilterName configuration directive.

    :param filter_name: the name of the filter level
    :param filtlvl: the integer ID for the filter level used in filter expressions
    """

    def __init__(self, filter_name: str, filtlvl: int) -> None:
        self.filter_name = filter_name
        self.filtlvl = filtlvl

    @property
    def ignored(self) -> bool:
        return False

    def render(self) -> str:
        return without_trailing_whitespace(
            "ItemDisplayFilterName[]:",
            self.filter_name,
        )
