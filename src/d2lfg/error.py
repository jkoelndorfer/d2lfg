"""
``d2lfg.error``
===============

Contains error types that :py:mod:`d2lfg` may throw.
"""


class D2LfgError(Exception):
    """
    Base class for :py:mod:`d2lfg` errors.

    If :py:mod:`d2lfg` raises an error explicitly, the error
    will be of this type (and likely something more specific).
    """


class DataLookupError(D2LfgError):
    """
    Error raised when a data lookup fails.
    """


class BHFilterExpressionError(D2LfgError):
    """
    Error raised when there is an error related to BH filter expressions.
    """


class InvalidStringConversionError(BHFilterExpressionError):
    """
    Error raised when an object is incorrectly converted to a string.

    This is used to prevent users accidentally stringifying something
    in a context that it should not be.
    """


class TooManyOperandsError(BHFilterExpressionError):
    """
    Error raised when a compound filter expression has too many operands
    for the operator given.
    """
