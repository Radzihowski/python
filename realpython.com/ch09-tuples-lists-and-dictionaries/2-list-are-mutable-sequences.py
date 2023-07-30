# 9.2 Exercises

# 1. Create a list named food with two elements, "rice" and "beans"
food = ["rice", "beans"]
print(food)

# 2. Append the string "broccoli" to food using .append()
food.append("broccoli")
print(food)

# 3. Add the strings "bread" and "pizza" to food using .extend()
food.extend(("bread", "pizza"))
print(food)

# 4. Print the first two items in the food list using print() and slice notation
print(food[:2])

# 5. Print the last item in food using print() and index notation
print(food[-1])

# 6. Create a list called breakfast from the string "eggs, fruit, orange, juice" using the string .split() method
breakfast = "eggs, fruit, orange, juice".split(", ")
print(breakfast)

# 7. Verify that breakfast has three items using len()
print(len(breakfast) == 3)

# 8. Create a new list called lengths using a list comprehension that contains the lengths of each string in the
# breakfast list
lengths = [len(item) for item in breakfast]
print(lengths)