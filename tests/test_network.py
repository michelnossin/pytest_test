from tdd_checkout_example.network import Network
from unittest.mock import MagicMock


def test_call_and_return_good_result(monkeypatch):
    mock_result = MagicMock()
    mock_result.text = "Favourite_Data_Engineer"
    mock_get = MagicMock(return_value=mock_result)
    monkeypatch.setattr("requests.get", mock_get)
    result = Network().get_url("http://www.nossin.com")
    mock_get.assert_called_once_with("http://www.nossin.com")
    assert result.text == "Favourite_Data_Engineer"
