"""
d2lfl.diablo.data.txt
=====================

Contains code to implement a Diablo2Database backed by
.txt files.
"""

from pathlib import Path
from types import MappingProxyType
from typing import Dict, Iterable, Iterator, Mapping, Optional, Sequence, Union

from ..game.item import Diablo2Armor, Diablo2BodyLoc, Diablo2Item, Diablo2ItemType, Diablo2Weapon
from ..game.skill import Diablo2Skill
from .database import Diablo2Database


class Diablo2TxtRecord:
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
        return self.data[self.field_indices[index.lower()]]

    def __len__(self) -> int:
        return len(self.data)

    def __repr__(self) -> str:
        return repr({k: self.data[v] for k, v in self.field_indices.items()})


class Diablo2TxtFile:
    """
    Object representing a Diablo 2 .txt file.

    Provides .txt file parsing and permits iteration over records.
    """

    def __init__(self, path: Union[Path, str]) -> None:
        if isinstance(path, str):
            self.path = Path(path)
        else:
            self.path = path

        with open(self.path, "r") as f:
            l = f.readline().rstrip("\r\n")
            self._fields = l.split("\t")
            num_fields = len(self._fields)

            self._field_indices = MappingProxyType({v.lower(): k for k, v in enumerate(self._fields)})
            self._records = []

            for l in f.readlines():
                line_fields = l.rstrip("\r\n").split("\t")
                record = Diablo2TxtRecord(self._field_indices, line_fields[:num_fields+1])
                if not self._skip_record(record):
                    self._records.append(record)

    @classmethod
    def _skip_record(cls, record: Diablo2TxtRecord) -> bool:
        # Many txt files have mostly empty lines where the first
        # field is "Expansion" or "Not Used". These are junk data,
        # so exclude them.
        if record[0].lower() in ("expansion", "not used"):
            return True

        # If the record is incomplete (has missing columns), skip it.
        if len(record.data) < len(record.field_indices):
            return True

        try:
            if record["code"] == "":
                return True
        except (IndexError, KeyError):
            pass
        return False

    def fields(self) -> Sequence[str]:
        return list(self._fields)

    def __len__(self) -> int:
        return len(self._records)

    def __getitem__(self, index: int) -> Diablo2TxtRecord:
        return self._records[index]

    def __iter__(self) -> Iterator[Diablo2TxtRecord]:
        for r in self._records:
            yield r


class Diablo2TxtDatabase(Diablo2Database):
    def __init__(
        self,
        item_types_txt: Diablo2TxtFile,
        armor_txt: Diablo2TxtFile,
        misc_txt: Diablo2TxtFile,
        skills_txt: Diablo2TxtFile,
        weapons_txt: Diablo2TxtFile,
    ) -> None:
        """
        Creates a new Diablo2TxtDatabase.

        Diablo2TxtDatabase uses .txt files extracted from Diablo 2 MPQs
        to provide information about game items and skills.

        :param item_types_txt: the data/global/excel/ItemTypes.txt data file
        :param armor_txt: the data/global/excel/Armor.txt data file
        :param misc_txt: the data/global/excel/Misc.txt data file
        :param skills_txt: the data/global/excel/Skills.txt data file
        :param weapons_txt: the data/global/excel/Weapons.txt data file
        """
        self.armor_txt = armor_txt
        self.item_types_txt = item_types_txt
        self.misc_txt = misc_txt
        self.skills_txt = skills_txt
        self.weapons_txt = weapons_txt

        self._item_types_by_code: Dict[str, Diablo2ItemType] = dict()
        self._items_by_code: Dict[str, Diablo2Item] = dict()
        self._armors_by_code: Dict[str, Diablo2Armor] = dict()
        self._weapons_by_code: Dict[str, Diablo2Weapon] = dict()
        self._skills_by_id: Dict[int, Diablo2Skill] = dict()

        self.initialize_db()

    def armor(self, code: str) -> Diablo2Armor:
        return self._armors_by_code[code]

    def all_armors(self) -> Iterable[Diablo2Armor]:
        return self._armors_by_code.values()

    def item(self, code: str) -> Diablo2Item:
        return self._items_by_code[code]

    def all_items(self) -> Iterable[Diablo2Item]:
        return self._items_by_code.values()

    def item_type(self, code: str) -> Diablo2ItemType:
        return self._item_types_by_code[code]

    def _item_type_optional(self, code: Optional[str]) -> Optional[Diablo2ItemType]:
        if code == "" or code is None:
            return None
        return self.item_type(code)

    def skill(self, id: int) -> Diablo2Skill:
        return self._skills_by_id[id]

    def all_skills(self) -> Iterable[Diablo2Skill]:
        return self._skills_by_id.values()

    def weapon(self, code: str) -> Diablo2Weapon:
        return self._weapons_by_code[code]

    def all_weapons(self) -> Iterable[Diablo2Weapon]:
        return self._weapons_by_code.values()

    def initialize_db(self) -> None:
        self.initialize_item_types()
        self.initialize_armor()
        self.initialize_misc()
        # self.initialize_skills()
        # self.initialize_weapons()

    def initialize_item_types(self) -> None:
        for r in self.item_types_txt:
            item_type = Diablo2ItemType(
                r["itemtype"],
                r["code"],
                r["equiv1"],
                r["equiv2"],
                Diablo2BodyLoc.from_string(r["bodyloc1"]),
                Diablo2BodyLoc.from_string(r["bodyloc2"]),
            )
            self._item_types_by_code[item_type.code] = item_type

    def initialize_armor(self) -> None:
        for r in self.armor_txt:
            armor = Diablo2Armor(
                r["code"],
                self.item_type(r["type"]),
                self._item_type_optional(r["type2"]),
                r["name"],
                int(r["level"]),
                int(r["levelreq"]),
                int(r["gemsockets"]),
                int(r["durability"]),
                r["normcode"],
                r["ubercode"],
                r["ultracode"],
                int(r["reqstr"]),
                int(r["minac"]),
                int(r["maxac"]),
            )
            self._items_by_code[armor.code] = armor
            self._armors_by_code[armor.code] = armor

    def initialize_misc(self) -> None:
        for r in self.misc_txt:
            item = Diablo2Item(
                r["code"],
                self.item_type(r["type"]),
                self._item_type_optional(r["type2"]),
                r["name"],
                int(r["level"]),
                int(r["levelreq"]),
            )
            self._items_by_code[item.code] = item