# kieranthakkar, tanu
# ADVENTURE GAME - a complete text game
# the program will let users move through rooms based on user input and get descriptions of each room. To create this, you’ll need to establish the direction in which the user can move, a way to track how far the user has moved (and therefore which room he/she is in), and to print out a description.
# You’ll also need to set limits for how far the user can move. In other words, create “walls” around the rooms that tell the user, “You can’t move further in this direction.”


# Importing the 'os' module to use the 'cls' command and clear the terminal
import os
os.system('cls')

# Map generation
map = {"-1,1": "┌───┬───┬───┐\n│ X │   │   │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
  "0,1": "┌───┬───┬───┐\n│   │ X │   │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
  "1,1": "┌───┬───┬───┐\n│   │   │ X │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
 "-1,0": "┌───┬───┬───┐\n│   │   │   │\n├───┼───┼───┤\n│ X │   │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
  "0,0": "┌───┬───┬───┐\n│   │   │   │\n├───┼───┼───┤\n│   │ X │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
  "1,0": "┌───┬───┬───┐\n│   │   │   │\n├───┼───┼───┤\n│   │   │ X │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
"-1,-1": "┌───┬───┬───┐\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│ X │   │   │\n└───┴───┴───┘",
 "0,-1": "┌───┬───┬───┐\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│   │ X │   │\n└───┴───┴───┘",
 "1,-1": "┌───┬───┬───┐\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│   │   │ X │\n└───┴───┴───┘"}

# Random name
names = ["Michael Scott", "Jim Halpert", "Pam Beesly", "Dwight Schrute", "Creed", "Kevin Malone", "Toby", "Meredith"]
offices = []
random_index = random.randint(0,7)
random_name = names[random_index]
delivery = offices[random_index]

# Starting position
xPos, yPos = 0,-1

# The game - while loop to continuously take input
while True:
    request = input("Request: ").lower()
    
    if request == "end" or request == "quit" or request == "exit":
        print("Failed to deliver pizza. Game over.")
        break

    if request == "deliver" and stringCoord == deliveryCoord:
        print(f"{random_name} thanks you for the pizza.\nGame over.")
        break

    # Movement with limits, movement works along a Cartesian coordinate system
    if request == "left":
        if xPos == -1:
            print("You can't move further in this direction.")
            continue
        else:
            xPos -= 1
    elif request == "right":
        if xPos == 1:
            print("You can't move further in this direction.")
            continue
        else:
            xPos += 1
    elif request == "up":
        if yPos == 1:
            print("You can't move further in this direction.")
            continue
        else:
            yPos += 1
    elif request == "down":
        if yPos == -1:
            print("You can't move further in this direction.")
            continue
        else:
            yPos -= 1

    os.system('cls')
    print(f"{xPos},{yPos}")
    
