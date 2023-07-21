# 8.3 Control the Flow of Your Program

# Exercise 1
# Write a program thet prompts the user to enter a word using the input() function and compares the
# lenght of the word to the number five. The program should display one of the outputs,
# depending on the length of the users's input.

user_input = input("Type some word: ")
if len(user_input) < 5:
    print("Your input is less than 5 characters long")
elif len(user_input) > 5:
    print("Your input is greater than 5 character long")
else:
    print("Your input is 5 characters long")


# Exercise 2
# Write a program that displays "I'm thinking of a number between 1 and 10. Guess which one."
# Then use input() to get a number from the user. If the user inputs the number 3, then the program should display
# "You win!" For any other input, the program should display "You lose."

print("I'm thinking of a number between 1 and 10. Guess which one. Guess which one.")

u_input = input("Type your number: ")
if u_input == "3":
    print("You win!")
else:
    print("You lose.")