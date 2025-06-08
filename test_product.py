import pytest
from products import Product

def test_create_valid_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.get_quantity() == 100
    assert product.is_active() is True

def test_create_invalid_product_raises_exception():
    with pytest.raises(Exception):
        Product("", price=1450, quantity=100)  # Empty name

    with pytest.raises(Exception):
        Product("MacBook Air M2", price=-10, quantity=100)  # Negative price

    with pytest.raises(Exception):
        Product("MacBook Air M2", price=1450, quantity=-5)  # Negative quantity

def test_product_becomes_inactive_at_zero_quantity():
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.buy(1)
    assert product.get_quantity() == 0
    assert product.is_active() is False

def test_product_purchase_updates_quantity_and_returns_price():
    product = Product("MacBook Air M2", price=1450, quantity=10)
    total = product.buy(2)
    assert total == 2900
    assert product.get_quantity() == 8

def test_buy_more_than_available_raises_exception():
    product = Product("MacBook Air M2", price=1450, quantity=5)
    with pytest.raises(Exception):
        product.buy(10)
