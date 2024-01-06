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
