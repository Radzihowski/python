inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]


print("Inventory:")
for i in list(dragonLoot):
    for k,v in inv.get():
        if str(dragonLoot[i]) == str(k):
            v = v +1
            print(str(k) + " " + str(v))
        else:
            inv.setdefault(dragonLoot[i], 1)
    print(i)

