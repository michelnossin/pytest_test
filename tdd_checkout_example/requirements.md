- Can create instance of Checkout class
- Set price on Item
- Add item to Checkout list
- Calculate current total cost all added items
- Add mutiple items and get correct total
- Add discount rules
- Apply discount rules based on N type of items
- Exception thrown if item is added without price

First add tests which fails
test_can_create_checkout_instance
calling Checkout() which does not exist

Later on we have some new requirements for IO (Mock)
- Can call readfrom file
- readfromfile gets a correct string
- readfromfile throws exception if file does not exist
