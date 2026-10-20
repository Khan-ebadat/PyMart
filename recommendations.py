
from collections import deque

from products import catalog


# Product ID -> related product IDs
recommendation_graph = {
    "P101": ["P102", "P103", "P104"],
    "P102": ["P101", "P103"],
    "P103": ["P101", "P102", "P104"],
    "P104": ["P101", "P103"],
    "P105": ["P102", "P104"],
}


def recommend_products(product_id, max_hops=2):
    """Find related products within max_hops graph connections."""

    if product_id not in catalog:
        print("Product not found.")
        return []

    visited = {product_id}
    queue = deque([(product_id, 0)])
    recommendations = []

    while queue:
        current_id, distance = queue.popleft()

        if distance == max_hops:
            continue

        for neighbor_id in recommendation_graph.get(current_id, []):
            if neighbor_id not in visited:
                visited.add(neighbor_id)
                queue.append((neighbor_id, distance + 1))
                recommendations.append(neighbor_id)

    print(
        f"\n--- Recommendations for "
        f"{catalog[product_id].name} ---"
    )

    if not recommendations:
        print("No recommendations found.")
        return []

    for recommended_id in recommendations:
        product = catalog[recommended_id]
        print(
            f"{recommended_id} | {product.name} | "
            f"Rs. {product.price:,} | Stock: {product.stock}"
        )

    return recommendations
