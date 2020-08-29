# Assumptions: 
# 1. Warehouses are pre-sorted based on cost. 
# 2. Output list order is in the order of least cost (0-indexed) to highest cost (index -1)

class InventoryAllocator:
    def get_allocation(self, ordered_items: dict(), warehouse_inventories: list(dict())) -> list(dict()):

        # Initialize the list of warehouses to ship from (the returned list)
        cheapest_shipment = list() 

        # Initialize a dictionary to hold the necessary shipments from each warehouse 
        warehouse_orders = dict()
        
        for item in ordered_items.keys():
            item_amount = ordered_items.get(item)

            # Handle each item sequentially, and check each warehouse for inventory for that item
            for warehouse in (warehouse_inventories): # This is a list 
                if (item in warehouse['inventory']) and (item_amount > 0):
                    amount_taken = min(item_amount, warehouse['inventory'][item])
                    if not warehouse_orders.get(warehouse['name'], None):
                        warehouse_orders[warehouse['name']] = {item : amount_taken}
                    else:
                        warehouse_orders[warehouse['name']].update({item : amount_taken})

                    item_amount -= warehouse['inventory'][item]
                    warehouse['inventory'][item] -= amount_taken

            if item_amount > 0:
                # print('Insufficient inventory, order requires {} more {}(s) than available.'.format(item_amount, item))
                return []

        for (k,v) in warehouse_orders.items():
            cheapest_shipment.append({k:v})

        return cheapest_shipment

if __name__ == "__main__":
    NewAllocator = InventoryAllocator()

    # Manual testing
    order = { 'apple': 2, 'orange': 9 }
    inventories = [{ 'name': 'owd', 'inventory': { 'apple': 4 ,'orange': 6 }}, {'name': 'lol', 'inventory': { 'banana': 2 ,'orange': 2 } }]

    print('Output: {}'.format(NewAllocator.get_allocation(order, inventories)))
