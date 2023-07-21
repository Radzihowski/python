# 8.5 - Break Out of the Pattern

# Using break, write a program that repeatedly asks the user for some input and quits only if the user enters "q" or "Q"
while True:
    user_input = input("Type 'q' or 'Q' to quit")
    if user_input.lower() == "q":
        break

# Using continue, write a program that loops over the numbers 1 to 50 and prints all numbers that are NOT multiple of 3
for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)
