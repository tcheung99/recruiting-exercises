class InventoryAllocator:
    def get_allocation(self, order, warehouse_inventories):
        return_order = list() 
        warehouse_order = dict()
        for item in order.keys():
            item_amount = order.get(item)

            # warehouse_order = dict()
            # Handle each item sequentially, and check each warehouse for inventory for that item
            for i, warehouse in enumerate(warehouse_inventories): # This is a list 
                if (item in warehouse['inventory']) and (item_amount > 0):
                    amount_taken = min(item_amount, warehouse['inventory'][item])
                    if not warehouse_order.get(warehouse['name'], None):
                        warehouse_order[warehouse['name']] = {item : amount_taken}
                    else:
                        # print(warehouse_order)
                        warehouse_order[warehouse['name']].update({item : amount_taken})
                        # else:

                    item_amount -= warehouse['inventory'][item]
                    warehouse['inventory'][item] -= amount_taken

            if item_amount > 0:
                print('Insufficient inventory, order requires {} more {}(s) than available.'.format(item_amount, item))
                return []

        print(warehouse_order)
        print(warehouse_inventories)
        return_order.append(warehouse_order)

        return return_order

# not enough inventory in 2nd warehouse 
# multiple items 
# should we remove if the inventory is 0 

if __name__ == "__main__":
    NewAllocator = InventoryAllocator()

    # Manual testing 
    order = { 'apple': 2, 'orange': 9 }
    # inventories = [{ 'name': 'owd', 'inventory': { 'apple': 4 ,'orange': 6 }, 'name': 'lol', 'inventory': { 'banana': 2 ,'orange': 2 } }]
    inventories = [{ 'name': 'owd', 'inventory': { 'apple': 4 ,'orange': 6 }}, {'name': 'lol', 'inventory': { 'banana': 2 ,'orange': 2 } }]
    print('Output: {}'.format(NewAllocator.get_allocation(order, inventories)))

# Warehouses are pre-sorted based on cost. 
