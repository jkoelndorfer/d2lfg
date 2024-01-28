"""
``d2lfg.gamedata.datasource``
=============================

This module contains classes that act as a source for game data.
"""

from abc import ABCMeta, abstractproperty
from os import PathLike
from pathlib import Path
from typing import Dict, Optional, Union

from ..error import InvalidTxtDirectory
from ..d2core.data.txt import Diablo2TxtFile, Diablo2TxtParser

Pathable = Union[str, "PathLike[str]"]


class Diablo2TxtDataSource(metaclass=ABCMeta):
    """
    Abstract class representing a Diablo 2 .txt data source.
    """

    @abstractproperty
    def armor_txt(self) -> Diablo2TxtFile:
        """
        The Armor.txt data file.
        """
        raise NotImplementedError("subclasses must implement armor_txt")

    @abstractproperty
    def bodylocs_txt(self) -> Diablo2TxtFile:
        """
        The BodyLocs.txt data file.
        """
        raise NotImplementedError("subclasses must implement bodylocs_txt")

    @abstractproperty
    def itemtypes_txt(self) -> Diablo2TxtFile:
        """
        The ItemTypes.txt data file.
        """
        raise NotImplementedError("subclasses must implement itemtypes_txt")

    @abstractproperty
    def misc_txt(self) -> Diablo2TxtFile:
        """
        The Misc.txt data file.
        """
        raise NotImplementedError("subclasses must implement misc_txt")

    @abstractproperty
    def playerclass_txt(self) -> Diablo2TxtFile:
        """
        The PlayerClass.txt data file.
        """
        raise NotImplementedError("subclasses must implement playerclass_txt")

    @abstractproperty
    def skills_txt(self) -> Diablo2TxtFile:
        """
        The Skills.txt data file.
        """
        raise NotImplementedError("subclasses must implement skills_txt")

    @abstractproperty
    def weapons_txt(self) -> Diablo2TxtFile:
        """
        The Weapons.txt data file.
        """
        raise NotImplementedError("subclasses must implement weapons_txt")


class Diablo2FilesystemTxtDataSource(Diablo2TxtDataSource):
    """
    Class that provides access to game data via .txt files that are extracted
    to the filesystem.

    This class does *not* read data from MPQ archives.

    This class should be pointed at the directory containing required the following
    required .txt files:

        * Armor.txt
        * BodyLocs.txt
        * ItemTypes.txt
        * Misc.txt
        * PlayerClass.txt
        * Skills.txt
        * Weapons.txt

    :param data_path: path to the directory containing the required .txt files
    """

    def __init__(self, data_path: Pathable) -> None:
        if isinstance(data_path, str):
            self.data_path: Path = Path(data_path)
        else:
            self.data_path = Path(data_path)

        self._txt_parser = Diablo2TxtParser()

        required_txts = {
            "armor.txt",
            "bodylocs.txt",
            "itemtypes.txt",
            "misc.txt",
            "playerclass.txt",
            "skills.txt",
            "weapons.txt",
        }
        self.required_txt_paths: Dict[str, Path] = dict()

        for filename in self.data_path.iterdir():
            filename_cs = filename.name.casefold()

            if filename_cs not in required_txts:
                continue

            self.required_txt_paths[filename_cs] = self.data_path / filename

        self._armor_txt: Optional[Diablo2TxtFile] = None
        self._bodylocs_txt: Optional[Diablo2TxtFile] = None
        self._itemtypes_txt: Optional[Diablo2TxtFile] = None
        self._misc_txt: Optional[Diablo2TxtFile] = None
        self._playerclass_txt: Optional[Diablo2TxtFile] = None
        self._skills_txt: Optional[Diablo2TxtFile] = None
        self._weapons_txt: Optional[Diablo2TxtFile] = None

    def _initialize_txt(self, filename: str) -> Diablo2TxtFile:
        try:
            return self._txt_parser.parse(self.required_txt_paths[filename])
        except KeyError as e:
            f = e.args[0]
            raise InvalidTxtDirectory(f"missing required txt data file {f}")

    @property
    def armor_txt(self) -> Diablo2TxtFile:
        if self._armor_txt is None:
            self._armor_txt = self._initialize_txt("armor.txt")
        return self._armor_txt

    @property
    def bodylocs_txt(self) -> Diablo2TxtFile:
        if self._bodylocs_txt is None:
            self._bodylocs_txt = self._initialize_txt("bodylocs.txt")
        return self._bodylocs_txt

    @property
    def itemtypes_txt(self) -> Diablo2TxtFile:
        if self._itemtypes_txt is None:
            self._itemtypes_txt = self._initialize_txt("itemtypes.txt")
        return self._itemtypes_txt

    @property
    def misc_txt(self) -> Diablo2TxtFile:
        if self._misc_txt is None:
            self._misc_txt = self._initialize_txt("misc.txt")
        return self._misc_txt

    @property
    def playerclass_txt(self) -> Diablo2TxtFile:
        if self._playerclass_txt is None:
            self._playerclass_txt = self._initialize_txt("playerclass.txt")
        return self._playerclass_txt

    @property
    def skills_txt(self) -> Diablo2TxtFile:
        if self._skills_txt is None:
            self._skills_txt = self._initialize_txt("skills.txt")
        return self._skills_txt

    @property
    def weapons_txt(self) -> Diablo2TxtFile:
        if self._weapons_txt is None:
            self._weapons_txt = self._initialize_txt("weapons.txt")
        return self._weapons_txt
