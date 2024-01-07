"""
``tests.util``
==============

This module contains test code for :py:mod:`d2lfg.util`.
"""

import pytest
from typing import Type

from d2lfg.util.d2collection import Diablo2Collection
from d2lfg.error import DataLookupError


class StringCollection(Diablo2Collection[str]):
    A = "a"
    B = "b"
    C = "c"

    @classmethod
    def collection_type(cls) -> Type[str]:
        return str


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

    @pytest.mark.parametrize("k, v", [("A", "a"), ("B", "b"), ("C", "c")])
    def test_lookup_invalid(self, k: str, v: str) -> None:
        """
        Tests that a call to :py:meth:`Diablo2Collection.lookup` with
        a valid key succeeds and returns the correct value.
        """
        assert StringCollection.lookup(k) == v

    @pytest.mark.parametrize("k", ["A1", "_A", "D"])
    def test_lookup_invalid_raises_data_lookup_error(self, k) -> None:
        """
        Tests that a call to :py:meth:`Diablo2Collection.lookup` with
        an invalid key raises a :py:class:`DataLookupError`.
        """
        with pytest.raises(DataLookupError):
            StringCollection.lookup(k)
