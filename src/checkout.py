class Checkout:
    def __init__(self, pricing_rules):
        # Initialize the Checkout class with pricing rules and an empty cart
        self.pricing_rules = pricing_rules
        self.cart = {}

    def scan(self, item):
        # Add scanned items to the cart or update the quantity if the item is already in the cart
        if item in self.cart:
            self.cart[item] += 1
        else:
            self.cart[item] = 1

    def total(self):
        # Calculate the total price of all scanned items in the cart
        total_price = sum(self.calculate_item_price(item, quantity) for item, quantity in self.cart.items())
        return total_price

    def calculate_item_price(self, item, quantity):
        # Calculate the price of an item based on the provided pricing rules
        item_data = self.pricing_rules.get(item)
        if item_data:
            unit_price = item_data.get('unit_price', 0)
            special_price = item_data.get('special_price')

            if special_price and quantity >= special_price.get('quantity', 0):
                special_offers, remaining_items = divmod(quantity, special_price['quantity'])
                return special_offers * special_price['price'] + remaining_items * unit_price
            else:
                return quantity * unit_price
        else:
            return 0 # Item not found in pricing rules, so it's free or doesn't exist
