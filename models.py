"""Models for bytebites_tinker_activity

This module summarizes the four main domain classes used by the project.

- Customer: Represents a customer with identifying fields (id, name, email),
  loyalty points, and a purchase history (transactions). Typical methods
  include adding a transaction and computing total spent.

- Item: Represents a menu item with id, name, price, category, and a
  popularity rating. Typical operations include updating price and
  adjusting popularity.

- MenuCatalog: A container for `Item` objects. Responsible for adding,
  removing, finding, and filtering items by category; it provides the
  primary catalog management interface used by the application.

- Transaction: Represents an order placed by a `Customer`, holding
  selected items, timestamps, computed total, and a status field. Typical
  methods include adding/removing items, calculating the total, and
  finalizing the transaction.
"""
from datetime import datetime
from typing import List, Optional

class Item:
    """Represents a menu item with pricing, category, and popularity."""
    
    def __init__(self, id: int, name: str, price: float, category: str, popularity_rating: float):
        self.id: int = id
        self.name: str = name
        self.price: float = price
        self.category: str = category
        self.popularity_rating: float = popularity_rating

    def update_price(self, new_price: float) -> None:
        """Update the price for this item."""
        self.price = new_price

    def adjust_popularity(self, delta: float) -> None:
        """Adjust popularity by a positive or negative delta."""
        self.popularity_rating += delta

class Customer:
    """Represents a customer with loyalty points and purchase history."""
    
    def __init__(self, id: int, name: str, email: str):
        self.id: int = id
        self.name: str = name
        self.email: str = email
        self.loyalty_points: int = 0
        self.purchase_history: List["Transaction"] = []

    def add_transaction(self, transaction: "Transaction") -> None:
        """Add a transaction to the customer's purchase history."""
        self.purchase_history.append(transaction)

    def get_purchase_history(self) -> List["Transaction"]:
        """Return a shallow copy of purchase history."""
        return list(self.purchase_history)

    def total_spent(self) -> float:
        """Compute the total amount spent across all transactions."""
        return sum(transaction.total for transaction in self.purchase_history)

class MenuCatalog:
    """A container for Item objects managing the menu catalog."""
    
    def __init__(self):
        self.items: List[Item] = []

    def add_item(self, item: Item) -> None:
        """Add an item to the catalog."""
        self.items.append(item)

    def remove_item(self, id: int) -> bool:
        """Remove the first item with matching id. Returns True if removed."""
        for index, item in enumerate(self.items):
            if item.id == id:
                del self.items[index]
                return True
        return False

    def filter_by_category(self, category: str) -> List[Item]:
        """Return all items whose category exactly matches the given value."""
        return [item for item in self.items if item.category == category]

    def get_all_items(self) -> List[Item]:
        """Return a shallow copy of all catalog items."""
        return list(self.items)

    def find_item(self, id: int) -> Optional[Item]:
        """Return the first item with matching id, or None if missing."""
        for item in self.items:
            if item.id == id:
                return item
        return None

    def sort_items(self, by: str = "name", descending: bool = False) -> List[Item]:
        """Return catalog items sorted by a supported field."""
        allowed_fields = {"name", "price", "popularity_rating"}
        if by not in allowed_fields:
            raise ValueError(
                f"Unsupported sort key: {by}. Use one of: name, price, popularity_rating"
            )
        return sorted(self.items, key=lambda item: getattr(item, by), reverse=descending)

class Transaction:
    """Represents an order placed by a customer."""
    
    def __init__(self, id: int, customer: Customer):
        self.id: int = id
        self.customer: Customer = customer
        self.selected_items: List[Item] = []
        self.date: datetime = datetime.now()
        self.total: float = 0.0
        self.status: str = "pending"

    def add_item(self, item: Item) -> None:
        """Add one item to the transaction and refresh total."""
        self.selected_items.append(item)
        self.calculate_total()

    def remove_item(self, item: Item) -> None:
        """Remove one matching item from the transaction and refresh total."""
        if item in self.selected_items:
            self.selected_items.remove(item)
        self.calculate_total()

    def calculate_total(self) -> float:
        """Calculate and store the total price for selected items."""
        self.total = sum(item.price for item in self.selected_items)
        return self.total

    def finalize(self) -> None:
        """Finalize this transaction and add it to customer history."""
        self.calculate_total()
        self.status = "finalized"
        if self not in self.customer.purchase_history:
            self.customer.add_transaction(self)