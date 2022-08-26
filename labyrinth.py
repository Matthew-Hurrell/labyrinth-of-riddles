from riddles import riddle

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
print("Navigate the maze and answer the riddles correctly to prove yourself")
print("worthy \n")
print("But beware! Many a brave explorer has become lost and mad within its")
print("walls. \n")

play_game = True

def you_die():
    final_words = """
"Your three guesses are up." 

The Ridder raises his hand.

"BE GONE!"

There is a bright flash and everything fades to black

GAME OVER.
    """
    print(final_words)
    quit()

def first_riddle():
    riddle_one = riddle[0]["riddle_one"]
    riddle_one_answer = riddle[0]["correct"]
    print(riddle_one_answer)
    path_one = f"""
--------------------------------------------------------------

You walk forwards into the path leading straight into the labyrinth.

Suddenly a dark shadowy figure appears before you.

The figure's face is obscured by a dark black cloak.

The figure speaks in a quiet raspy voice: "I am the one they call... The Ridder."

"If you cannot guess my riddle in three, you die."

The figure points at you.

"Riddle me this."

"{riddle_one}"
    
    """
    print(path_one)
    guesses = 3
    while play_game:
        choice = input(" \n").lower().strip()
        if choice == riddle_one_answer:
            print("Correct")
            break
        else:
            print("Incorrect")
            guesses -= 1
            if guesses == 0:
                you_die()
                break

        
def begin_labyrinth():
    first_paragraph = """
--------------------------------------------------------------

You find yourself facing the doorway to the beginning of the Labyrinth.

There is not a single sound to be heard. Only the faint crackle of the torches 
that light the dim walkways.

You feel the gravel crunch beneath your feet as you take a breath 
and enter the labyrinth.

The walls are thick stone bricks which extend up far beyond reach.
The stones are old and sticky to the touch. 

Before you are two paths. One path continues straight and the other follows 
the outer ring of the labyrinth to the left.

"""
    
    print(first_paragraph)
    while play_game:
        choice = input("Which path will you choose? (forward/left) \n").lower().strip()
        if choice == "forward" or choice == "f":
            first_riddle()
            break
        elif choice == "left" or choice == "l":
            left = """
--------------------------------------------------------------

You follow the left path along the outer edge of the labyrinth.

You turn right at the end of the path and right again as it curves around
onto itself.

You have reached a dead end. 
            """
            print(left)
            while play_game:
                dead_end_choice = input("Do you want to return back \
or do you want to exit the labyrinth (back/exit) \n").lower().strip()
                if dead_end_choice == "back" or dead_end_choice == "b":
                    print("You retrace your steps back to where you were. \n")
                    break
                elif dead_end_choice == "exit" or dead_end_choice == "e":
                    quit()
                else:
                    print("Invalid input. Please try again. \n")
        else:
            print("Invalid input. Please try again. \n")

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

