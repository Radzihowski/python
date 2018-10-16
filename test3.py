inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]

print("Inventory:")
for i in list(dragonLoot):
    inv.get(dragonLoot[i], 1)
print(inv)

