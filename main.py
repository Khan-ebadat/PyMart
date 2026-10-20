
from collections import deque
from products import (
    Product,
    catalog,
    product_names,
    search_product,
    display_products,
    calculate_inventory_value,
)

from cart import (
    cart_stack,
    clear_cart,
    add_to_cart,
    undo_last_add,
    view_cart,
)

from orders import (
    Order,
    Node,
    LinkedList,
    order_queue,
    sales_count,
    customer_histories,
    place_order,
    process_next_order,
    display_pending_orders,
)

from categories import (
    CategoryNode,
    root_category,
    electronics,
    clothing,
    phones,
    laptops,
    accessories,
    men,
    women,
    get_products_in_category,
    browse_category,
)

from recommendations import recommendation_graph, recommend_products




def get_positive_integer(prompt):
    """Keep asking until the user enters a positive integer."""
    while True:
        value = input(prompt).strip()

        try:
            number = int(value)
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if number <= 0:
            print("Please enter a number greater than zero.")
            continue

        return number


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
        print("8. Place order")
        print("9. Process next order")
        print("10. Display pending orders")
        print("11. View customer order history")
        print("12. Browse products by category")
        print("13. Get product recommendations")
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
            product_id = input("Enter product ID: ").strip().upper()
            quantity = get_positive_integer("Enter quantity: ")
            
            add_to_cart(product_id, quantity)


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
       
        elif choice == "7":
            clear_cart()
            print("Cart cleared successfully.")

        elif choice == "8":
            customer_name = input("Enter customer name: ")
            success, message = place_order(customer_name)
            print(message)

        elif choice == "9":
            order = process_next_order()
            if order:
                print(f"Processing order #{order.order_id}")
            else:
                print("No pending orders to process.")

        elif choice == "10":
            count = display_pending_orders()
            print(f"Total pending orders: {count}")

        
        elif choice == "11":
            customer_name = input("Enter customer name: ").strip()

            if customer_name in customer_histories:
                customer_histories[customer_name].print_history()
            else:
                print(f"No completed orders found for {customer_name}.")
        elif choice == "12":
            browse_category()
        elif choice == "13":
            product_id = input("Enter product ID: ").strip().upper()
            recommend_products(product_id)


        elif choice == "0":
            print("Thank you for using PyMart!")
            break

        else:
            print("Invalid option. Choose 0 to 13.")


if __name__ == "__main__":
    main()