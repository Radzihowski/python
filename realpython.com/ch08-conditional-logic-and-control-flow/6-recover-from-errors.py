# 8.6 - Recover From Errors

# Example 1 prevent program from crashing
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("That was not an integer")

# Example 2 multiple exceptions types
def divide(num1, num2):
    try:
        print(num1/num2)
    except (TypeError, ZeroDivisionError):
        print("encounter a problem")

divide(5, "2")
divide(5, 0)
divide(5, 2)

# Example 3 catching multiple exceptions
def divide2(num1, num2):
    try:
        print(num1 / num2)
    except TypeError:
        print("Both arguments must be numbers ")
    except ZeroDivisionError:
        print("num2 must not be 0")

divide2(5, "2")
divide2(5, 0)
divide2(5, 2)

# Exercise 1 write a program  that repeatedly asks the user to input an integer. If the user enter something other than an integer,
# then the program should catch the ValueError and display the message "Try again". Once the user enters an integer, the program
# should display the number back to the user and end without crashing

while True:
    try:
        user_input = input("Type integer: ")
        print(int(user_input))
        break
    except ValueError:
        print("Try again")

# Exercise 2 Write a program thet askjs the user to input a string and an integer n, then displays the character at index n in the string
# use error handling to make sure the program doesn't crash if the user enters soemthing other than an integer or if the index
# is out of out of bonds. The program should display a different message depending on which error occures

user_string = input("Type a string: ")

try:
    user_integer = int(input("Type an index: "))
    print(user_string[user_integer])
except ValueError:
    print("That was not an integer.")
except IndexError:
    print("Index out of bonds.")

