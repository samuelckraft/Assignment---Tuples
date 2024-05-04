#Task 1

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2)
]

def display_orders(orders):
    print("\nOutgoing orders:")
    for order in orders:
        name, item, quantity = order
        print(f"\nCustomer: {name}\nItem: {item}\nQuantity: {quantity}")

display_orders(orders)