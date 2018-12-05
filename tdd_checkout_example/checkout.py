class Checkout:
    def __init__(self):
        self._item_list = []
        self._discount_rules_list = []

    def add_item_price(self, item):
        try:
            if item["price"] and item["quantity"] and item["price"]:
                self._item_list.append(dict(item))
        except KeyError:
            raise ValueError

    def calculate_total_price(self, discount):
        price_list = ([item["price"] * item["quantity"]
                       for item in self._item_list])
        total_price_no_discount = (sum(price_list))

        if not discount:
            return total_price_no_discount
        else:
            _discount_prices = []
            for item in self._item_list:
                _applied = False
                for rule in self._discount_rules_list:
                    if item["name"] == rule["name"] and not _applied:
                        _applied = True
                        if item["quantity"] >= rule["minimum_quantity"]:
                            new_price = (item["price"] *
                                         item["quantity"] *
                                         ((100 - rule["discount_percent"])
                                          / 100))
                            _discount_prices.append(new_price)
                        else:
                            new_price = item["price"] * item["quantity"]
                            _discount_prices.append(new_price)
                if not _applied:
                    new_price = item["price"] * item["quantity"]
                    _discount_prices.append(new_price)

            return sum(_discount_prices)

    def add_discount_rule(self, rule):
        try:
            if (rule["name"] and rule["minimum_quantity"]
               and rule["discount_percent"]):
                if (rule["name"] in
                    [item["name"] for item in self._item_list] and
                   rule["minimum_quantity"] >= 0 and
                   rule["discount_percent"] >= 0 and
                   rule["discount_percent"] <= 100):
                    self._discount_rules_list.append(dict(rule))
                else:
                    raise ValueError
        except KeyError:
            raise ValueError
