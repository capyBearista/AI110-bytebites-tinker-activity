"""Simple test script to verify ByteBites core behaviors."""

from models import Item, Customer, MenuCatalog, Transaction

# Create some menu items
burger = Item(id=1, name="Spicy Burger", price=8.99, category="Main", popularity_rating=4.5)
fries = Item(id=2, name="Crispy Fries", price=3.50, category="Sides", popularity_rating=4.8)
soda = Item(id=3, name="Large Soda", price=2.99, category="Drinks", popularity_rating=4.2)

print("✓ Created items:")
print(f"  - {burger.name} (${burger.price}), category: {burger.category}")
print(f"  - {fries.name} (${fries.price}), category: {fries.category}")
print(f"  - {soda.name} (${soda.price}), category: {soda.category}")
print()

# Create a menu catalog
catalog = MenuCatalog()
catalog.add_item(burger)
catalog.add_item(fries)
catalog.add_item(soda)

print(f"✓ Created MenuCatalog with {len(catalog.items)} items")
print()

# Create a customer
alice = Customer(id=101, name="Alice", email="alice@example.com")
print(f"✓ Created Customer:")
print(f"  - Name: {alice.name}, Email: {alice.email}")
print(f"  - Loyalty Points: {alice.loyalty_points}")
print(f"  - Purchase History: {len(alice.purchase_history)} transactions")
print()

# Create a transaction for Alice
txn1 = Transaction(id=501, customer=alice)
txn1.add_item(burger)
txn1.add_item(fries)

print(f"✓ Created Transaction:")
print(f"  - Customer: {txn1.customer.name}")
print(f"  - Items in transaction: {len(txn1.selected_items)}")
print(f"  - Status: {txn1.status}")
print(f"  - Date: {txn1.date}")
print()

# Add transaction to customer's purchase history
alice.add_transaction(txn1)
print(f"✓ Added transaction to customer's history")
print(f"  - {alice.name} now has {len(alice.purchase_history)} transaction(s)")
print()

# Filtering checks
drinks_only = catalog.filter_by_category("Drinks")
assert len(drinks_only) == 1
assert drinks_only[0].name == "Large Soda"
print("✓ filter_by_category works")

# Sorting checks
sorted_by_price_desc = catalog.sort_items(by="price", descending=True)
assert [item.name for item in sorted_by_price_desc] == ["Spicy Burger", "Crispy Fries", "Large Soda"]

sorted_by_name_asc = catalog.sort_items(by="name", descending=False)
assert [item.name for item in sorted_by_name_asc] == ["Crispy Fries", "Large Soda", "Spicy Burger"]
print("✓ sort_items works for ascending and descending order")

# Total checks
txn_total = txn1.calculate_total()
assert round(txn_total, 2) == 12.49
assert round(txn1.total, 2) == 12.49
assert round(alice.total_spent(), 2) == 12.49

empty_txn = Transaction(id=502, customer=alice)
assert empty_txn.calculate_total() == 0
print("✓ calculate_total and total_spent work")

print("=" * 50)
print("All scaffold tests passed! ✓")
