from tdd_checkout_example import filesystem as fs
import pytest
from pytest import raises
from unittest.mock import MagicMock


@pytest.fixture(scope="session")
def fs_handler():
    return fs.FilesystemHandler()


@pytest.fixture()
def mock_read_from_file(fs_handler, monkeypatch):
    def mock_read_from_file(filename):
        if filename == "badfile":
            raise Exception("Bad filename")
        return "CORRECT_STRING"
    monkeypatch.setattr(fs_handler, 'read_from_file', mock_read_from_file)
    return mock_read_from_file


def test_read_from_file_returns_correct_string(
        fs_handler, mock_read_from_file, monkeypatch):
    result = fs_handler.read_from_file("somefile")
    assert result == "CORRECT_STRING"


def test_read_from_file_throws_exception_badfile(
        fs_handler, mock_read_from_file, monkeypatch):
    with raises(Exception):
        fs_handler.read_from_file("badfile")
