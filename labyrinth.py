title = """

██╗      █████╗ ██████╗ ██╗   ██╗██████╗ ██╗███╗   ██╗████████╗██╗  ██╗    
██║     ██╔══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗██║████╗  ██║╚══██╔══╝██║  ██║    
██║     ███████║██████╔╝ ╚████╔╝ ██████╔╝██║██╔██╗ ██║   ██║   ███████║    
██║     ██╔══██║██╔══██╗  ╚██╔╝  ██╔══██╗██║██║╚██╗██║   ██║   ██╔══██║    
███████╗██║  ██║██████╔╝   ██║   ██║  ██║██║██║ ╚████║   ██║   ██║  ██║    
╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝    
                                                                           
 ██████╗ ███████╗    ██████╗ ██╗██████╗ ██████╗ ██╗     ███████╗███████╗   
██╔═══██╗██╔════╝    ██╔══██╗██║██╔══██╗██╔══██╗██║     ██╔════╝██╔════╝   
██║   ██║█████╗      ██████╔╝██║██║  ██║██║  ██║██║     █████╗  ███████╗   
██║   ██║██╔══╝      ██╔══██╗██║██║  ██║██║  ██║██║     ██╔══╝  ╚════██║   
╚██████╔╝██║         ██║  ██║██║██████╔╝██████╔╝███████╗███████╗███████║   
 ╚═════╝ ╚═╝         ╚═╝  ╚═╝╚═╝╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝   

 """

print(title)
print("Greetings adventurer! \n")
print("Welcome to the Labyrinth of Riddles. \n")
print("Only the truly worthy can succeed in completing the Labyrinth. \n")
print("Navigate the maze and answer the riddles correctly to prove yourself worthy. \n")
print("But beware! Many a brave explorer has become lost and mad within its walls. \n")

play_game = True

def begin_labyrinth():
    print("Its started")

while play_game:
    start = input("Do you wish to enter the Labyrinth of Riddles? (yes/no) \n").lower().strip()
    if start == "yes" or start == "y":
        print("Let it begin! \n")
        begin_labyrinth()
        break
    elif start == "no" or start == "n":
        quit()
    else:
        print("Invalid input. Please try again. \n")

