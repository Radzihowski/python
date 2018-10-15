inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]


print("Inventory:")
for i in range(len(dragonLoot)):
    for k,v in inv.items():
        if dragonLoot[i] == k:
            v = v +1
            print(v)
        print(i)
print(inv)
