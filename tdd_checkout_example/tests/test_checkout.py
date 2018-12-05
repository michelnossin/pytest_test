from tdd_checkout_example import checkout as ch
import pytest


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
