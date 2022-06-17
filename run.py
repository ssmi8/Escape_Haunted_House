# Creator: Steven Smith
# 18.06.22
# Escape Horror House

import sys
import time

a = 2
b = 0.1
c = 0.08


def intro():
    print()
    time.sleep(a)
    print("To quit the game, press Q at any input section...")
    print()
    print()
    print()
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
    print("Door #2: It's an old wooden door with scratch marks")
    time.sleep(a)
    print("Door #3: The last door looks plain, almost new...strange")
    time.sleep(a)
    print()
    print()
    time.sleep(a)
    print("Which door will you choose? (1/2/3):")

    c1 = input()
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if c1 == "1":
            print()
            ans = 'correct'
            path1()
        elif c1 == "2":
            print()
            ans = 'correct'
            path2()
        elif c1 == "3":
            print()
            ans = 'correct'
            path3()
        elif c1 == "q" or c1 == "Q":
            print("Thanks for playing!")
            ans = 'correct'
        else:
            print("Invalid entry: please select 1,2 or 3")
            c1 = input()


def path1():  # Door 1
    print("You push the door open and come to another strange room")
    time.sleep(a)
    print("This feels a lot colder than the previous room")
    time.sleep(a)
    print("You notice an old bed in the corner of the room")
    time.sleep(a)
    print("Gently and without a sound, you walk towards the bed")
    time.sleep(a)
    print("There's scraps of paper, crumpled on top")
    time.sleep(a)
    print("You pick one and it reads...")
    time.sleep(a)
    print()
    s = '"Today is the day I escape."'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    print("You put the note in your pocket, and carry on.")
    time.sleep(a)
    print()
    time.sleep(a)
    print("There's small gap in the wall, big enough to squeeze through")
    time.sleep(a)
    print()
    print("Do you squeeze through the gap? (Y/N):")

    c1 = input()
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if c1 == "y" or c1 == "Y":
            ans = 'correct'
            path1_1()
        elif c1 == "n" or c1 == "N":
            ans = 'correct'
            path1_2()
        elif c1 == "q" or c1 == "Q":
            ans = 'correct'
            print("Thanks for playing!")
        else:
            print("Invalid entry: please select Y or N")
            c1 = input()    


def path1_1():  # player loses game
    print("You squeeze through the gap in the wall")
    time.sleep(a)
    print("It looks like this is a hidden room")
    time.sleep(a)
    print("There's a door in front of you")
    time.sleep(a)
    print("You hurry towards the door")
    time.sleep(a)
    print("As you get to the door you hear something feint behind you")
    time.sleep(a)
    print()
    s = '"H-Help M-Me!"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    print("In a flash you turn to see someone in the corner of the room")
    time.sleep(a)
    print("It's the girl who wrote the note...what is she doing in here?")
    time.sleep(a)
    print("You walk over to her, and you can see she's tied up")
    time.sleep(a)
    print()
    s = "\"Don't you worry, I'll get you out of here\""
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    print("You frantically search around for something to break the chains")
    time.sleep(a)
    print("Something catches your eye")
    time.sleep(a)
    print("There's movement outside the room")
    time.sleep(a)
    print("The sound footsteps haunt your soul")
    time.sleep(a)
    print("The door slams open")
    time.sleep(a)
    print()
    s = '"Well, well, well, tried to escape did you.  I don\'t think so!"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    print("GAME OVER")
    time.sleep(a)
    print("Do you want to play again? (Y/N):")

    c1 = input()
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if c1 == "y" or c1 == "Y":
            ans = 'correct'
            intro()
        elif c1 == "n" or c1 == "N":
            print("Thank you for playing!")
            ans = 'correct'
        else:
            print("Invalid entry: please select Y or N")
            c1 = input()


def path1_2():  # player loses game
    print("You avoid squeezing through the gap")
    time.sleep(a)
    print("Scanning the rest of the room you try to find a way out")
    time.sleep(a)
    print("There's another door, which is locked")
    time.sleep(a)
    print()
    s = '"I need to get through that door, it must be my way out"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(a)
    print()
    print("You search around for something to help unlock the door")
    time.sleep(a)
    print("You notice a box on a table")
    time.sleep(a)
    print()
    s = '"There must be something in here I can use"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(a)
    print("It's nothing but old pictures of a young boy and his mother")
    time.sleep(a)
    print("There's something at the bottom of the box...it's an old teddy")
    time.sleep(a)
    print("You hear a groin coming through the small gap in the wall")
    time.sleep(a)
    print("In your panic you knock the box on the floor")
    time.sleep(a)
    print("The sound echoes around the the room")
    time.sleep(a)
    print("There is silence, then you here keys opening the door")
    time.sleep(a)
    print()
    s = '"So this is where you\'ve been hiding.  Well I have you now!"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(a)
    print()
    time.sleep(a)
    print("GAME OVER")
    time.sleep(a)
    print("Do you want to play again? (Y/N):")

    c1 = input()
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if c1 == "y" or c1 == "Y":
            ans = 'correct'
            intro()
        elif c1 == "n" or c1 == "N":
            print("Thank you for playing!")
            ans = 'correct'
        else:
            print("Invalid entry: please select Y or N")
            c1 = input()


def path2():  # Door 2
    print("You gingerly walk over to the door")
    time.sleep(a)
    print("The door is heavy to push open")
    time.sleep(a)
    print("The door closes behind")
    time.sleep(a)
    print("It's dark and you scramble to find some light")
    time.sleep(a)
    print("Feeling the wall with your hands you hit a switch")
    time.sleep(a)
    print("A few flashes of light and the lights are on")
    time.sleep(a)
    print("Your eyes slowly adjust")
    time.sleep(a)
    print("The room looks like a surgical room")
    time.sleep(a)
    print("You notice a steel door in the far corner")
    time.sleep(a)
    print("There's a key code next to the door")
    time.sleep(a)
    print()
    s = '"A key code?  What could the code be?"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(a)
    print()
    print("You search around the room for key")
    time.sleep(a)
    print("There's a computer!")
    time.sleep(a)
    print("You run to the computer")
    time.sleep(a)
    print("There's a notepad on the desk")
    time.sleep(a)
    print("There are two codes written down. Which one is it?")
    print()
    print("Do you choose code 1 or code 2? (1/2):")

    c1 = input()
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if c1 == "1":
            ans = 'correct'
            path2_1()
        elif c1 == "2":
            ans = 'correct'
            path2_2()
        elif c1 == "q" or c1 == "Q":
            print("Thanks for playing!")
            ans = 'correct'
        else:
            print("Invalid entry: please select 1 or 2")
            c1 = input()


def path2_1():  # player loses game
    print()
    print("Code 1")
    time.sleep(a)
    print()
    s = '"This has to be the right one"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(a)
    print()
    print("You rush back over to the keypad")
    time.sleep(a)
    print("You enter the code")
    time.sleep(a)
    print("An alarm rings a deafening sound around the room")
    time.sleep(a)
    print("There's no way to stop it")
    time.sleep(a)
    print("He's coming for you")
    time.sleep(a)
    print("The door swings open and you're caught")
    print()
    print("GAME OVER")
    print()
    time.sleep(a)
    print("Do you want to play again? (Y/N):")

    c1 = input()
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if c1 == "y" or c1 == "Y":
            ans = 'correct'
            intro()
        elif c1 == "n" or c1 == "N":
            print("Thank you for playing!")
            ans = 'correct'
        else:
            print("Invalid entry: please select Y or N")
            c1 = input()


def path2_2():  # player loses game
    print()
    print("Code 2")
    time.sleep(a)
    print()
    s = '"This has to be the right one"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(a)
    print()
    print("You rush back over to the keypad")
    time.sleep(a)
    print("You enter the code")
    time.sleep(a)
    print("Nothing...")
    time.sleep(a)
    print()
    print("Still nothing...")
    time.sleep(a)
    print("You hear a noise coming from behind you")
    time.sleep(a)
    print("You hurrily enter the code again")
    time.sleep(a)
    print()
    s = '"You can\'t escape me now little one!"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(a)
    print()
    time.sleep(a)
    print()
    print("He has you!")
    print()
    print("GAME OVER")
    print()
    time.sleep(a)
    print("Do you want to play again? (Y/N):")

    c1 = input()
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if c1 == "y" or c1 == "Y":
            ans = 'correct'
            intro()
        elif c1 == "n" or c1 == "N":
            print("Thank you for playing!")
            ans = 'correct'
        else:
            print("Invalid entry: please select Y or N")
            c1 = input()


def path3():  # Door 3
    print("You push open the door slowly, and come to a corridor")
    time.sleep(a)
    print("It's dark and never ending")
    time.sleep(a)
    print("You here some feint noises in the distance")
    time.sleep(a)
    print("You slowly walk down the corridor")
    time.sleep(a)
    print("There is a light in the distance and movement")
    time.sleep(a)
    print("Another room is next to you and you rush inside")
    time.sleep(a)
    print("Looking around you see an old desk in the corner")
    time.sleep(a)
    print("Upon inspection, you see a key on the desk")
    time.sleep(a)
    print("You pick it up")
    time.sleep(a)
    print()
    print()
    time.sleep(a)
    print()
    s = '"NOOOOOOOOO!"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(a)
    print("You here a scream coming from the corridor")
    time.sleep(a)
    print("They're coming!")
    time.sleep(a)
    print()
    time.sleep(a)
    print("You can hide under the desk and wait for you chance to escape")
    time.sleep(a)
    print("You hide under the desk")
    time.sleep(a)
    print("Not making a sound")
    time.sleep(a)
    print("Slowly the door to room opens with a creek")
    time.sleep(a)
    print("Thud, Thud, Thud")
    time.sleep(a)
    print("....They're here")  #
    time.sleep(a)
    print()
    time.sleep(a)
    print("Option #1: Stay hidden until they leave")
    time.sleep(a)
    print("option #2: Make a run for it!")
    time.sleep(a)
    print("Which path would you like to take? (1/2):")

    c1 = input()
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if c1 == "1":
            ans = 'correct'
            path3_1()
        elif c1 == "2":
            ans = 'correct'
            path3_2()
        elif c1 == "q" or c1 == "Q":
            print("Thanks for playing!")
            ans = 'correct'
        else:
            print("Invalid entry: please select 1 or 2")
            c1 = input()


def path3_1():
    print()
    print("You stay under the desk...")
    time.sleep(a)
    print("...hoping they'll leave")
    time.sleep(a)
    print("There is a sudden pause and then silence....")
    time.sleep(a)
    print("You hear heavy breathing")
    time.sleep(a)
    print('"HAHAHA I found you little one!')
    time.sleep(a)
    print()
    print()
    print("GAME OVER - Try Again!")
    time.sleep(a)
    print()
    print()
    print("Do you want to play again? (Y/N):")

    c1 = input()
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if c1 == "y" or c1 == "Y":
            ans = 'correct'
            intro()
        elif c1 == "n" or c1 == "N":
            print("Thank you for playing!")
            ans = 'correct'
        else:
            print("Invalid entry: please select Y or N")
            c1 = input()


def path3_2():
    print()  # Winning path
    print("You realise you have a key, this must be the way out")
    time.sleep(a)
    print("Slowly, you lean out and notice the door is open")
    time.sleep(a)
    print("It's now or never...")
    time.sleep(a)
    print('You whisper "I can do this, I can do this"')
    time.sleep(a)
    print("You wait for your moment, they have they're back to you")
    time.sleep(a)
    print("In one swift motion you get and up and run for the door")
    time.sleep(a)
    print("Down the corridor you see a set of stairs")
    time.sleep(a)
    print("Without hesitation you bolt to the bottom")
    time.sleep(a)
    print("...")
    time.sleep(a)
    print("You look around for freedom")
    time.sleep(a)
    print("There's a door behind you")
    time.sleep(a)
    print("Escape is near")
    time.sleep(a)
    print("But it's locked")
    time.sleep(a)
    print("You can hear footsteps getting louder")
    time.sleep(a)
    print("They're coming for you")
    time.sleep(a)
    print(".....the key!")
    time.sleep(a)
    print("You remember you found a key in the other room")
    time.sleep(a)
    print("It works!")
    time.sleep(a)
    print("They're nearly at the bottom of the stairs")
    time.sleep(a)
    print("You only have seconds left")
    time.sleep(a)
    print("With one big push, the door flings open")
    time.sleep(a)
    print("You run towards the street for help")
    time.sleep(a)
    print("A car is passing by")
    time.sleep(a)
    print("You stop them and ask for help")
    time.sleep(a)
    print("You made it! You're safe now")
    time.sleep(a)
    print()
    time.sleep(a)
    print("CONGRATULATIONS!  YOU WON!!")
    time.sleep(a)
    print("You successfully escaoed Horror House!")
    time.sleep(a)
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
print("Would you like to start the game? (Y/N)")

c1 = input()
ans = 'incorrect'
while(ans == 'incorrect'):
    if c1 == "n" or c1 == "N":
        print("Okay...maybe next time")
        ans = 'correct'
    elif c1 == "y" or c1 == "Y":
        ans = 'correct'
        intro()
    else:
        print("Invalid entry: please select Y or N")
        c1 = input()
    
