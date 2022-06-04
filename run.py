# Creator: Steven Smith

def intro():
    print("(Everything is dark)")
    print("You look around to try and figure out where you are")
    print("The last thing you rememeber was walking to your car and then everything went black")
    print("You can feel old, damp carpet around")
    print("Your eyes slowly adjust, and you start to make out that your in a strange room")
    print()
    print('"Where am I?  Whose room is this?"')
    print()
    print('A light shines through a crack in the window and shines onto the door...."Is this my way out?"')
    print("You walk towards the door...you notice there is no lock")
    print("You gently push the door open")
    print("In front you of you are three more doors")
    print()
    print("Door #1: Looks old and worn.  There are burn marks on it...")
    print("Door #2: It's a wooden door. You look closely and can see scratch marks on the door")
    print("Has someone been here before?")
    print("Door #3: The last door looks plain, almost new...strange")
    print()
    print()
    firstPath = input("Which door will you choose? (1/2/3)")



print()
print("    #########################")
print("    #                       #")
print("    #  Escape Horror House  #")
print("    #                       #")
print("    #########################")
print()
print()

start_game = input("Would you like to start the game? (Y/N):\n")
if start_game == 'n' or start_game == 'N':
    print("Okay...maybe next time")
elif start_game == 'y' or start_game == 'Y':
    intro()

