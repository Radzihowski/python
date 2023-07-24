# 8.9 Challenge: Simulate an Election

# Write a program thet simulates the election ten thousand times and prints the percentage of times in which Candidate A wins
# To keep things simple, assume that a candidate wins the election if the win in at least two of the three regions.

from random import random

# calculate chances to win in one region
def regional_election(chance_A_to_wins):
    if random() < chance_A_to_wins:
        return "A"
    else:
        return "B"

# based on regional calculate overall election output. Number of Candidate B won we can find out from the len of list
# minus number of Candidate A won
def run_election(regional_election_chances):
    num_regions_A_won = 0
    for chance_A_to_wins in regional_election_chances:
        if regional_election(chance_A_to_wins) == "A":
            num_regions_A_won = num_regions_A_won + 1
    num_regions_B_won = len(regional_election_chances) - num_regions_A_won

    if num_regions_A_won > num_regions_B_won:
        return "A"
    else:
        return "B"

chances_A_to_win_in_regions = [.87, .65, .17]
number_of_simulations = 10000
numbers_A_won = 0
numbers_B_won = 0

for simulation in range(number_of_simulations):
    if run_election(chances_A_to_win_in_regions) == "A":
        numbers_A_won += 1
    else:
        numbers_B_won += 1

print(f"Probability A won: {numbers_A_won / number_of_simulations}")
print(f"Probability B won: {numbers_B_won / number_of_simulations}")