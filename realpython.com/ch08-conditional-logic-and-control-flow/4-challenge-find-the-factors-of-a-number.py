# 8.4 - Challenge: Find the Factors of a Number

# Write a program that asks the user to input a possitive integer and then prints out the factors of that number.

print("Enter a positive integer: ")
user_input = int(input())

for divisor in range(1, user_input+1):
    if ( user_input % divisor) == 0:
        print(f"{divisor} is a factor of {user_input}")