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
    
    result = random.randint(min,max)
    print(f"[{min}-{max}] You rolled a {result}!")

    while True:
        reroll = input("Would you like to roll again? ")
        if reroll.lower() in "yes":
            result = random.randint(min,max)
            print(f"[{min}-{max}] You rolled a {result}!")
            continue
        elif reroll.lower() in "no,exit":
            return "Thank you for rolling the dice :)"
        else:
            print("Please enter (yes/no)")

dice_roller.__annotations__

#print(dice_roller())        # Classic dice (1 to 6 by default)
#print(dice_roller(2,20))    # Adjusted dice rolling between 2 and 20
#print(dice_roller(0,4))     # Error. Invalid range (Min value != 0)
#print(dice_roller(6,1))     # Error. Invalid range (Min < Max)



