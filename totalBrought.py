allGuests = { "Alice": {"apples": 5, "pretzels": 12}, 
              "Bob": {"ham sandwiches": 3, "apples": 3},
              "Carol":{"cups": 3, "apple pies": 1}}

def totalBrought(guest, item):
    numBrought = 0
    for k, v in guests.item():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print("Number of things being brought:")
print("")
