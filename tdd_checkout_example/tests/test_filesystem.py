from tdd_checkout_example import filesystem as fs
import pytest
from pytest import raises
from unittest.mock import MagicMock


@pytest.fixture(scope="session")
def fs_handler():
    return fs.FilesystemHandler()


def test_read_from_file_returns_correct_string(fs_handler, monkeypatch):
    def mock_read_from_file(filename):
        return "CORRECT_STRING"
    monkeypatch.setattr(fs_handler, 'read_from_file', mock_read_from_file)
    result = fs_handler.read_from_file("somefile")
    assert result == "CORRECT_STRING"
