"""
Models for ByteBites backend system.

Classes:
- User: stores user info and purchase history
- MenuItem: stores item details (name, price, category, popularity rating)
- Menu: manages the collection of items and filtering
- Order: groups selected items and calculates the total cost
"""

from typing import List


class User:
    """Represents a ByteBites customer."""
    def __init__(self, name: str):
        self.name: str = name
        self.purchase_history: List["Order"] = []

    def add_purchase(self, order: "Order") -> None:
        """Append a completed Order to purchase_history."""
        self.purchase_history.append(order)

    def get_history(self) -> List["Order"]:
        """Return a copy of the user's purchase history."""
        return list(self.purchase_history)


class MenuItem:
    """Represents a sellable item (name, price, category, popularity_rating)."""
    def __init__(self, name: str, price: float, category: str, popularity_rating: int):
        self.name: str = name
        self.price: float = float(price)
        self.category: str = category
        self.popularity_rating: int = popularity_rating

    def adjust_popularity(self, delta: int) -> None:
        """Adjust popularity_rating by delta."""
        self.popularity_rating += delta


class Menu:
    """Collection managing MenuItem objects and filtering."""
    def __init__(self):
        self.items: List[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        """Add a MenuItem to the menu."""
        self.items.append(item)

    def filter_by_category(self, category: str) -> List[MenuItem]:
        """Return items matching the given category."""
        return [item for item in self.items if item.category == category]


class Order:
    """A purchase transaction grouping selected MenuItems and computing total."""
    def __init__(self):
        self.items: List[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        """Add a MenuItem to this Order."""
        self.items.append(item)

    def total(self) -> float:
        """Compute and return the total cost of items in the order."""
        return sum(item.price for item in self.items)


if __name__ == "__main__":
    # Create menu items
    burger = MenuItem("Spicy Burger", 8.99, "Entree", 75)
    fries = MenuItem("Fries", 3.49, "Side", 60)
    soda = MenuItem("Large Soda", 2.50, "Drinks", 90)
    salad = MenuItem("Garden Salad", 5.99, "Entree", 50)

    # Create a menu and add items
    menu = Menu()
    menu.add_item(burger)
    menu.add_item(fries)
    menu.add_item(soda)
    menu.add_item(salad)

    print("Full Menu:")
    for item in menu.items:
        print(item.name, "-", item.category, "-", item.price)

    # Filter menu items by category
    entrees = menu.filter_by_category("Entree")
    print("\nFiltered (Entree items):")
    for item in entrees:
        print(item.name)

    # Sort menu by popularity
    sorted_menu = sorted(menu.items, key=lambda item: item.popularity_rating, reverse=True)
    print("\nMenu sorted by popularity:")
    for item in sorted_menu:
        print(item.name, "-", item.popularity_rating)

    # Create an order
    order = Order()
    order.add_item(burger)
    order.add_item(soda)

    print("\nOrder items:")
    for item in order.items:
        print(item.name)

    # Compute total
    print("\nOrder total:", order.total())

    # Create a user and record purchase
    user = User("Alice")
    user.add_purchase(order)

    print("\nUser purchase history:")
    for past_order in user.get_history():
        print("Order total:", past_order.total())