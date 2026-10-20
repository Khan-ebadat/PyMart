
import unittest

import main


class TestPyMart(unittest.TestCase):

    def setUp(self):
        """Reset the cart before each test."""
        main.clear_cart()

    def test_search_existing_product(self):
        result = main.search_product("Laptop")

        self.assertIsNotNone(result)
        self.assertEqual(result[0], "P101")
        self.assertEqual(result[1].name, "Laptop")

    def test_search_is_case_insensitive(self):
        result = main.search_product("lApToP")

        self.assertIsNotNone(result)
        self.assertEqual(result[0], "P101")

    def test_search_missing_product(self):
        result = main.search_product("Unknown Product")

        self.assertIsNone(result)

    def test_add_valid_product_to_cart(self):
        success, message = main.add_to_cart("P101", 1)

        self.assertTrue(success)
        self.assertEqual(main.cart_stack, [("P101", 1)])

    def test_reject_invalid_product_id(self):
        success, message = main.add_to_cart("INVALID", 1)

        self.assertFalse(success)
        self.assertEqual(main.cart_stack, [])

    def test_reject_zero_quantity(self):
        success, message = main.add_to_cart("P101", 0)

        self.assertFalse(success)
        self.assertEqual(main.cart_stack, [])

    def test_undo_last_cart_addition(self):
        main.add_to_cart("P101", 1)

        removed = main.undo_last_add()

        self.assertEqual(removed, ("P101", 1))
        self.assertEqual(main.cart_stack, [])

    def test_inventory_value_is_positive(self):
        value = main.calculate_inventory_value()

        self.assertGreater(value, 0)



    def test_place_order_reduces_stock_and_clears_cart(self):
        original_stock = main.catalog["P101"].stock

        main.add_to_cart("P101", 1)
        success, message = main.place_order("Test Customer")

        self.assertTrue(success)
        self.assertEqual(
            main.catalog["P101"].stock,
            original_stock - 1
        )
        self.assertEqual(main.cart_stack, [])
        self.assertEqual(len(main.order_queue), 1)

        # Clean up the queued order and restore stock.
        main.process_next_order()
        main.catalog["P101"] = main.catalog["P101"]._replace(
            stock=original_stock
        )

    def test_reject_order_with_empty_cart(self):
        success, message = main.place_order("Test Customer")

        self.assertFalse(success)
        self.assertEqual(len(main.order_queue), 0)

    def test_orders_are_processed_fifo(self):
        main.add_to_cart("P102", 1)
        success1, _ = main.place_order("Customer One")
        self.assertTrue(success1)

        main.add_to_cart("P103", 1)
        success2, _ = main.place_order("Customer Two")
        self.assertTrue(success2)

        first = main.process_next_order()
        second = main.process_next_order()

        self.assertEqual(first.customer_name, "Customer One")
        self.assertEqual(second.customer_name, "Customer Two")

        # Restore stock for these test orders.
        main.catalog["P102"] = main.catalog["P102"]._replace(
            stock=main.catalog["P102"].stock + 1
        )
        main.catalog["P103"] = main.catalog["P103"]._replace(
            stock=main.catalog["P103"].stock + 1
        )



    def test_electronics_category_contains_five_products(self):
        products = main.get_products_in_category(
            main.electronics
        )

        product_ids = {product_id for product_id, _ in products}

        self.assertEqual(
            product_ids,
            {"P101", "P102", "P103", "P104", "P105"}
        )

    def test_phones_category_contains_smartphone(self):
        products = main.get_products_in_category(main.phones)

        product_ids = [product_id for product_id, _ in products]

        self.assertEqual(product_ids, ["P105"])

    def test_laptop_recommendations(self):
        recommendations = main.recommend_products(
            "P101",
            max_hops=1
        )

        self.assertEqual(
            set(recommendations),
            {"P102", "P103", "P104"}
        )
        self.assertNotIn("P101", recommendations)



if __name__ == "__main__":
    unittest.main()
