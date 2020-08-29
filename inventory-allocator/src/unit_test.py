import unittest

from inventory_allocation import InventoryAllocator

class TestInventoryAllocator(unittest.TestCase):
    def test_perfect_match(self):
        """
        Simple case 1: order can be shipped using one warehouse (perfect match). 
            This test is a sanity check. 
        """
        ordered_items, warehouse_inventories = { 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 1 } }]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        expected_output = [{ 'owd': { 'apple': 1 } }]
        # print(actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_insufficient_inventory_1_item_variant1(self):
        """
        Simple case 2: order cannot be fulfilled because of insufficient inventory for one item. 
        """
        ordered_items, warehouse_inventories = { 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 0 } }]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        expected_output = []
        # print(actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_insufficient_inventory_1_item_variant2(self):
        """
        Simple case 2: order cannot be fulfilled because of insufficient inventory for one item. 
        """
        ordered_items, warehouse_inventories = { 'apple': 4 }, [{ 'name': 'owd', 'inventory': { 'apple': 3 } }]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        expected_output = []
        # print(actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_insufficient_inventory_1_item_variant3(self):
        """
        Case 3: order cannot be fulfilled because of insufficient inventory for one item (larger order and warehouses list). 
        """
        ordered_items, warehouse_inventories = { 'apple': 2, 'orange': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 1 ,'orange': 1 } }]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        expected_output = []
        # print(actual_output)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    InventoryAllocatorTest = InventoryAllocator()
    unittest.main()

# Order can be shipped using multiple warehouses
# Input: { apple: 10 }, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]
# Output: [{ dm: { apple: 5 }}, { owd: { apple: 5 } }]

# order = { 'apple': 10 }
# # inventories = [{ 'name': 'owd', 'inventory': { 'apple': 1 } }]
# inventories = [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 6 }}]

# order = { 'apple': 2, 'banana': 5,'orange': 2 }
#         inventories = [ { 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 10 } }, { 'name': 'dm', 'inventory': { 'banana': 5, 'orange': 10 } } ]


#         order = { 'apple': 2, 'orange': 2 }
#         inventories = [{ 'name': 'owd', 'inventory': { 'apple': 1 ,'orange': 1 } }]

#         []

#         order = { 'apple': 2, 'orange': 1 }
#         inventories = [{ 'name': 'owd', 'inventory': { 'apple': 1 ,'orange': 1 } }]


        # inventories = [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 6 }}]

        # order = { 'apple': 2, 'orange': 2 }
        # inventories = [{ 'name': 'owd', 'inventory': { 'apple': 4 ,'orange': 6 } }]


# Order can be shipped using one warehouse
# Input: { apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]
# Output: [{ owd: { apple: 1 } }]

# Order can be shipped using multiple warehouses
# Input: { apple: 10 }, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]
# Output: [{ dm: { apple: 5 }}, { owd: { apple: 5 } }]

# Order cannot be shipped because there is not enough inventory
# Input: { apple: 1 }, [{ name: owd, inventory: { apple: 0 } }]
# Output: []

# Input: { apple: 2 }, [{ name: owd, inventory: { apple: 1 } }]
# Output: []