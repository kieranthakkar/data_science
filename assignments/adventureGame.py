# kieranthakkar, tanu
# ADVENTURE GAME - a complete time-trials text game
# the program will let users move through rooms based on user input and get descriptions of each room. To create this, you’ll need to establish the direction in which the user can move, a way to track how far the user has moved (and therefore which room he/she is in), and to print out a description.
# You’ll also need to set limits for how far the user can move. In other words, create “walls” around the rooms that tell the user, “You can’t move further in this direction.”


# Importing the 'os' module to use the 'cls' command and clear the terminal
import os, random, time
os.system('cls')

startTime = time.perf_counter()

# Map generation
map = {"-1,1": "┌───┬MAP┬───┐\n│ X │   │   │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
  "0,1": "┌───┬MAP┬───┐\n│   │ X │   │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
  "1,1": "┌───┬MAP┬───┐\n│   │   │ X │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
 "-1,0": "┌───┬MAP┬───┐\n│   │   │   │\n├───┼───┼───┤\n│ X │   │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
  "0,0": "┌───┬MAP┬───┐\n│   │   │   │\n├───┼───┼───┤\n│   │ X │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
  "1,0": "┌───┬MAP┬───┐\n│   │   │   │\n├───┼───┼───┤\n│   │   │ X │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
"-1,-1": "┌───┬MAP┬───┐\n│   │   │   │\n├───┼───┼───┤\n│   │   │   │\n├───┼───┼───┤\n│ X │   │   │\n└───┴───┴───┘",
 "0,-1": "┌───┬MAP┬───┐\tLOBBY AREA\n│   │   │   │\n├───┼───┼───┤\tTo your right is a receptionist, to your left is the Regional Manager's office.\n│   │   │   │\tIn front of you are office employees.\n├───┼───┼───┤\n│   │ X │   │\tBehind you, the door is closed. You will need to deliver the pizza to leave.\n└───┴───┴───┘",
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

# Opening banner
opener = f"You have entered The Office. Find \033[1m{random_name}\033[0m and deliver their pizza"
print("-"*(len(opener)-6)+"\n"+f" {opener}"+"\n"+"-"*(len(opener)-6))

# The game - while loop to continuously take input
while True:
    # Constantly show map w/ instructions
    print(map[stringCoord])
    print(f"Target = {random_name}\nMove with (up), (down), (left), (right).\n")

    # Delivery prompt
    if stringCoord == deliveryCoord:
        print(f"(deliver) pizza to {random_name}")

    # Run away outcome
    if wasOn is True:
        print(f"{random_name} says come back here!")
        wasOn = False

    action = input("Action: ").lower()
    
    if action == "end" or action == "quit" or action == "exit":
        print("Failed to deliver pizza. Game over.")
        break
    
    if stringCoord == deliveryCoord:
        if action == "deliver":
            os.system('cls')
            print(f"{random_name} thanks you for the pizza.")
            endTime = time.perf_counter()
            timer = endTime-startTime
            print(f"Game over. That took {timer} second(s) to complete.\n\n")
            break
        elif action in ["up","down","left","right"]:
            wasOn = True

    # Movement with limits, movement works along a Cartesian coordinate system
    wallError = "\033[91mYou can't move further in this direction.\033[0m"
    if action == "left":
        if xPos == -1:
            os.system('cls')
            print(wallError)
            wasOn = False
            continue
        else:
            xPos -= 1
    elif action == "right":
        if xPos == 1:
            os.system('cls')
            print(wallError)
            wasOn = False
            continue
        else:
            xPos += 1
    elif action == "up":
        if yPos == 1:
            os.system('cls')
            print(wallError)
            wasOn = False
            continue
        else:
            yPos += 1
    elif action == "down":
        if yPos == -1:
            os.system('cls')
            print(wallError)
            wasOn = False
            continue
        else:
            yPos -= 1
    stringCoord = str(xPos)+","+str(yPos)
    os.system('cls')