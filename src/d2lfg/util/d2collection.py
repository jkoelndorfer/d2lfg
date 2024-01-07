"""
``d2lfg.util.d2collection``
===========================

This module contains the implementation for :py:class:`Diablo2Collection`.
"""

from abc import ABCMeta, abstractmethod
from typing import Generic, Hashable, Iterable, Set, Type, TypeVar

from ..error import DataLookupError


T = TypeVar("T", bound=Hashable)


class Diablo2Collection(Generic[T], metaclass=ABCMeta):
    """
    Provides an enum-style interface to a collection of Diablo 2 objects
    of a single type.

    This class provides dotted member access like :py:class:`~enum.Enum`s
    do, but without having to call :py:meth:`~enum.Enum.value` to
    acess the actual value.

    Additionally, class methods are provided to access all members or
    look up a member by key.

    Python dunder methods like :py:func:`__iter__` and :py:func:`__getitem__`
    are not used because they cannot be implemented as class methods
    without using a metaclass.
    """

    @classmethod
    def all(cls) -> Iterable[T]:
        """
        Returns an iterable over all items in this collection.
        """
        t = cls.collection_type()
        s: Set[T] = set()
        for attr in dir(cls):
            v = getattr(cls, attr, None)
            if isinstance(v, t):
                s.add(v)
        return s

    @classmethod
    def lookup(cls, k: str) -> T:
        """
        Looks up the item in this collection with the given key.
        """
        t = cls.collection_type()
        v = getattr(cls, k, None)
        if isinstance(v, t):
            return v
        raise DataLookupError(f"{k}: no such {t.__name__}")

    @classmethod
    @abstractmethod
    def collection_type(cls) -> Type[T]:
        """
        Returns the type of object that this collection contains.
        """
        raise NotImplementedError("subclasses must implement collection_type")
