# Creator: Steven Smith

def intro():
    print('Introduction to the story line')

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

