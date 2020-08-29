import unittest

from inventory_allocation import InventoryAllocator

class TestInventoryAllocator(unittest.TestCase):
    def test_perfect_match_single_warehouse(self):
        """
        Simple case 1: order can be shipped using one warehouse (perfect match). 
            This test is a sanity check. 
        """
        ordered_items, warehouse_inventories = { 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 1 } }]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        expected_output = [{ 'owd': { 'apple': 1 } }]
        # print(actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_sufficient_inventory_single_warehouse(self):
        """
        Case 3: order cannot be fulfilled because of insufficient inventory for one item (larger order and warehouses list). 
        """
        ordered_items, warehouse_inventories = { 'apple': 10 }, [{ 'name': 'dm', 'inventory': { 'apple': 17 }}]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        expected_output = [{ 'dm': { 'apple': 10 } }]
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

    def test_perfect_match_mult_warehouses(self):
        """
        Case 3: order cannot be fulfilled because of insufficient inventory for one item (larger order and warehouses list). 
        """
        ordered_items, warehouse_inventories = { 'apple': 10 }, [{ 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 1 } } , { 'name': 'dm', 'inventory': { 'apple': 5 }}]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        # expected_output = [{ 'dm': { 'apple': 5 }}, { 'owd': { 'apple': 5 } }]
        expected_output = [{ 'owd': { 'apple': 5 } }, { 'dm': { 'apple': 5 }}]
        # print(actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_sufficient_inventory_mult_warehouses(self):
        """
        Case 3: order cannot be fulfilled because of insufficient inventory for one item (larger order and warehouses list). 
        """
        ordered_items, warehouse_inventories = { 'apple': 10 }, [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 6 }}]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        # expected_output = [{ 'dm': { 'apple': 5 }}, { 'owd': { 'apple': 5 } }]
        expected_output = [{ 'owd': { 'apple': 5 } }, { 'dm': { 'apple': 5 }}]
        # print(actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_sufficient_inventory_mult_warehouses_mult_item_ordered(self):
        """
        Case 3: order cannot be fulfilled because of insufficient inventory for one item (larger order and warehouses list). 
        """
        ordered_items, warehouse_inventories = { 'apple': 2, 'banana': 5,'orange': 2 }, [ { 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 10 } }, { 'name': 'dm', 'inventory': { 'banana': 5, 'orange': 10 } } ]
        actual_output = InventoryAllocatorTest.get_allocation(ordered_items, warehouse_inventories)
        # expected_output = [{ 'dm': { 'apple': 5 }}, { 'owd': { 'apple': 5 } }]
        expected_output = [{ 'owd': { 'apple': 2, 'orange': 2  } }, { 'dm': { 'banana': 5 }}]
        # print(actual_output)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    InventoryAllocatorTest = InventoryAllocator()
    unittest.main()
    