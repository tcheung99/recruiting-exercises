import unittest

from inventory_allocation import InventoryAllocator

class TestInventoryAllocator(unittest.TestCase):

    # Tests with a single warehouse
    def test_perfect_match_single_warehouse(self):
        """
        Case 1: order can be shipped using one warehouse (perfect match). 
            This test is a sanity check. 
        """
        ordered_items, warehouse_inventories = { 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 1 } }]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        expected_output = [{ 'owd': { 'apple': 1 } }]
        self.assertEqual(actual_output, expected_output)

    def test_sufficient_inventory_single_warehouse(self):
        """
        Case 2: order can be shipped using one warehouse (inventory is greater than requested order amount). 
        """
        ordered_items, warehouse_inventories = { 'apple': 10 }, [{ 'name': 'dm', 'inventory': { 'apple': 17 }}]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        expected_output = [{ 'dm': { 'apple': 10 } }]
        self.assertEqual(actual_output, expected_output)

    def test_insufficient_inventory_1_item_variant1(self):
        """
        Case 3: order cannot be fulfilled because of insufficient inventory for one item. 
        """
        ordered_items, warehouse_inventories = { 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 0 } }]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        expected_output = []
        self.assertEqual(actual_output, expected_output)

    def test_insufficient_inventory_1_item_variant2(self):
        """
        Case 4: order cannot be fulfilled because of insufficient inventory for one item. 
        """
        ordered_items, warehouse_inventories = { 'apple': 4 }, [{ 'name': 'owd', 'inventory': { 'apple': 3 } }]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        expected_output = []
        self.assertEqual(actual_output, expected_output)

    def test_insufficient_inventory_1_item_variant3(self):
        """
        Case 5: order cannot be fulfilled because of insufficient inventory for one item (with larger order map and warehouses list). 
        """
        ordered_items, warehouse_inventories = { 'apple': 2, 'orange': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 1 ,'orange': 1 } }]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        expected_output = []
        self.assertEqual(actual_output, expected_output)

    def test_not_in_inventory_single_warehouses(self):
        """
        Case 6: single-item order cannot be fulfilled because of insufficient inventory at any warehouse. 
        """
        ordered_items, warehouse_inventories = { 'mango': 100 }, [ { 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 10 } }, { 'name': 'dm', 'inventory': { 'banana': 5, 'orange': 10} } ]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        expected_output = []
        self.assertEqual(actual_output, expected_output)

    # Tests with multiple warehouses
    def test_perfect_match_mult_warehouses(self):
        """
        Case 7: order can be shipped using multiple warehouses (perfect match for each item). 
        """
        ordered_items, warehouse_inventories = { 'apple': 10 }, [{ 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 1 } } , { 'name': 'dm', 'inventory': { 'apple': 5 }}]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        expected_output = [{ 'owd': { 'apple': 5 } }, { 'dm': { 'apple': 5 }}]
        self.assertEqual(actual_output, expected_output)

    def test_sufficient_inventory_mult_warehouses(self):
        """
        Case 8: order can be shipped using multiple warehouses (where the inventory at each warehouse can be greater than requested order amount). 
        """
        ordered_items, warehouse_inventories = { 'apple': 10 }, [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 6 }}]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        expected_output = [{ 'owd': { 'apple': 5 } }, { 'dm': { 'apple': 5 }}]
        self.assertEqual(actual_output, expected_output)

    def test_sufficient_inventory_mult_warehouses_mult_item_ordered(self):
        """
        Case 9: multi-item order can be shipped using multiple warehouses (where the inventory at each warehouse can be greater than requested order amount). 
        """
        ordered_items, warehouse_inventories = { 'apple': 2, 'banana': 5,'orange': 2 }, [ { 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 10 } }, { 'name': 'dm', 'inventory': { 'banana': 5, 'orange': 10 } } ]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        expected_output = [{ 'owd': { 'apple': 2, 'orange': 2  } }, { 'dm': { 'banana': 5 }}]
        self.assertEqual(actual_output, expected_output)

    def test_insufficient_inventory_mult_warehouses(self):
        """
        Case 10: multi-item order cannot be fulfilled because of insufficient inventory at any warehouse. 
        """
        ordered_items, warehouse_inventories = { 'apple': 2, 'mango': 100,'orange': 8 }, [ { 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 10 } }, { 'name': 'dm', 'inventory': { 'banana': 5, 'orange': 10, 'mango': 10 } } ]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        expected_output = []
        self.assertEqual(actual_output, expected_output)

    def test_not_in_inventory_mult_warehouses(self):
        """
        Case 11: multi-item order cannot be fulfilled because of insufficient inventory at any warehouse. 
        """
        ordered_items, warehouse_inventories = { 'apple': 2, 'mango': 100,'watermelon': 8 }, [ { 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 10 } }, { 'name': 'dm', 'inventory': { 'banana': 5, 'orange': 10} } ]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        expected_output = []
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    InventoryAllocatorTest = InventoryAllocator()
    unittest.main()
