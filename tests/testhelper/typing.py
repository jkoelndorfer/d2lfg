"""
``testhelper.typing``
=====================

This module contains test typing code.
"""

from pathlib import Path
from typing import Callable, Generic, TypeVar, Union

from pytest import FixtureRequest as _FixtureRequest

T = TypeVar("T")


class FixtureRequest(_FixtureRequest, Generic[T]):
    """
    Type stub for a pytest FixtureRequest.
    """

    param: T


PathTyper = Callable[[Path], Union[str, Path]]
