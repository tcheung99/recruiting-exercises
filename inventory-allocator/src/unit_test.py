import unittest
from fractions import Fraction

from inventory_allocation import InventoryAllocator
# import inventory_allocation


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = { apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]
        result = InventoryAllocatorTest.sum(data)
        expected_output = [{ owd: { apple: 1 } }]
        self.assertEqual(result, expected_output)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = InventoryAllocatorTest.sum(data)
        self.assertEqual(result, Fraction(9,10))

if __name__ == '__main__':
    


    InventoryAllocatorTest = InventoryAllocator()
    unittest.main()


# order = { 'apple': 10 }
# # inventories = [{ 'name': 'owd', 'inventory': { 'apple': 1 } }]
# inventories = [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 6 }}]



        order = { 'apple': 2, 'orange': 2 }
        inventories = [{ 'name': 'owd', 'inventory': { 'apple': 1 ,'orange': 1 } }]

        []

        order = { 'apple': 2, 'orange': 1 }
        inventories = [{ 'name': 'owd', 'inventory': { 'apple': 1 ,'orange': 1 } }]