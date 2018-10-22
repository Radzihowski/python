inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]

def addToInventory(inventory, addedItems):
    for val in dragonLoot:
        totalItems = 0
        for k,v in inv.items():
            if val == k:
                totalItems = v + 1
                inv[val] = totalItems
                break
            else:
                inv.setdefault(val, 1)
                print(inv)
                break
inv = addToInventory(inv, dragonLoot)
print("Inventory:") 
print(inv)
