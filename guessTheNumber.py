# This is a guess the number game.
import random

initialStart = "yes"
while initialStart == "yes" or initialStart != "no":
    secretNumber = random.randint(1, 20)
    print("Paul, I am thinking of a number between 1 and 20.")

    # Ask the player to guess 6 times.
    for guessesTaken in range(1, 7):
        print("Take a guess")
        guess = int(input())

        if guess < secretNumber:
            print("Your guess is too low.")
        elif guess > secretNumber:
            print("Your guess is too high.")
        else:
            break # This condition is the correct guess!

    if guess == secretNumber:
        print("Good job, Paul! You guessed my number in " + str(guessesTaken) + " guesses!")
    else:
        print("Nope. The number I was thinking of was " + str(secretNumber))
    print("would you like to play again yes/no?")
    initialStart = input()
