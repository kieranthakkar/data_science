# kieranthakkar, Murtaza3D
# GUESS THE NUMBER
# This program uses the random module to generate a random integer between 0 and X, where X is a user-defined upper bound.
# User will input guesses and the program will respond accordingly to help the user.

# Importing the 'random' module to generate random integers
import random

def number_guesser():
    # Defining function / local variables.
    # Take user input to set the upper-bound of range - program requires a positive integer input.
    upperBound = input("Type a number (upper bound): ")
    # Checking to see if user input is a positive integer.
    if upperBound.isdigit():
        # If input is +integer, cast upperBound to type int.
        upperBound = int(upperBound)
        # Check to ensure there is a non-zero range. If input == 0, function/program is restarted.
        if upperBound == 0:
            print("Range can't be equal to 0. Please enter a different number.")
            return number_guesser()
        # Numbers reaching here have passed the checks and are then used to generate a random integer.
        else:
            ans = random.randint(0, upperBound)
    # Restart program if input != positive integer
    else:
        print("Please type a positive integer.")
        return number_guesser()
    