# 6.4 - Run in Circles
# Solutions to review exercises


# Exercise 1
# Write a for loop that prints out the integers 2 through 10, each on a new line, using range()
for n in range (2,11):
    print(n)

# Exercise 2
# Write a while loop thet print out hte integers 2 through 10
i = 2
while i < 11:
    print(i)
    i = i + 1

# Exercise 3
# Write a function called double() that takes a number as its input and doubles it.
# Then use doubles() in a loop to double the number 2 three times, displaying each result on a separate line
# Here's some sample output:
# 4
# 8
# 16

def doubles(k):
    return k * 2

num = 2
for l in range (0, 3):
    num = doubles(num)
    print(num)
