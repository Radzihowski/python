# 9.3 Exercises

# 1. Create a tuple called data with two values. The first value should be the tuple(1, 2), and the second value should be the tuple(3, 4).
data = ((1, 2), (3, 4))
print(data)

# 2. Write a for loop that loops over data and prints the sum of each nested tuple. The output should look like this:
# Row 1 sum: 3
# Row 2 sum: 4
i = 1
for k in data:
    print(f"Row {i} sum: {sum(k)}")
    i += 1

# 3. Create the list [4, 3, 2, 1] and assign it to the variable numbers
numbers = [4, 3, 2, 1]
print(numbers)

# 4. crate a copy of the numbers list using the [:] slice notation
copy_number = numbers[:]
print(copy_number)

# 5. Sort the numbers list in numerical order using .sort()
numbers.sort()
print(numbers)

