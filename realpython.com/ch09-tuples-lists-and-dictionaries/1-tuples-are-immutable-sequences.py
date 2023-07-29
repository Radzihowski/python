# 9.1 Exercises

# 1. Create a tuple ...
cardinal_number = ("first", "second", "third")
print(cardinal_number)

# 2. Using index notation and print() ...
print(cardinal_number[1])

# 3. In a single line of code, unpack the values in cardinal_numbers into three new strings names position1, position2
# position3. Then print each value on separate line
position1, position2, position3 = cardinal_number[0], cardinal_number[1], cardinal_number[2]
print(position1)
print(position2)
print(position3)

# 4. Using tuple() and a string literal, create a tuple called my_name that contains the letters of your name
myname = ("Mark Tapley")
print(myname)

# 5. Check whether the character 'x' is in my_name using the in keyword
print("x" in myname)


# 6. Create a new tuple containing all but the first letter in my_name using slice notation.
new_tuple = myname[1:]
print(new_tuple)
