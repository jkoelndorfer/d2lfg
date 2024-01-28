"""
``testhelper.typing``
=====================

This module contains test typing code.
"""

from typing import Generic, TypeVar

from pytest import FixtureRequest as _FixtureRequest

T = TypeVar("T")


class FixtureRequest(_FixtureRequest, Generic[T]):
    """
    Type stub for a pytest FixtureRequest.
    """

    param: T
