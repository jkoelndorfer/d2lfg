"""
``d2lfg.d2core.data.txt``
=========================

This module contains code for parsing Diablo 2 .txt
files that contain game data.

See the `Phrozen Keep File Guide`_ for documentation about
the various .txt files and what their fields do.

.. _Phrozen Keep File Guide: https://www.d2mods.info/forum/viewtopic.php?t=34455
"""

from io import TextIOBase
from pathlib import Path
import re
from types import MappingProxyType
from typing import Callable, List, Mapping, overload, Sequence, Union


class Diablo2TxtRecord(Sequence[str], Mapping[str, str]):
    """
    Object representing a single row from a :py:class:`Diablo2TxtFile`.

    :param fields: a mapping of column name to its integer index in \
        ``data``; all keys must be :py:meth:`~str.casefold` ed
    :param data: the row as a sequence; each element contains one field
    """

    def __init__(self, fields: Mapping[str, int], data: Sequence[str]) -> None:
        self.fields = fields
        self.data = data

    @overload
    def __getitem__(self, k: Union[str, int]) -> str:
        ...

    @overload
    def __getitem__(self, k: slice) -> Sequence[str]:
        ...

    def __getitem__(self, k: Union[slice, str, int]) -> Union[str, Sequence[str]]:
        if isinstance(k, str):
            k = self.fields[k.casefold()]
        return self.data[k]

    def __eq__(self, other: object) -> bool:
        """
        Returns ``True`` if the compared object is an equivalent
        :py:class:`Diablo2TxtRecord`.
        """
        if not isinstance(other, Diablo2TxtRecord):
            return False
        return self.data == other.data and self.fields == other.fields

    def __len__(self) -> int:
        return len(self.data)

    def __repr__(self) -> str:
        return repr({f"{v}/{k}": self.data[v] for k, v in self.fields.items()})


class Diablo2TxtFile:
    """
    Object representing a Diablo 2 .txt file.
    """

    def __init__(
        self, path: Union[None, str, Path], records: Sequence[Diablo2TxtRecord]
    ):
        if isinstance(path, str):
            self.path: Union[None, str, Path] = Path(path)
        else:
            self.path = path

        self.records = records


#: Regular expression describing an empty Diablo 2 .txt file field.
empty_field = re.compile(r"^\s*$")


def skip_record(record: Diablo2TxtRecord) -> bool:
    """
    Default record-skipping logic for :py:class:`Diablo2TxtParser`.

    Skips records where one of the following is true:

        1. All fields after the first are empty. Sometimes the first field
           is used by itself as a comment. When that happens, the rest of
           the record is empty.

        2. The record contains fewer fields than there are columns in the file;
           i.e. the record is incomplete
    """
    # field_indices contains all the columns in the txt file.
    # If there is less data than there are columns, the record
    # is incomplete. For our purposes, that means we should skip
    # it.
    if len(record.data) < len(record.fields):
        return True

    for v in record.data[1:]:
        if not empty_field.match(v):
            return False

    return True


class Diablo2TxtParser:
    """
    Parses Diablo 2 .txt files and returns a :py:class:`Diablo2TxtFile`.

    :param skip_record: a :py:class:`~collections.abc.Callable` that accepts a \
        :py:class:`Diablo2TxtRecord` and returns ``True`` if it should be not \
        be included in the resulting :py:class:`Diablo2TxtFile`
    """

    def __init__(
        self, skip_record: Callable[[Diablo2TxtRecord], bool] = skip_record
    ) -> None:
        self.skip_record = skip_record

    def parse(self, file: Union[Path, str, TextIOBase]) -> Diablo2TxtFile:
        records: List[Diablo2TxtRecord] = list()

        if isinstance(file, TextIOBase):
            f = file
            path = None
        else:
            f = open(file, "r")
            path = file

        # In a properly formed Diablo 2 .txt file, the first line is
        # always a header containing field names.
        header = self._as_data(f.readline())

        # To be *somewhat* efficient, each record will share the set
        # of fields parsed from the .txt file. However, by doing this
        # we need to be careful that the field mapping is not mutable.
        # If one record's field mapping were changed, it would impact
        # *all* records from the same file. That would be confusing
        # and very undesirable behavior, so we provide read-only access
        # to fields using the MappingProxyType.
        fields = MappingProxyType({v.casefold(): k for k, v in enumerate(header)})

        for line in f.readlines():
            record = Diablo2TxtRecord(fields, self._as_data(line))
            if self.skip_record(record):
                continue
            records.append(record)

        return Diablo2TxtFile(path, records)

    @classmethod
    def _as_data(cls, line: str) -> Sequence[str]:
        """
        Splits a line from a Diablo 2 .txt file into a sequence
        of data fields.

        :param line: the line to process
        """
        return line.rstrip("\r\n").split("\t")
