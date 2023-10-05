# kieranthakkar, Tanu, Mohamed Idris, Haley Visconti
"""
ADVENTURE GAME - a complete time-trials text game.
PLAY IN TERMINAL
Users are timed as they move through rooms w/ input.
A map is displayed with live tracking and descriptions of each room

5/10/23 - This version of the game will no longer be updated. To see any further developments please see the repo 'theOfficeGame.'
"""


# 'os' module for 'cls' command to clear the terminal
# 'random' module used to find where pizza is delivered
# 'time' module needed for perf_counter() - used to time deliveries
import os, random, time
os.system('cls')

startTime = time.perf_counter()

# Map generation
map = {"-1,1": "┌───┬MAP┬───┐\tHUMAN RESOURCES\n│ X │   │   │\n├───┼───┼───┤\tHere you find Toby.\n│   │   │   │\t\n├───┼───┼───┤\tTo the right a man waves, he drools and points at the pizza.\n│   │   │   │\tBehind is the conference room.\n└───┴───┴───┘\t",
  "0,1": "┌───┬MAP┬───┐\tKEVIN'S DESK\n│   │ X │   │\n├───┼───┼───┤\tKevin drools whilst staring at the pizza.\n│   │   │   │\t\n├───┼───┼───┤\n│   │   │   │\tOn the right is a suspicious elderly man. To the left you see HR.\n└───┴───┴───┘\t",
  "1,1": "┌───┬MAP┬───┐\tCREED'S DESK\n│   │   │ X │\n├───┼───┼───┤\tNo one knows what he does here.\n│   │   │   │\t\n├───┼───┼───┤\n│   │   │   │\tTo the left a man waves, he drools and points at the pizza. \n└───┴───┴───┘\tBehind a lady plays solitaire.",
 "-1,0": "┌───┬MAP┬───┐\tTHE CONFERENCE ROOM\n│   │   │   │\n├───┼───┼───┤\tDwight is here. He refuses to speak, but he's smiling?.\n│ X │   │   │\n├───┼───┼───┤\n│   │   │   │\n└───┴───┴───┘",
  "0,0": "┌───┬MAP┬───┐\tJIM AND DWIGHTS'S DESKS\n│   │   │   │\n├───┼───┼───┤\tJim is on the phone trying to close a sale. Dwight is not here\n│   │ X │   │\tbut Jim points to the conference room.\n├───┼───┼───┤\n│   │   │   │\tThe conference room is on the left. To your right a lady plays solitaire.\n└───┴───┴───┘\tIn front a man waves - he points at the pizza.",
  "1,0": "┌───┬MAP┬───┐\tMEREDITH'S DESK\n│   │   │   │\n├───┼───┼───┤\tHere Meredith plays Microsoft Solitaire whilst attempting to\n│   │   │ X │\thide a bottle of rum.\n├───┼───┼───┤\n│   │   │   │\tTo your left is a lively sales rep. Up ahead there's a suspicious \n└───┴───┴───┘\telderly man. Behind/down is the reception.",
"-1,-1": "┌───┬MAP┬───┐\tMICHAEL SCOTT'S OFFICE\n│   │   │   │\n├───┼───┼───┤\tA rather basic office for the Regional Manager.\n│   │   │   │\tHe keeps shouting \"That's what she said!\"\n├───┼───┼───┤\n│ X │   │   │\tAdjacent is the conference room and lobby.\n└───┴───┴───┘",
 "0,-1": "┌───┬MAP┬───┐\tLOBBY AREA\n│   │   │   │\n├───┼───┼───┤\tTo your right is a receptionist, to your left is the Regional Manager's office.\n│   │   │   │\tIn front of you are office employees.\n├───┼───┼───┤\n│   │ X │   │\tBehind you, the door is closed. You must deliver the pizza to leave.\n└───┴───┴───┘",
 "1,-1": "┌───┬MAP┬───┐\tTHE RECEPTION - PAM\n│   │   │   │\n├───┼───┼───┤\tHere you find Pam, the Receptionist.\n│   │   │   │\tShe is on the phone and offers no help.\n├───┼───┼───┤\n│   │   │ X │\tUp ahead you see a woman playing solitaire on the computer.\n└───┴───┴───┘"}

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
    print(f"\nTarget = {random_name}\t\tMove with (up), (down), (left), (right).\n")

    # Delivery prompt
    if stringCoord == deliveryCoord:
        print(f"\033[32m-! (deliver) pizza to {random_name} !-\033[0m")

    # Run away outcome
    if wasOn is True:
        print(f"{random_name} says come back here!")
        wasOn = False

    action = input("\nAction: ").lower()
    
    if action == "end" or action == "quit" or action == "exit":
        print("\033[91mFailed to deliver pizza. Game over.\033[0m\n")
        break
    
    # Route for delivery and game completion
    if stringCoord == deliveryCoord:
        if action == "deliver":
            os.system('cls')
            print(f"{random_name} thanks you for the pizza.")
            endTime = time.perf_counter()
            timer = endTime-startTime
            print(f"Game over. That took {timer} second(s) to complete.\n")
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
    
    # Update coordinates after movement and reset the terminal.
    stringCoord = str(xPos)+","+str(yPos)
    os.system('cls')