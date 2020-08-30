from cheapest_shipment import Test
import unittest

#Class that holds the test cases to check the correct functionlity of the CheapestShipment method
class CheapestShipmentTests(unittest.TestCase):

    # test case with order items matching the inventory availablity
    def test_inventory_match(self):
        order = {'apple': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        order_output = [{'owd': {'apple': 1}}]
        self.assertEqual(order_output, Test.CheapestShipment(order, inventory))

    # test case with order items that cannot be fulfilled by the inventory availablity
    def test_inventory_insufficient(self):
        order = {'apple': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 0}}]
        order_output = []
        self.assertEqual(order_output, Test.CheapestShipment(order, inventory))

    # test case in which the order is satisfied by availablity in multiple warehouses
    def test_order_split_across_warehouses(self):
        order = {'apple': 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5}},
                     {'name': 'dm', 'inventory': {'apple': 5}}]
        order_output = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
        self.assertEqual(order_output, Test.CheapestShipment(order, inventory))

    # test case with and order but empty inventory
    def test_inventory_blank(self):
        order = {'apple': 10}
        inventory = []
        order_output = []
        self.assertEqual(order_output, Test.CheapestShipment(order, inventory))

    # test case with empty order
    def test_order_blank(self):
        order = {}
        inventory = [{'name': 'owd', 'inventory': {'apple': 10, 'banana': 5, 'orange': 15}},
                     {'name': 'dm', 'inventory': {'apple': 5, 'banana': 20, 'orange': 5}}]
        order_output = []
        self.assertEqual(order_output, Test.CheapestShipment(order, inventory))

    # test case with multiple order items
    def test_order_multiple_items(self):
        order = {'apple': 10, 'banana': 10, 'orange': 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 10, 'banana': 5, 'orange': 15}},
                     {'name': 'dm', 'inventory': {'apple': 5, 'banana': 20, 'orange': 5}}]
        order_output = [{'owd': {'apple': 10, 'banana': 5, 'orange': 10}}, {'dm': {'banana': 5}}]
        self.assertEqual(order_output, Test.CheapestShipment(order, inventory))

    # test case with multiple order items matching mutiple inventories
    def test_multiple_items_and_inventories(self):
        order = {'apple': 15, 'banana': 20, 'orange': 20}
        inventory = [{'name': 'owd', 'inventory': {'apple': 10, 'banana': 5, 'orange': 15}},
                     {'name': 'dm', 'inventory': {'apple': 5, 'banana': 20, 'orange': 5}},
                     {'name': 'xn', 'inventory': {'apple': 5, 'orange': 10}}]
        order_output = [{'owd': {'apple': 10, 'banana': 5, 'orange': 15}}, {'dm': {'apple': 5, 'banana': 15, 'orange': 5}}]
        self.assertEqual(order_output, Test.CheapestShipment(order, inventory))

    # test case with order item not matching any inventory availablity
    def test_order_does_not_exist(self):
        order = {'apple': 15, 'banana': 20, 'orange': 20, 'watermelon': 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 10, 'banana': 5, 'orange': 15}},
                     {'name': 'dm', 'inventory': {'apple': 5, 'banana': 20, 'orange': 5}},
                     {'name': 'xn', 'inventory': {'apple': 5, 'orange': 10}}]
        order_output = []
        self.assertEqual(order_output, Test.CheapestShipment(order, inventory))


if __name__ == '__main__':
    unittest.main()
