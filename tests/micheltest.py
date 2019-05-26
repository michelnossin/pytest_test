import tdd_checkout_example.checkout as victim

item = {"name": "car", "price": 11200, "quantity": 3}

checkout = victim.Checkout()

checkout.add_item_price(item)

total_price = checkout.calculate_total_price(discount=False)

print(total_price)
