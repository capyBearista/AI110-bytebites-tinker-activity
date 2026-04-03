"""Simple test script to verify scaffold classes instantiate correctly."""

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
catalog.items.append(burger)
catalog.items.append(fries)
catalog.items.append(soda)

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
txn1.selected_items.append(burger)
txn1.selected_items.append(fries)

print(f"✓ Created Transaction:")
print(f"  - Customer: {txn1.customer.name}")
print(f"  - Items in transaction: {len(txn1.selected_items)}")
print(f"  - Status: {txn1.status}")
print(f"  - Date: {txn1.date}")
print()

# Add transaction to customer's purchase history
alice.purchase_history.append(txn1)
print(f"✓ Added transaction to customer's history")
print(f"  - {alice.name} now has {len(alice.purchase_history)} transaction(s)")
print()

print("=" * 50)
print("All scaffold tests passed! ✓")
