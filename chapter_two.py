import sys
from time import sleep
from riddles import riddle

play_game = True

def second_riddle():
    print("Second Riddle.")

def second_chapter():
    second_paragraph = """
--------------------------------------------------------------

"You guessed correctly... I'm impressed. It's been a thousand years since
someone solved one of my riddles. Maybe you will finally be a worthy 
opponent?"    

"But don't get cocky. I always save my hardest riddles for last!"

"I'll see you soon... if you survive."

There's a blinding flash of light. You shade your eyes and the Riddler
vanishes from sight.
"""
    print(second_paragraph)
    path_two = """Infront of you there are two pathways.

One path goes left, and the other goes right.

The ends of both paths are obscured from view.

There is a small carving in the stone wall infront of you.

You lean in to have a closer look.

It reads "Whatever you do, don't go left."
"""
    print(path_two)
    while play_game:
        choice = input("Which path will you choose? (left/right) \n").lower().strip()
        if choice == "right" or choice == "r":
            second_riddle()
            break
        elif choice == "left" or choice == "l":
            left = """
--------------------------------------------------------------

Against your better judgement you decide to ignore the words of warning
and go left anyway.

You follow the pathway forwards and then around to the left. 

You begin to notice small holes in the ceiling and walls as you continue to 
walk forwards.

As you walk further into the passageway, you hear an audible click as one 
of your feet touches a panel on the floor.

"Ah crap, why did I go left?!"

Before you have time to react, you hear the whip of hundreds of arrows
as they are released from the holes in the walls and ceiling and whizz towards
your body.

It all goes black.

GAME OVER.
            """
            print(left)
            while play_game:
                start = input("Do you wish to play again? (yes/no) \n").lower().strip()
                if start == "yes" or start == "y":
                    print("\nLet it begin! \n")
                    begin_labyrinth()
                    break
                elif start == "no" or start == "n":
                    quit()
                else:
                    print("Invalid input. Please try again. \n")
        else:
            print("Invalid input. Please try again. \n")
