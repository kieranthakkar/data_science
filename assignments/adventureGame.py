# kieranthakkar, tanu
# ADVENTURE GAME - a complete text game
# the program will let users move through rooms based on user input and get descriptions of each room. To create this, you’ll need to establish the direction in which the user can move, a way to track how far the user has moved (and therefore which room he/she is in), and to print out a description.
# You’ll also need to set limits for how far the user can move. In other words, create “walls” around the rooms that tell the user, “You can’t move further in this direction.”


# Importing the 'random' module to generate random integers
import random, os

# Starting position
xPos, yPos = 0,-1

# The game - while loop to continuously take input
while True:
    request = input("Request: ").lower()
    if request == "left":
        xPos -= 1
        if xPos:
            pass
        
    if request == "right":
        xPos += 1
    if request == "up":
        yPos += 1
    if request == "down":
        yPos -= 1
    if request == "end" or "quit" or "exit":
        break

    os.system('cls')
    print(f"{xPos},{yPos}")
    
    
    
# Map generation
#  -1,1 print(f"┌───┬───┬───┐\n│ X │   │   │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘")
#   0,1 print(f"┌───┬───┬───┐\n│   │ X │   │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘")
#   1,1 print(f"┌───┬───┬───┐\n│   │   │ X │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘")
#  -1,0 print(f"┌───┬───┬───┐\n│   │   │   │\n├───┼───┼───┤\n│ X │   │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘")
#   0,0 print(f"┌───┬───┬───┐\n│   │   │   │\n├───┼───┼───┤\n│   │ X │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘")
#   1,0 print(f"┌───┬───┬───┐\n│   │   │   │\n├───┼───┼───┤\n│   │   │ X │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘")
# -1,-1 print(f"┌───┬───┬───┐\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│ X │   │   │\n└───┴───┴───┘")
#  0,-1 print(f"┌───┬───┬───┐\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│   │ X │   │\n└───┴───┴───┘")
#  1,-1 print(f"┌───┬───┬───┐\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│   │   │ X │\n└───┴───┴───┘")
