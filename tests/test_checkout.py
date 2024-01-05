from src.checkout import Checkout
from src.constants import pricing_rules


def test_scan_item():
    co = Checkout(pricing_rules)
    co.scan('A')
    assert co.cart['A'] == 1

def test_total_price():
    co = Checkout(pricing_rules)
    co.scan('A')
    co.scan('A')
    total = co.total()
    assert total == 100  # 2 * 50 (unit_price of 'A')

def test_calculate_item_price():
    co = Checkout(pricing_rules)
    price_a = co.calculate_item_price('A', 3)  # Should use special price
    price_b = co.calculate_item_price('B', 2)  # Should use special price
    price_c = co.calculate_item_price('C', 1)  # Should use unit price
    assert price_a == 130
    assert price_b == 45
    assert price_c == 20
