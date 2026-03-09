import pytest
from models import Menu, MenuItem, Order, User

def test_order_total_sums_prices_correctly():
    """Order.total() returns the sum of item prices for multiple items."""
    order = Order()
    # Fixed parameter order: name, price, category, popularity_rating
    burger = MenuItem("Burger", 10.0, "Entree", 50)
    soda = MenuItem("Soda", 5.0, "Drinks", 20)
    
    order.add_item(burger)
    order.add_item(soda)
    
    assert order.total() == pytest.approx(15.0)


def test_empty_order_returns_zero_total():
    """An empty order returns a total of 0."""
    order = Order()
    assert order.total() == 0.0


def test_filter_menu_items_by_category():
    """Filtering a menu by category returns only matching items."""
    menu = Menu()
    # Fixed parameter order: name, price, category, popularity_rating
    burger = MenuItem("Burger", 10.0, "Entree", 50)
    soda = MenuItem("Soda", 5.0, "Drinks", 20)
    fries = MenuItem("Fries", 3.0, "Side", 30)
    
    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(fries)
    
    entrees = menu.filter_by_category("Entree")
    
    assert len(entrees) == 1
    assert entrees[0].name == "Burger"