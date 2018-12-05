class Checkout:
    def __init__(self):
        self._item_list = []
        self._discount_rules_list = []

    def add_item_price(self, item):
        try:
            if item["price"]:
                self._item_list.append(dict(item))
        except KeyError:
            raise ValueError

    def calculate_total_price(self):
        return sum([item["price"] for item in self._item_list])

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
