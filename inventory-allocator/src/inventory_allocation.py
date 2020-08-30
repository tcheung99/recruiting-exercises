# Assumptions: 
# 1. Warehouses are pre-sorted based on cost. 
# 2. Output list order is in the order of least cost (0-indexed) to highest cost (index -1)
# 3. The input is formatted in a valid manner
# 4. The orders is not empty 

class InventoryAllocator:
    def get_allocation(self, ordered_items: dict(), warehouse_inventories: list(dict())) -> list(dict()):
        """
        Description: Function that identifies the cheapest way to ship the order. 

        Parameters:
            ordered_items (dict()): map of the order's items and the corresponding quantity ordered.
            warehouse_inventories (list(dict())): list of dictionaries which contain the warehouse name and inventory distribution the items.

        Returns:
            cheapest_shipment (list(dict)): list of warehouses and the items and corresponding units taken from that warehouse (corresponds to the cheapest shipment possible).
        """
        
        # Initialize the list of warehouses to ship from (the returned list)
        cheapest_shipment = list() 

        # Initialize a dictionary to hold the necessary shipments from each warehouse 
        warehouse_orders = dict()
        
        # Handle each item sequentially
        for item in ordered_items.keys():
            # Get the number of units requested for the item
            units_requested = ordered_items.get(item)

            # Check each warehouse for inventory for that item
            for warehouse in (warehouse_inventories): 
                # Check that the warehouse inventory contains the item, and that we are still looking for units of that item
                if (item in warehouse['inventory']) and (units_requested > 0):
                    inventory_available = warehouse['inventory'][item]
                    # We only take the minimum between the number of units requested and the inventory available
                    amount_taken = min(units_requested, inventory_available)

                    # Track the amount of units that the warehouse contributed using the warehouse_orders dictionary
                    if not warehouse_orders.get(warehouse['name'], None):
                        warehouse_orders[warehouse['name']] = {item : amount_taken}
                    else:
                        warehouse_orders[warehouse['name']].update({item : amount_taken})

                    # Subtract the amount taken from the amount of units requested, and the warehouse's inventory
                    units_requested -= amount_taken
                    warehouse['inventory'][item] -= amount_taken

            # If we have iterated through all of the warehouses but are still requesting units, we have insufficient inventory! 
            if units_requested > 0:
                return []

        # Add the dictionary items into the list in the correct format (cannot simply append the warehouse_orders dict)
        for (name,item_and_units_taken) in warehouse_orders.items():
            cheapest_shipment.append({name:item_and_units_taken})

        return cheapest_shipment

if __name__ == "__main__":
    NewAllocator = InventoryAllocator()

    # Manual testing
    order = { 'apple': 2, 'orange': 9 }
    inventories = [{ 'name': 'owd', 'inventory': { 'apple': 4 ,'orange': 6 }}, {'name': 'lol', 'inventory': { 'banana': 2 ,'orange': 2 } }]

    print('Output: {}'.format(NewAllocator.get_allocation(order, inventories)))
