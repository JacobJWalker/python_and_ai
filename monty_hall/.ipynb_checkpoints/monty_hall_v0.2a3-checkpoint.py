# Name: Monty Hall Game and Monte Carlo Simulation
# Version: 0.2a3
# Summary: A simple game that replicates the Monty Hall problem, and a Monte Carlo simulator to determine probabilities
# Keywords: Monty Hall, Monte Carlo
# Author: Jacob J. Walker
#
# Header comments based on meta-data specs at https://packaging.python.org/specifications/core-metadata/

import random

car_location = random.randint(1,3)

# print(car_location)

# Initialize doors
door = {}
for i in (1,2,3):
    door[i] = "Goat"
#     print(str(i) + ": " + door[i])

door[car_location] = "Car"

# Get guess and tell player whether they won or not
guess = input("Which door do you choose? ")

if door[int(guess)] == "Goat":
    print("Sorry, you got a goat. If you chose door number " + str(car_location) + " you would have won the car...")
elif door[int(guess)] == "Car":
    print("You won a car!!!")
else:
    print("Sorry, I did not understand.")
