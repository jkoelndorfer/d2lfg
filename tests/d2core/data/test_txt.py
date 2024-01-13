"""
``tests.d2core.data.test_txt``
==============================

This module contains tests for Diablo 2 .txt processing code.
"""

from io import StringIO
from pathlib import Path

import pytest

from d2lfg.d2core.data.txt import Diablo2TxtFile, Diablo2TxtParser, Diablo2TxtRecord


@pytest.fixture
def axe_txt_record() -> Diablo2TxtRecord:
    """
    A mock :py:class:`~d2lfg.d2core.data.txt.Diablo2TxtRecord`.
    """
    fields = {
        "name": 0,
        "type": 1,
        "type2": 2,
        "code": 3,
        "alternategfx": 4,
        "namestr": 5,
        "mindam": 6,
        "maxdam": 7,
        "1or2handed": 8,
        "2handed": 9,
        "2handmindam": 10,
        "2handmaxdam": 11,
        "minmisdam": 12,
        "maxmisdam": 13,
        "rangeadder": 14,
        "speed": 15,
        "strbonus": 16,
        "dexbonus": 17,
        "reqstr": 18,
        "reqdex": 19,
        "durability": 20,
        "nodurability": 21,
        "level": 22,
        "levelreq": 23,
        "cost": 24,
        "gamble cost": 25,
        "normcode": 26,
        "ubercode": 27,
        "ultracode": 28,
        "2handedwclass": 29,
        "invwidth": 30,
        "invheight": 31,
    }

    data = [
        "Axe",
        "axe",
        "",
        "axe",
        "axe",
        "axe",
        "4",
        "11",
        "",
        "",
        "",
        "",
        "",
        "",
        "1",
        "10",
        "100",
        "",
        "32",
        "",
        "24",
        "",
        "7",
        "0",
        "403",
        "8821",
        "axe",
        "9ax",
        "7ax",
        "1hs",
        "2",
        "3",
    ]
    return Diablo2TxtRecord(fields, data)


@pytest.fixture
def txt_parser() -> Diablo2TxtParser:
    """
    A :py:class:`~d2lfg.d2core.data.txt.Diablo2TxtParser` suitable
    for testing.
    """
    return Diablo2TxtParser()


@pytest.fixture
def weapons_txt_snippet_path() -> Path:
    """
    Path to a partial valid Weapons.txt.
    """
    this_dir = Path(__file__).parent
    return this_dir / "fixtures" / "snippet-weapons.txt"


class TestDiablo2TxtRecord:
    """
    Tests :py:class:`~d2lfg.d2core.data.txt.Diablo2TxtRecord`.
    """

    def test_equivalent_records_compare_equal(self) -> None:
        """
        Verifies that two :py:class:`~d2lfg.d2core.data.txt.Diablo2TxtRecord`
        objects that are equivalent compare as equal.
        """
        fields = {
            "f1": 0,
            "f2": 1,
        }
        data = ["f1val", "f2val"]

        assert Diablo2TxtRecord(fields, data) == Diablo2TxtRecord(fields, data)

    def test_non_record_compares_unequal(self) -> None:
        """
        Verifies that a :py:class:`~d2lfg.d2core.data.txt.Diablo2TxtRecord`
        compares unequal with an object of a different type.
        """
        fields = {
            "f1": 0,
            "f2": 1,
        }
        data = ["f1val", "f2val"]
        assert Diablo2TxtRecord(fields, data) != data

    @pytest.mark.parametrize(
        "key, expected_value",
        [
            (0, "Axe"),
            (6, "4"),
            (26, "axe"),
            (27, "9ax"),
        ],
    )
    def test_getitem_int_returns_correct_value(
        self, axe_txt_record: Diablo2TxtRecord, key: int, expected_value: str
    ) -> None:
        """
        Verifies that an item lookup for
        :py:class:`~d2lfg.d2core.data.txt.Diablo2TxtRecord` returns the correct value
        when the key is an integer.
        """
        assert axe_txt_record[key] == expected_value

    @pytest.mark.parametrize(
        "key, expected_value",
        [
            ("name", "Axe"),
            ("NAME", "Axe"),
            ("MinDam", "4"),
            ("NormCode", "axe"),
            ("ubercode", "9ax"),
        ],
    )
    def test_getitem_string_returns_correct_value(
        self, axe_txt_record: Diablo2TxtRecord, key: str, expected_value: str
    ) -> None:
        """
        Verifies that an item lookup for
        :py:class:`~d2lfg.d2core.data.txt.Diablo2TxtRecord` returns the correct value
        when the key is a string.
        """
        assert axe_txt_record[key] == expected_value

    def test_len_returns_correct_len(self, axe_txt_record: Diablo2TxtRecord) -> None:
        """
        Verifies that :py:class:`~d2lfg.d2core.data.txt.Diablo2TxtRecord` objects
        have the correct length.
        """
        r = axe_txt_record
        assert len(r) == len(r.data) == len(r.fields)

    def test_repr_returns_string(self, axe_txt_record: Diablo2TxtRecord) -> None:
        """
        Verifies that the representation of
        :py:class:`~d2lfg.d2core.data.txt.Diablo2TxtRecord` is a string.
        """
        assert isinstance(repr(axe_txt_record), str)


class TestDiablo2TxtFile:
    """
    Tests :py:class:`~d2lfg.d2core.data.txt.Diablo2TxtFile`.
    """

    def test_init_string_path(self) -> None:
        """
        Verifies that a :py:class:`~d2lfg.d2core.data.txt.Diablo2TxtFile`
        can be initialized with a :py:class:`str` path.
        """
        path_str = "/some/string/path"
        txt_file = Diablo2TxtFile(path_str, [])

        assert txt_file.path == Path(path_str)

    def test_init_pathlib_path(self) -> None:
        """
        Verifies that a :py:class:`~d2lfg.d2core.data.txt.Diablo2TxtFile`
        can be initialized with a :py:class:`pathlib.Path`.
        """
        path = Path("/some/pathlib/path")
        txt_file = Diablo2TxtFile(path, [])

        assert txt_file.path == path


class TestDiablo2TxtParser:
    """
    Tests :py:class:`~d2lfg.d2core.data.txt.Diablo2TxtParser`.
    """

    def test_parse_mostly_empty_record(self, txt_parser: Diablo2TxtParser) -> None:
        """
        Verifies that :py:meth:`~d2lfg.d2core.data.txt.Diablo2TxtParser.parse`
        can parse a mostly-empty record.
        """
        expected_record = Diablo2TxtRecord(
            {"name": 0, "code": 1, "normcode": 2, "ubercode": 3, "ultracode": 4},
            ["Axe", "axe", "axe", "9ax", "7ax"],
        )
        # A record whose first field has a "comment" and all subsequent
        # fields are empty.
        #
        # This is a common pattern used in Diablo 2 .txt files. These
        # records are junk and should not be included in the resulting
        # file.

        mostly_empty_record = ["Expansion", "", "", "", "", ""]
        io = StringIO()

        for row in [
            expected_record.fields.keys(),
            expected_record.data,
            mostly_empty_record,
        ]:
            io.write("\t".join(row))
            io.write("\r\n")
        io.seek(0)

        txt_file = txt_parser.parse(io)

        assert len(txt_file.records) == 1
        assert txt_file.records[0] == expected_record

    def test_parse_incomplete_record(self, txt_parser: Diablo2TxtParser) -> None:
        """
        Verifies that :py:meth:`~d2lfg.d2core.data.txt.Diablo2TxtParser.parse`
        can parse an incomplete record.
        """
        expected_record = Diablo2TxtRecord(
            {"name": 0, "code": 1, "normcode": 2, "ubercode": 3, "ultracode": 4},
            ["Axe", "axe", "axe", "9ax", "7ax"],
        )
        # This is a record that is missing fields. These should not
        # occur in a properly formed .txt file. But if they do, we
        # should omit them as they will be garbage data.
        incomplete_record = ["Hand Axe", "hax"]

        io = StringIO()

        for row in [
            expected_record.fields.keys(),
            expected_record.data,
            incomplete_record,
        ]:
            io.write("\t".join(row))
            io.write("\r\n")
        io.seek(0)

        txt_file = txt_parser.parse(io)

        assert len(txt_file.records) == 1
        assert txt_file.records[0] == expected_record

    def test_parse_weapons_txt_snippet(
        self, txt_parser: Diablo2TxtParser, weapons_txt_snippet_path: Path
    ) -> None:
        """
        Verifies that :py:meth:`~d2lfg.d2core.data.txt.Diablo2TxtParser.parse`
        is able to parse a snippet of an actual .txt file.
        """
        txt_file = txt_parser.parse(weapons_txt_snippet_path)
        hand_axe = txt_file.records[0]

        assert len(txt_file.records) == 2
        assert hand_axe["name"] == "Hand Axe"
        assert hand_axe["code"] == "hax"
        assert hand_axe["gemsockets"] == "2"
