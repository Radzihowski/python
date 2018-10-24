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
                break

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    item = 0
    for k, v in inventory.items():
        item_total = item_total + v
        print(str(v) + " " + str(k))
    print("Total number of items: " + str(item_total))

addToInventory(inv, dragonLoot)
displayInventory(inv)
