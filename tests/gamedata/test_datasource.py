"""
``tests.gamedata.test_datasource``
==================================

This module contains tests for Diablo 2 game data source provider code.
"""

from pathlib import Path

import pytest

from d2lfg.d2core.data.txt import Diablo2TxtFile
from d2lfg.error import InvalidTxtDirectory
from d2lfg.gamedata.datasource import Diablo2FilesystemTxtDataSource

from tests.testhelper.typing import PathTyper

fixtures_dir = Path(__file__).parent / "fixtures"


@pytest.fixture
def alltxt_filesystem_txt_data_source(
    pathtyper: PathTyper,
) -> Diablo2FilesystemTxtDataSource:
    """
    Returns a Diablo2FileSystemTxtDataSource that contains all required
    .txt files. The files are syntactically valid but not complete datasets.
    """
    return Diablo2FilesystemTxtDataSource(pathtyper(fixtures_dir / "alltxt"))


@pytest.fixture
def noarmor_filesystem_txt_data_source(
    pathtyper: PathTyper,
) -> Diablo2FilesystemTxtDataSource:
    """
    Returns a Diablo2FileSystemTxtDataSource whose directory does not
    contain ``Armor.txt``.
    """
    return Diablo2FilesystemTxtDataSource(pathtyper(fixtures_dir / "noarmor"))


class TestFilesystemTxtDataSource:
    """
    Tests FilesystemTxtDataSource.
    """

    def test_extraneous_file_not_processed(
        self,
        alltxt_filesystem_txt_data_source: Diablo2FilesystemTxtDataSource,
    ) -> None:
        """
        Validates that unrecognized files are not processed by
        Diablo2FilesystemTxtDataSource.
        """

        assert "armor.txt" in alltxt_filesystem_txt_data_source.required_txt_paths
        assert "armor.bin" not in alltxt_filesystem_txt_data_source.required_txt_paths
        assert (alltxt_filesystem_txt_data_source.data_path / "armor.bin").exists()

    def test_valid_txt_dir_returns_all_txts(
        self,
        alltxt_filesystem_txt_data_source: Diablo2FilesystemTxtDataSource,
    ) -> None:
        """
        Validates that a Diablo2FilesystemTxtDataSource provides Diablo2TxtFiles
        for a valid source directory.
        """
        t = alltxt_filesystem_txt_data_source

        assert isinstance(t.armor_txt, Diablo2TxtFile)
        assert isinstance(t.bodylocs_txt, Diablo2TxtFile)
        assert isinstance(t.itemtypes_txt, Diablo2TxtFile)
        assert isinstance(t.misc_txt, Diablo2TxtFile)
        assert isinstance(t.playerclass_txt, Diablo2TxtFile)
        assert isinstance(t.skills_txt, Diablo2TxtFile)
        assert isinstance(t.weapons_txt, Diablo2TxtFile)

    def test_partial_txt_dir_raises_error(
        self,
        noarmor_filesystem_txt_data_source: Diablo2FilesystemTxtDataSource,
    ) -> None:
        """
        Validates that a Diablo2FilesystemTxtDataSource raises an error if a
        .txt file is missing.
        """

        with pytest.raises(InvalidTxtDirectory):
            noarmor_filesystem_txt_data_source.armor_txt
