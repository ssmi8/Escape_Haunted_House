# Creator: Steven Smith
import sys
import time

a = 2
b = 0.1
c = 0.08

def intro():
    print("(Everything is dark)")
    time.sleep(a)
    print("You look around to try and figure out where you are")
    time.sleep(a)
    print("You were walking to your car")
    time.sleep(a)
    print("and then everything went black")
    time.sleep(a)
    print("You can feel old, damp carpet around")
    time.sleep(a)
    print("Your eyes slowly adjust")
    time.sleep(a)
    print("You start to make out that your in a strange room")
    print()
    print()
    s = '"Where am I?  Whose room is this?"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    print("A light shines through the window and shines onto the door....")
    time.sleep(a)
    print()
    s = '"Is this my way out?"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(1)
    print()
    print("You walk towards the door...you notice there is no lock")
    time.sleep(a)
    print("You gently push the door open")
    time.sleep(a)
    print("In front you of you are three more doors")
    time.sleep(a)
    print()
    print("Door #1: Looks old and worn.  There are burn marks on it...")
    time.sleep(a)
    print("Door #2: It's an old wooden door with see scratch marks")
    time.sleep(a)
    print("Door #3: The last door looks plain, almost new...strange")
    time.sleep(a)
    print()
    print()
    time.sleep(a)
    firstPath = input("Which door will you choose? (1/2/3):\n")
    if firstPath == '1':
        print()
        path1()
    elif firstPath == '2':
        print()
        path2()
    elif firstPath == '3':
        print()
        path3()


def path1():  # Door 1
    print()

def path1_1():
    print()

def path1_2():
    print()

def path2():
    print()

def path2_1():
    print()

def path2_2():
    print()

def path3():
    print("You push open the door slowly, and come to a corridor")
    print("It's dark and never ending")
    print("You here some feint noises in the distance")
    print("You slowly walk down the corridor")
    print("There is a light in the distance and movement")
    print("Another room is next to you and you rush inside")
    print("Looking around you see an old desk in the corner")
    print("Upon inspection, you see a key on the desk")
    print("You pick it up")
    print()
    print()
    print("'NOOOOOOOOO!!!!!!")
    print("You here a scream coming from the corridor")
    print("They're coming!")
    print()
    print("Path #1")
    print("Path #2")
    print("Path #3")
    print("Path #4")
    print("Path #5")
    print()
    secondPath = input("Which path will you take? (1/2/3/4/5:\n")
    if secondPath == '2':
        path2_2()
    elif secondPath == '3':
        path1_1()
    elif secondPath == '4':
        path1()
    elif secondPath == '5':
        path2()
    else:
        print()
    print("You hide under the desk")
    print("Not making a sound")
    print("Slowly the door to room opens with a creek")
    print("Thud, Thud, Thud")
    print("....They're here")
    print()
    print("Path #1: Stay hidden until they leave")
    print("Path #2: Make a run for it!")
    thirdPath = input("Which path would you like to take? (1/2):\n")
    if thirdPath == '1':
        path3_1()
    elif thirdPath == '2':
        path3_2()


def path3_1():
    print()
    print("You stay under the desk...")
    print("...hoping they'll leave")
    print("There is a sudden pause and then silence....")
    print("You hear heavy breathing")
    print('"HAHAHA I found you little one!')
    print("GAME OVER - Try Again!")
    intro()

def path3_2():
    print()  # Winning path
    print("You realise you have a key, this must be the way out")
    print("Slowly, you lean out and notice the door is open")
    print("It's now or never...")
    print('You whisper "I can do this, I can do this"')
    print("You wait for your moment, they have they're back to you")
    print("In one swift motion you get and up and run for the door")
    print("Down the corridor you see a set of stairs")
    print("Without hesitation you bolt to the bottom")
    print("...")
    print("You look around for freedom")
    print("There's a door behind you")
    print("Escape is near")
    print("But it's locked")
    print("You can hear footsteps getting louder")
    print("They're coming for you")
    print(".....the key!")
    print("You remember you found a key in the other room")
    print("It works!")
    print("They're nearly at the bottom of the stairs")
    print("You only have seconds left")
    print("With one big push, the door flings open")
    print("You run towards the street for help")
    print("A car is passing by")
    print("You stop them and ask for help")
    print("You made it! You're safe now")
    print()
    print("Thanks for playing!!")


print("    #########################")
print("    #                       #")
print("    #  Escape Horror House  #")
print("    #                       #")
print("    #########################")
print()
print()
time.sleep(a)
print("You've had a long day of work")
time.sleep(a)
print()
s = '"I\'m working late again!  I need a promotion"'
for character in s:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(b)
print()
print("Your car is the only one left in the car park")
time.sleep(a)
print("You hear noise behind you")
time.sleep(a)
print()
s = '"Must be the wind or I must be tired"'
for character in s:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(b)
print()
time.sleep(a)
print("You turn and .....")
time.sleep(a)
print("...Everthing turns black")
time.sleep(a)
print()
start_game = input("Would you like to start the game? (Y/N):\n")
if start_game == 'n' or start_game == 'N':
    print("Okay...maybe next time")
elif start_game == 'y' or start_game == 'Y':
    intro()

