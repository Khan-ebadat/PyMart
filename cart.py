
from products import catalog

cart_stack = []


def clear_cart():
    """Remove all items from the cart."""
    cart_stack.clear()
    print("Cart cleared.")


def add_to_cart(product_id, quantity=1):
    """Add a product and return (success, message)."""

    if product_id not in catalog:
        message = "Invalid product ID."
        print(message)
        return False, message

    if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0:
        message = "Quantity must be a positive integer."
        print(message)
        return False, message

    product = catalog[product_id]

    quantity_in_cart = sum(
        existing_quantity
        for existing_id, existing_quantity in cart_stack
        if existing_id == product_id
    )

    if quantity_in_cart + quantity > product.stock:
        message = "Not enough stock available."
        print(message)
        return False, message

    cart_stack.append((product_id, quantity))
    message = f"Added {quantity} x {product.name}."
    print(message)
    return True, message


def undo_last_add():
    """Remove and return the most recently added cart entry."""

    if not cart_stack:
        message = "Cart is empty. Nothing to undo."
        print(message)
        return None

    removed_item = cart_stack.pop()
    product_id, quantity = removed_item
    product = catalog[product_id]

    print(f"Removed {quantity} x {product.name} from the cart.")
    return removed_item


def view_cart():
    """Display cart contents and return the total price."""

    if not cart_stack:
        print("Cart is empty.")
        return 0

    total = 0
    print("\n--- Shopping Cart ---")

    for product_id, quantity in cart_stack:
        product = catalog[product_id]
        subtotal = product.price * quantity
        total += subtotal

        print(
            f"{product.name} x {quantity} = "
            f"Rs. {subtotal:,}"
        )

    print(f"Total: Rs. {total:,}")
    return total
