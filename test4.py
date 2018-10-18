inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]

print("Inventory:")
for val in dragonLoot:
    for k in inv.keys():
##        print(val)
##        print(k)
        if val == k:
            print("ok")
        else:
            print("fail")
print(inv)


