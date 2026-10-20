
from products import catalog


class CategoryNode:
    """Represent one category in the category tree."""

    def __init__(self, name):
        self.name = name
        self.children = []
        self.product_ids = []

    def add_subcategory(self, category):
        """Add a child category."""
        self.children.append(category)

    def add_product(self, product_id):
        """Associate a product ID with this category."""
        self.product_ids.append(product_id)


# Root category
root_category = CategoryNode("All Products")

# Main categories
electronics = CategoryNode("Electronics")
clothing = CategoryNode("Clothing")

root_category.add_subcategory(electronics)
root_category.add_subcategory(clothing)

# Electronics subcategories
phones = CategoryNode("Phones")
laptops = CategoryNode("Laptops")
accessories = CategoryNode("Accessories")

electronics.add_subcategory(phones)
electronics.add_subcategory(laptops)
electronics.add_subcategory(accessories)

# Clothing subcategories
men = CategoryNode("Men")
women = CategoryNode("Women")

clothing.add_subcategory(men)
clothing.add_subcategory(women)

# Assign existing products to categories
phones.add_product("P105")
laptops.add_product("P101")
accessories.add_product("P102")
accessories.add_product("P103")
accessories.add_product("P104")


def get_products_in_category(category, products=catalog):
    """Return products in a category and its subcategories."""
    result = []

    for product_id in category.product_ids:
        if product_id in products:
            result.append((product_id, products[product_id]))

    for child in category.children:
        result.extend(get_products_in_category(child, products))

    return result


def browse_category():
    """Display products belonging to a selected category."""
    categories = {
        "all products": root_category,
        "electronics": electronics,
        "phones": phones,
        "laptops": laptops,
        "accessories": accessories,
        "clothing": clothing,
        "men": men,
        "women": women,
    }

    category_name = input("Enter category name: ").strip().lower()
    category = categories.get(category_name)

    if category is None:
        print("Category not found.")
        return []

    products = get_products_in_category(category)

    print(f"\n--- Products in {category.name} ---")

    if not products:
        print("No products found in this category.")
        return []

    for product_id, product in products:
        print(
            f"{product_id} | {product.name} | "
            f"Rs. {product.price:,} | Stock: {product.stock}"
        )

    return products
