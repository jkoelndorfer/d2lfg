"""
``tests.util.test_d2collection``
================================

This module contains test code for :py:mod:`d2lfg.util.d2collection`.
"""

import pytest
from typing import Type

from d2lfg.util.d2collection import Diablo2Collection
from d2lfg.error import DataLookupError


class Diablo2Object(str):
    """
    An object for testing :py:class:`Diablo2Collection`.
    """


class StringCollection(Diablo2Collection[Diablo2Object]):
    A = Diablo2Object("a")
    B = Diablo2Object("b")
    C = Diablo2Object("c")

    @classmethod
    def collection_type(cls) -> Type[Diablo2Object]:
        return Diablo2Object


class TestDiablo2Collection:
    """
    Tests :py:class:`Diablo2Collection`.
    """

    def test_all_returns_all_items(self) -> None:
        """
        Tests that :py:meth:`Diablo2Collection.all` returns all items
        in the collection.
        """
        assert sorted(list(StringCollection.all())) == ["a", "b", "c"]

    def test_base_collection_type_raises_not_implemented(self) -> None:
        """
        Tests that :py:meth:`Diablo2Collection.collection_type` raises
        a :py:class:`NotImplementedError`. Subclasses must override
        this class method.
        """
        with pytest.raises(NotImplementedError):
            Diablo2Collection.collection_type()  # type: ignore

    @pytest.mark.parametrize("k, v", [("A", "a"), ("B", "b"), ("C", "c")])
    def test_lookup_invalid(self, k: str, v: str) -> None:
        """
        Tests that a call to :py:meth:`Diablo2Collection.lookup` with
        a valid key succeeds and returns the correct value.
        """
        assert StringCollection.lookup(k) == v

    @pytest.mark.parametrize("k", ["A1", "_A", "D"])
    def test_lookup_invalid_raises_data_lookup_error(self, k: str) -> None:
        """
        Tests that a call to :py:meth:`Diablo2Collection.lookup` with
        an invalid key raises a :py:class:`DataLookupError`.
        """
        with pytest.raises(DataLookupError):
            StringCollection.lookup(k)
