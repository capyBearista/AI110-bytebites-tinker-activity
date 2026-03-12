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