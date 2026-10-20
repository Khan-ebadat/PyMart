
from collections import namedtuple, deque

from products import catalog
from cart import cart_stack, clear_cart


# Each order is an immutable record.
Order = namedtuple(
    "Order",
    ["order_id", "customer_name", "items", "total"]
)


class Node:
    """One node containing an order and a link to the next node."""

    def __init__(self, order):
        self.order = order
        self.next = None


class LinkedList:
    """Store a customer's completed orders in chronological order."""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_order(self, order):
        """Append an order to the end of the linked list."""
        new_node = Node(order)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_history(self):
        """Display newest orders first without changing the list."""
        if self.head is None:
            print("No order history found.")
            return []

        stack = []
        current = self.head

        while current is not None:
            stack.append(current.order)
            current = current.next

        history = []
        print("\n--- Customer Order History ---")

        while stack:
            order = stack.pop()
            history.append(order)

            print(
                f"Order #{order.order_id} | "
                f"Customer: {order.customer_name} | "
                f"Total: Rs. {order.total:,}"
            )

        return history


# Pending orders are processed in FIFO order.
order_queue = deque()

# Order IDs start at 1001.
next_order_id = 1001

# Number of units sold per product.
sales_count = {
    product_id: 0
    for product_id in catalog
}

# Customer name -> linked list of completed orders.
customer_histories = {}


def place_order(customer_name):
    """Create an order and add it to the pending queue."""
    global next_order_id

    customer_name = customer_name.strip()

    if not customer_name:
        return False, "Customer name cannot be empty."

    if not cart_stack:
        return False, "Your cart is empty."

    # Combine repeated cart entries for the same product.
    quantities = {}

    for product_id, quantity in cart_stack:
        quantities[product_id] = (
            quantities.get(product_id, 0) + quantity
        )

    # Validate all products before changing any stock.
    for product_id, quantity in quantities.items():
        if product_id not in catalog:
            return False, f"Product {product_id} no longer exists."

        if quantity > catalog[product_id].stock:
            return False, (
                f"Not enough stock for "
                f"{catalog[product_id].name}."
            )

    # Store an immutable snapshot of the ordered items.
    items = tuple(quantities.items())

    total = sum(
        catalog[product_id].price * quantity
        for product_id, quantity in items
    )

    order = Order(
        next_order_id,
        customer_name,
        items,
        total
    )

    # Reserve stock when the order is accepted.
    for product_id, quantity in items:
        product = catalog[product_id]
        catalog[product_id] = product._replace(
            stock=product.stock - quantity
        )

    order_queue.append(order)
    next_order_id += 1

    # Empty the cart after successful checkout.
    clear_cart()

    return True, (
        f"Order #{order.order_id} placed successfully! "
        f"Total: Rs. {order.total:,}"
    )


def process_next_order():
    """Process the oldest order and update sales and history."""
    if not order_queue:
        return None

    order = order_queue.popleft()

    for product_id, quantity in order.items:
        sales_count[product_id] += quantity

    customer_name = order.customer_name

    if customer_name not in customer_histories:
        customer_histories[customer_name] = LinkedList()

    customer_histories[customer_name].add_order(order)

    return order


def display_pending_orders():
    """Display pending orders without removing them."""
    if not order_queue:
        print("\nNo pending orders.")
        return 0

    print("\n--- Pending Orders ---")

    for order in order_queue:
        print(
            f"Order #{order.order_id} | "
            f"Customer: {order.customer_name} | "
            f"Total: Rs. {order.total:,}"
        )

    return len(order_queue)
