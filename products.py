
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


def search_product(name):
    """Return (product_id, product), or None if not found."""
    normalized_name = name.strip().lower()

    if normalized_name not in product_names:
        return None

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
    """Calculate the total value of all available inventory."""
    inventory_values = {
        product_id: product.price * product.stock
        for product_id, product in catalog.items()
    }

    return sum(inventory_values.values())
