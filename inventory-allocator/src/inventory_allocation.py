class InventoryAllocator:
    def __init__(self):
        # order = { 'apple': 2, 'orange': 2 }
        # inventories = [{ 'name': 'owd', 'inventory': { 'apple': 4 ,'orange': 6 } }]

        order = { 'apple': 2, 'banana': 5,'orange': 2 }
        inventories = [ { 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 10 } }, { 'name': 'dm', 'inventory': { 'banana': 5, 'orange': 10 } } ]

        # inventories = [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 6 }}]

        self.get_allocation(order, inventories)
        

    def sum(self,arg):
        total = 0
        for val in arg:
            total += val
        return total

    def get_allocation(self, order, warehouse_inventories):
        # order = [(dict())]*len(warehouse_inventories)
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
                print('[]')
                
                return []
            else:
                print('----', warehouse_order)
                # return_order.append(warehouse_order)
            

        print(warehouse_order)
        print(warehouse_inventories)
        print(return_order)
        return_order.append(warehouse_order)

        return return_order

# not enough inventory in 2nd warehouse 
# multiple items 
# should we remove if the inventory is 0 

if __name__ == "__main__":
    NewAllocator = InventoryAllocator()

# Warehouses are pre-sorted based on cost. 

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