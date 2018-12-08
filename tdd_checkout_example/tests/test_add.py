from tdd_checkout_example.add import AbstractAdder, AddExecutor
from unittest.mock import MagicMock


def test_add_Executor_calls_abstractadder_correct():
    mock_adder = MagicMock(AbstractAdder)
    mock_adder.add = MagicMock(return_value=3)
    result = AddExecutor(mock_adder)
    mock_adder.add.assert_called_once_with(1, 2)
    assert result == 3
