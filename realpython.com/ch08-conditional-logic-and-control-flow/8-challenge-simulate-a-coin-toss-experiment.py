# Exercise 1
# Write a simulation that runs ten thousands trials of the experiment and prints the average number of flips per trial

import random

def coin_flip():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

num_trials = 10000
counter = 0

for trial in range(num_trials):
    if coin_flip() == "heads":
        counter = counter + 1
        while coin_flip() == "heads":
            counter = counter + 1
        counter = counter + 1
    else:
        counter = counter + 1
        while coin_flip() == "tails":
            counter = counter + 1
        counter = counter + 1
average = counter / num_trials
print(f"Average number of flips ter trial {average}")