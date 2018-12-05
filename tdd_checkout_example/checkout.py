class Checkout:
    def __init__(self):
        self._item_list = []

    def add_item_price(self, item):
        self._item_list.append(dict(item))
