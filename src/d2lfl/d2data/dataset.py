"""
d2data.dataset
==============

This module contains a data set implementation.
"""

from abc import ABCMeta, abstractmethod
from pathlib import Path
from typing import Iterator, Mapping, Sequence, Union


class Diablo2DataRecord:
    """
    Object representing a Diablo 2 data record (i.e. a row from
    a txt file).
    """
    def __init__(self, field_indices: Mapping[str, int], data: Sequence[str]) -> None:
        self.field_indices = field_indices
        self.data = data

    def __getitem__(self, index: Union[int, str]) -> str:
        if isinstance(index, int):
            return self.data[index]
        return self.data[self.field_indices[index]]


class Diablo2DataSet(metaclass=ABCMeta):
    """
    Object representing a Diablo 2 data set.

    Data sets are intended to correspond to a .txt file, where
    there are one or more records that have a consistent set
    of fields.
    """

    @abstractmethod
    def fields(self) -> Sequence[str]:
        """
        Returns the valid fields for data in this file.
        """

    @abstractmethod
    def __getitem__(self, index: int) -> Diablo2DataRecord:
        """
        Gets record(s) from this data file.
        """

    @abstractmethod
    def __iter__(self) -> Iterator[Diablo2DataRecord]:
        """
        Iterates over the records in this data file.
        """


class Diablo2TxtDataSet(Diablo2DataSet):
    """
    A Diablo2DataSet backed by a .txt file extracted from an MPQ.
    """

    def __init__(self, path: Path) -> None:
        self.path = path

        with open(self.path, "r") as f:
            self._fields = f.readline().split("\t")
            self._field_indices = {v: k for k, v in enumerate(self._fields)}
            self._records = []

            for l in f.readlines():
                line_fields = l.split("\t")
                if len(line_fields) == len(self._field_indices):
                    self._records.append(Diablo2DataRecord(self._field_indices, l.split("\t")))

    def fields(self) -> Sequence[str]:
        return list(self._fields)

    def __getitem__(self, index: int) -> Diablo2DataRecord:
        return self._records[index]

    def __iter__(self) -> Iterator[Diablo2DataRecord]:
        for r in self._records:
            yield r
