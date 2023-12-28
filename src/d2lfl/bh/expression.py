"""
d2lfl.bh.expression
===================

This module contains helper functions to work with
BH maphack loot filter expressions.
"""

import re

_whitespace = re.compile(r"\s+")


def bh_and(*expressions: str) -> str:
    """
    Given a set of BH ItemDisplay expressions, returns a BH ItemDisplay
    expression logically ANDs them together.
    """
    return " ".join(bh_normalize(e) for e in expressions)


def bh_not(expression: str) -> str:
    """
    Given a BH ItemDisplay expression, returns a BH ItemDisplay
    expression that is the logical inverse (NOT).
    """

    return f"!{bh_normalize(expression)}"


def bh_normalize(expression: str) -> str:
    """
    Given a BH ItemDisplay expression, produces an equivalent expression
    that is normalized.

    Normalized expressions have extraneous whitespace removed and are
    wrapped in parenthesis if required.
    """
    n = _whitespace.sub(" ", expression.strip())

    has_enclosing_parens = n.startswith("(") and n.endswith(")")
    has_whitespace = " " in n
    if has_enclosing_parens:
        return n
    elif has_whitespace:
        return f"({n})"
    else:
        return n


def bh_or(*expressions: str) -> str:
    """
    Given a set of BH ItemDisplay expressions, returns a BH ItemDisplay
    expression logically ORs them together.
    """
    return bh_normalize(" OR ".join(bh_normalize(e) for e in expressions))
