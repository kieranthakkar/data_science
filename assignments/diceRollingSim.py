# DICE ROLLER w/ upper and lower bounds as arguements in the function declaration.
# By default, dice are 6-sided with min. roll = 1 and max. roll = 6.
# Program will ask if user wants to roll again, inputting "no" ends the program.

# Importing the 'random' module to generate random integers
import random

def dice_roller(min: int = 1, max: int = 6) -> str:
    # Tests to see the data can be processed
    if min == max:
        # Returns an error message for intangible dice
        return "Error: Invalid range, minimum value can't be equal to the maximum."
    elif min > max:
        # If minimum > maximum, values are swapped to prevent an error 
        # random.randint(a,b) requires b>=a.
        min,max = max,min

    # Generating and printing the result    
    result = random.randint(min,max)
    print(f"[{min}-{max}] You rolled a {result}!")

    # User input and re-roll loop
    # Program requires "no" input to break
    while True:
        reroll = input("Would you like to roll again? ")
        if reroll.lower() in "yes":
            result = random.randint(min,max)
            print(f"[{min}-{max}] You rolled a {result}!")
            continue
        elif reroll.lower() in "no":
            return "Thank you for rolling the dice :)"
        else:
            print("Please enter (yes/no)")

# Testing
#print(dice_roller())       # Classic dice (1 to 6 by default)
#print(dice_roller(2,20))   # Modified dice rolling between 2 and 20


