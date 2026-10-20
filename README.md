# PyMart — Inventory & Order Management System

PyMart is a console-based inventory and order management application built with Python. It demonstrates practical use of Python data structures, modular programming, order processing, and automated unit testing.

## Features

- **Product Catalog:** Display products with prices and available stock.
- **Product Search:** Search products by name, ignoring letter case.
- **Shopping Cart:** Add products, view totals, undo the last addition, and clear the cart.
- **Inventory Management:** Calculate the total value of available inventory.
- **Order Management:** Place orders, validate stock, and process pending orders in FIFO order.
- **Customer Order History:** Maintain completed order history using a custom linked list.
- **Category Browsing:** Browse products through a hierarchical category tree.
- **Product Recommendations:** Find related products using a graph and Breadth-First Search (BFS).
- **Input Validation:** Reject invalid product IDs, invalid quantities, and orders with an empty cart.
- **Automated Testing:** Verify core functionality using Python's `unittest` framework.

## Technologies Used

- Python 3
- Python standard library: `collections`, `namedtuple`, and `unittest`
- Data structures: dictionaries, sets, lists, stacks, queues, linked lists, trees, and graphs
- Algorithms: Breadth-First Search (BFS) and recursion

## Project Structure

| File | Responsibility |
|---|---|
| `main.py` | Application menu and program entry point |
| `products.py` | Product catalog, search, display, and inventory valuation |
| `cart.py` | Shopping cart operations and undo functionality |
| `orders.py` | Order placement, FIFO processing, and customer order history |
| `categories.py` | Product category tree and recursive browsing |
| `recommendations.py` | Product recommendation graph and BFS |
| `test_main.py` | Automated unit tests |

## Getting Started

### Prerequisites

Install Python 3 and ensure that the `python` command works in your terminal.

Check your installation:

```bash
python --version
```

### Run the Application

Clone or download this repository, open a terminal in the project directory, and run:

```bash
python main.py
```

### Run the Tests

Run the automated test suite:

```bash
python -m unittest -v
```

The current test suite contains **14 tests**, all of which pass.

## Example Workflow

1. Display the available products.
2. Add a product to the shopping cart.
3. Place an order under a customer's name.
4. Process the next pending order.
5. View the customer's completed order history.

Example output:

```text
Added 4 x Mouse.
Order #1001 placed successfully! Total: Rs. 3,000
Processing order #1001

--- Customer Order History ---
Order #1001 | Customer: Rahul | Total: Rs. 3,000
```

## Learning Outcomes

This project demonstrates how to:

- Organize a Python application into reusable modules.
- Select appropriate data structures for different tasks.
- Implement FIFO order processing.
- Use linked lists to maintain customer order history.
- Apply recursion to hierarchical data.
- Implement BFS for graph traversal and recommendations.
- Write automated tests for important application behavior.

## Future Improvements

- Persist products and orders in a database.
- Add a graphical or web-based interface.
- Add user authentication and role-based access.
- Generate sales reports and analytics.
- Add more comprehensive tests for edge cases.

---

**Project:** PyMart — Console-Based Inventory & Order Management System  
**Language:** Python
