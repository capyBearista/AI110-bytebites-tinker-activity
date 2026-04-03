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

class Customer:
    """Represents a customer with loyalty points and purchase history."""
    
    def __init__(self, id: int, name: str, email: str):
        self.id: int = id
        self.name: str = name
        self.email: str = email
        self.loyalty_points: int = 0
        self.purchase_history: List["Transaction"] = []

class MenuCatalog:
    """A container for Item objects managing the menu catalog."""
    
    def __init__(self):
        self.items: List[Item] = []

class Transaction:
    """Represents an order placed by a customer."""
    
    def __init__(self, id: int, customer: Customer):
        self.id: int = id
        self.customer: Customer = customer
        self.selected_items: List[Item] = []
        self.date: datetime = datetime.now()
        self.total: float = 0.0
        self.status: str = "pending"