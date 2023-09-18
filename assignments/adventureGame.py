# kieranthakkar, tanu
# ADVENTURE GAME - a complete text game
# the program will let users move through rooms based on user input and get descriptions of each room. To create this, you’ll need to establish the direction in which the user can move, a way to track how far the user has moved (and therefore which room he/she is in), and to print out a description.
# You’ll also need to set limits for how far the user can move. In other words, create “walls” around the rooms that tell the user, “You can’t move further in this direction.”


# Importing the 'os' module to use the 'cls' command and clear the terminal
import os, random
os.system('cls')

# Map generation
map = {"-1,1": "┌───┬MAP┬───┐\n│ X │   │   │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
  "0,1": "┌───┬MAP┬───┐\n│   │ X │   │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
  "1,1": "┌───┬MAP┬───┐\n│   │   │ X │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
 "-1,0": "┌───┬MAP┬───┐\n│   │   │   │\n├───┼───┼───┤\n│ X │   │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
  "0,0": "┌───┬MAP┬───┐\n│   │   │   │\n├───┼───┼───┤\n│   │ X │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
  "1,0": "┌───┬MAP┬───┐\n│   │   │   │\n├───┼───┼───┤\n│   │   │ X │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
"-1,-1": "┌───┬MAP┬───┐\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│ X │   │   │\n└───┴───┴───┘",
 "0,-1": "┌───┬MAP┬───┐\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│   │ X │   │\n└───┴───┴───┘",
 "1,-1": "┌───┬MAP┬───┐\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│   │   │ X │\n└───┴───┴───┘"}

# Random name/office selection
names = ["Michael Scott", "Jim", "Pam", "Dwight", "Creed", "Kevin", "Toby", "Meredith"]
offices = ["-1,-1", "0,0", "1,-1", "-1,0", "1,1", "0,1", "-1,1", "1,0"]
random_index = random.randint(0,7)
random_name = names[random_index]
deliveryCoord = offices[random_index]

# Starting position
xPos, yPos = 0,-1
wasOn = False
stringCoord = str(xPos)+","+str(yPos)
print(f"You have entered The Office. Find {random_name} to deliver their pizza.")

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
            os.system('cls')
            print(wallError)
            if wasOn is True:
                wasOn = False
            continue
        else:
            xPos -= 1
    elif request == "right":
        if xPos == 1:
            os.system('cls')
            print(wallError)
            if wasOn is True:
                wasOn = False
            continue
        else:
            xPos += 1
    elif request == "up":
        if yPos == 1:
            os.system('cls')
            print(wallError)
            if wasOn is True:
                wasOn = False
            continue
        else:
            yPos += 1
    elif request == "down":
        if yPos == -1:
            os.system('cls')
            print(wallError)
            if wasOn is True:
                wasOn = False
            continue
        else:
            yPos -= 1
    stringCoord = str(xPos)+","+str(yPos)
    os.system('cls')
