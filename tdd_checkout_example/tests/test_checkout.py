from tdd_checkout_example import checkout as ch
import pytest
from pytest import raises

@pytest.fixture(scope="session")
def checkout_cart():
    return ch.Checkout()


def test_can_add_item_price(checkout_cart):
    item = {"name": "car", "price": 11200}
    checkout_cart.add_item_price(item)
    assert len(checkout_cart._item_list) == 1

    item = {"name": "man", "price": 16200}
    checkout_cart.add_item_price(item)
    assert len(checkout_cart._item_list) == 2


def test_can_calculate_total_price(checkout_cart):
    assert checkout_cart.calculate_total_price() == 27400


def test_throw_exception_missing_price(checkout_cart):
    item = {"name": "woman"}

    with raises(ValueError):
        checkout_cart.add_item_price(item)
