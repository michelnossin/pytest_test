class Checkout:
    def __init__(self):
        self._item_list = []

    def add_item_price(self, item):
        def raise_exception():
            print("raise exception")
            raise ValueError
        try:
            if item["price"]:
                self._item_list.append(dict(item))
        except KeyError:
            raise_exception()

    def calculate_total_price(self):
        return sum([item["price"] for item in self._item_list])
