
from collections import namedtuple

# Product records are immutable namedtuples.
Product = namedtuple("Product", ["name", "price", "stock"])


# Product ID -> Product
catalog = {
    "P101": Product("Laptop", 62000, 5),
    "P102": Product("Mouse", 750, 20),
    "P103": Product("Keyboard", 1500, 12),
    "P104": Product("Headphones", 2500, 8),
    "P105": Product("Smartphone", 25000, 10),
}

# Fast membership checks for product names.
product_names = {
    product.name.lower()
    for product in catalog.values()
}

# Each entry records one addition to the cart.
# This list is used as a stack so the latest addition can be undone.
cart_stack = []


def search_product(name):
    """Return (product_id, product), or None if not found."""
    normalized_name = name.strip().lower()

    # Step 1: Fast membership check using the existing set.
    if normalized_name not in product_names:
        return None

    # Step 2: Find the full product record.
    for product_id, product in catalog.items():
        if product.name.lower() == normalized_name:
            return product_id, product

    return None


def display_products(products=catalog):
    """Display products and return the number displayed."""
    print("\n--- PyMart Product Catalog ---")

    for product_id, product in products.items():
        print(
            f"{product_id} | {product.name} | "
            f"Rs. {product.price:,} | Stock: {product.stock}"
        )

    return len(products)


def calculate_inventory_value():
    inventory_values = {
        product_id: product.price * product.stock
        for product_id, product in catalog.items()
    }

    return sum(inventory_values.values())

def clear_cart():
    """Remove all items from the shopping cart."""
    cart_stack.clear()
    return True


def add_to_cart(product_id, quantity=1):
    """Add one cart entry if the product and quantity are valid."""
    if product_id not in catalog:
        return False, "Product ID not found."

    if not isinstance(quantity, int) or isinstance(quantity, bool):
        return False, "Quantity must be a whole number."

    if quantity <= 0:
        return False, "Quantity must be greater than zero."

    product = catalog[product_id]

    # Include previous additions when checking available stock.
    already_added = sum(
        qty for pid, qty in cart_stack if pid == product_id
    )

    if already_added + quantity > product.stock:
        return False, "Not enough stock available."

    cart_stack.append((product_id, quantity))
    return True, f"Added {quantity} x {product.name}."


def undo_last_add():
    """Undo the most recent cart addition."""
    if not cart_stack:
        return None

    return cart_stack.pop()


def view_cart():
    """Display cart totals and return the total price."""
    if not cart_stack:
        print("\nYour cart is empty.")
        return 0

    total = 0

    print("\n--- Shopping Cart ---")

    for product_id, quantity in cart_stack:
        product = catalog[product_id]
        subtotal = product.price * quantity
        total += subtotal

        print(
            f"{product.name} x {quantity} = Rs. {subtotal:,}"
        )

    print(f"Cart total: Rs. {total:,}")
    return total


def main():
    while True:
        print("\n===== PyMart =====")
        print("1. Display products")
        print("2. Search product")
        print("3. Add to cart")
        print("4. Undo last addition")
        print("5. View cart")
        print("6. Show inventory value")
        print("7. Clear cart")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_products()

        elif choice == "2":
            name = input("Enter product name: ")
            result = search_product(name)

            if result is None:
                print("Product not found.")
            else:
                product_id, product = result
                print(product_id, product)

        elif choice == "3":
            product_id = input("Enter product ID: ").strip()

            # Basic validation without try/except.
            quantity_text = input("Enter quantity: ").strip()

            if not quantity_text.isdigit():
                print("Enter a valid positive whole number.")
                continue

            success, message = add_to_cart(
                product_id, int(quantity_text)
            )
            print(message)

        elif choice == "4":
            undone = undo_last_add()

            if undone is None:
                print("Nothing to undo.")
            else:
                product_id, quantity = undone
                print(f"Undid addition: {product_id} x {quantity}")

        elif choice == "5":
            view_cart()
    
        elif choice == "6":
            total_value = calculate_inventory_value()
            print(f"Total inventory value: Rs. {total_value:,}")

        elif choice == "0":
            print("Thank you for using PyMart!")
            break

        else:
            print("Invalid option. Choose 0 to 5.")


if __name__ == "__main__":
    main()