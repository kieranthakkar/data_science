import random

# Dice roller with upper and lower bounds defined within the function call.
# By default, dice is 6-sided with min. roll = 1 and max. roll = 6.
def dice_roller(min: int = 1, max: int = 6) -> str:
    """# Dice rolling function"""
    if min <= 0:
        return "Error: Invalid range, minimum value must be a positive integer >= 1."
        #Returns 
    elif min >= max:
        return "Error: Invalid range, minumum must be lower than the maximum." 
    
    result = random.randint(min,max)
    print(f"You rolled a {result}!")

    while True:
        reroll = input("Would you like to roll again?  ")
        if reroll.lower() in "yes":
            result = random.randint(min,max)
            print(f"You rolled a {result}!")
            continue
        elif reroll.lower() in "no":
            return "Thank you for rolling the dice :)"
        else:
            print("Please enter (yes/no)")

dice_roller.__annotations__

#print(dice_roller())        # Classic dice (1 to 6 by default)
#print(dice_roller(2,20))    # Adjusted dice rolling between 2 and 20
#print(dice_roller(0,4))     # Error. Invalid range (Min value != 0)
#print(dice_roller(6,1))     # Error. Invalid range (Min < Max)



