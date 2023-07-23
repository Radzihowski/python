# 8.7 - Simulate Events and Calculate Probabilities

# Example 1
import random

def coin_flip():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

heads_tally = 0
tails_tally = 0

for trial in range (100000):
    if coin_flip() == "heads":
        heads_tally += 1
    else:
        tails_tally += 1

ratio = (heads_tally / tails_tally)
print(f"The ratio of heads to tails is {ratio}")

# Example 2

def unfair_coin_flip(probability_of_tails):
    if random.random() < probability_of_tails:
        return "tails"
    else:
        return "heads"

heads_tally = 0
tails_tally = 0


for trial in range(10000):
    if unfair_coin_flip(.7) == "heads":
        heads_tally += 1
    else:
        tails_tally += 1
ratio = heads_tally / tails_tally
print(f"The ratio of heads of tails is {ratio}")

# Exercise 1
# Write a function called roll() that uses randint() to simulate rolling a fair die by returning a random integer between 1 and 6

def roll():
    return random.randint(1,6)

# Exercise 2
# Write a program that simulates ten thousands rolls of a fair die and displays the average number rolled.
num_rolls = 10_000
total = 0

for trial in range(num_rolls):
    total += roll()

average = total / num_rolls
print(f"The average number rolled is {average}")
