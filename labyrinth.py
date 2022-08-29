import sys
from time import sleep
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
intro_paragraph = """
Greetings adventurer!

Welcome to the Labyrinth of Riddles.

Only the truly worthy can succeed in completing the Labyrinth.

Navigate the maze and answer the riddles correctly to prove yourself
worthy.

But beware! Many brave explorers who venture into the labyrinth never return.
"""
print(intro_paragraph)

play_game = True

def sixth_chapter():
    print("sixth chapter")

def fifth_riddle():
    riddle_five = riddle[4]["riddle"]
    riddle_five_answer = riddle[4]["correct"]
    path_five = """
--------------------------------------------------------------

You walk up to the left door and open it slowly.

You peak around the edge of the door and see a pathway that
turns right.

All seems to be normal. 

You walk through the doorway and close the door behind you.

You follow the path and turn right into a narrow passage. 

You are hit with another flash of bright light.

The Riddler appears in the path infront of you.

"You may have been lucky solving my door riddle, but this time
I'm not playing around. Let's really see what you're made of."

The Riddler points at you.

"Riddle me this."
    """
    print(path_five)
    for char in riddle_five:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    guesses = 3
    while play_game:
        print(f"\nYou have {guesses} guesses left. \n")
        choice = input("What is your guess? \n").lower().strip()
        if choice == riddle_five_answer or choice == "the moon":
            sixth_chapter()
            break
        else:
            print('\n"You guessed incorrectly. Try again"')
            guesses -= 1
            if guesses == 0:
                you_die()
                break


def fifth_chapter():
    fifth_paragraph = """
--------------------------------------------------------------

"Correct again!"    

"You truly possess a formidable intellect. I will give you that."

"But you have not beaten me yet!"

"You are almost at the end of my labyrinth.. But the hardest part is yet 
to come."

"Until next time adventurer."

The Riddler vanishes again in another flash of light.
"""
    print(fifth_paragraph)
    path_five = """You look ahead and continue following the pathway
in front of you.

You are tired but push yourself forwards as you know you are close to the 
end of the labyrinth.

"It can't be much further." You tell yourself.

You follow the passageway around to the right and then right again as
the path turns around on itself.

You then take a left and find youself at another fork in the road.

There are two paths ahead. Left and right.

The left path descends downwards steeply and turns a corner.

The right path opens out what looks like a larger area beyond.
"""
    print(path_five)
    while play_game:
        choice = input("Which path will you choose? (left/right) \n").lower().strip()
        if choice == "right" or choice == "r":
            fifth_riddle()
            break
        elif choice == "left" or choice == "l":
            left = """
--------------------------------------------------------------

You choose the left path and begin your slow descent down the passageway.

You turn the corner and see that the passage continues down sharply.

You are unable to see the bottom.

Behind you you see a wall that looks slightly different from the other walls.

The bricks are noticeably smaller than the normal bricks used for walls.

You have a bad feeling, but you shrug it off and continue your descent.

As you move down into the dark you hear a loud noise from the top of 
the passage. 

The strange wall at the peak of the pathway cracks and then splits open.

The bricks crumble as a huge round boulder breaks through the wall and 
rolls down the slope towards you, gaining momentum as it continues.

You try to run but there is no escape.

You close your eyes and cover your head as the boulder comes crashing
down.

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

def fourth_riddle():
    riddle_four = riddle[3]["riddle"]
    riddle_four_answer = riddle[3]["correct"]
    path_four = """
--------------------------------------------------------------

You walk up to the left door and open it slowly.

You peak around the edge of the door and see a pathway that
turns right.

All seems to be normal. 

You walk through the doorway and close the door behind you.

You follow the path and turn right into a narrow passage. 

You are hit with another flash of bright light.

The Riddler appears in the path infront of you.

"You may have been lucky solving my door riddle, but this time
I'm not playing around. Let's really see what you're made of."

The Riddler points at you.

"Riddle me this."
    """
    print(path_four)
    for char in riddle_four:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    guesses = 3
    while play_game:
        print(f"\nYou have {guesses} guesses left. \n")
        choice = input("What is your guess? \n").lower().strip()
        if choice == riddle_four_answer or choice == "the moon":
            fifth_chapter()
            break
        else:
            print('\n"You guessed incorrectly. Try again"')
            guesses -= 1
            if guesses == 0:
                you_die()
                break

def right_door():
    right_door_choice = """
--------------------------------------------------------------

You walk up to the right door and open it slowly.

You peak around the door and see a pathway that continues and turns left
around a corner.

You breathe a sigh of relief and pass through the door, closing it
behind you.

You follow the path around to the left and see some words written on the 
wall infront of you.

"WRONG DOOR"

There is a blinding flash of light and it all goes dark.

GAME OVER.
"""
    print(right_door_choice)
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

def fourth_chapter():
    fourth_paragraph = """
--------------------------------------------------------------

"You've bested me again adventurer."    

"From now on I'm not going to be so easy on you."

"Until next time...."

The Riddler vanishes again in another flash of light.
"""
    print(fourth_paragraph)
    path_four = """You finish climbing to the end of the slope.

You see two dark figures infront of you.

There are also two identical doors. One to your left and one to your right.

"Greetings adventurer. Congratulations on making it this far."

"We are the guardians of the doors." 

"One of these doors leads to the end sections of the labyrinth. The other
leads to death."

"We know which door is which." 

"You may ask us one question and then you must make a choice on which door
to open."

"But one of us always lies, the other always tells the truth."

"Now ask us... and make your choice."
"""
    print(path_four)
    available_questions = 1
    while play_game:
        if available_questions == 1:
            choice = input("Choose door or ask question? (door/ask) \n").lower().strip()
            if choice == "door" or choice == "d":
                choice = input("Which door do you choose? (right/left) \n").lower().strip()
                if choice == "right" or choice == "r":
                    right_door()
                    break
                elif choice == "left" or choice == "l":
                    fourth_riddle()
                    break
                else:
                    print("Invalid input. Please try again. \n")
            elif choice == "ask" or choice == "a":
                which_question = """
--------------------------------------------------------------

Question A: Ask figure one - Which door leads to death?

Question B: Ask figure two - Which door leads to death?

Question C: Ask figure one - Which door would the other figure tell me 
leads to death?

Question D: Ask figure two - Which door would the other figure tell me 
leads to death?
"""
                print(which_question)
                available_questions -= 1
                choice = input("Which question do you ask? (a/b/c/d) \n").lower().strip()
                if choice == "a" or choice == "question a":
                    print("\nThe left door leads to death.\n")
                elif choice == "b" or choice == "question b":
                    print("\nThe right door leads to death.\n")
                elif choice == "c" or choice == "question c":
                    print("\nThe other figure would say the left door leads to death.\n")
                elif choice == "d" or choice == "question d":
                    print("\nThe other figure would say the left door leads to death.\n")
                else:
                    print("Invalid input. Please try again. \n")
            else:
                print("Invalid input. Please try again. \n")
        else:
            choice = input("Which door do you choose? (right/left) \n").lower().strip()
            if choice == "right" or choice == "r":
                right_door()
                break
            elif choice == "left" or choice == "l":                    
                fourth_riddle()
                break
            else:
                print("Invalid input. Please try again. \n")

def third_riddle():
    riddle_three = riddle[2]["riddle"]
    riddle_three_answer = riddle[2]["correct"]
    path_three = """
--------------------------------------------------------------

You follow the steep path to your left upwards. 

The pathway turns left and then right.

You see the top of the path infront of you. 

You are almost at the top when another flash of light forces
you to close your eyes.

When you re-open them you see the Riddler standing at the top
of the slope.

"What a surprise that you are still alive adventurer!"

"Let's see if you are worthy of continuing my labyrinth."

The Riddler points at you.

"Riddle me this."
    """
    print(path_three)
    for char in riddle_three:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    guesses = 3
    while play_game:
        print(f"\nYou have {guesses} guesses left. \n")
        choice = input("What is your guess? \n").lower().strip()
        if choice == riddle_three_answer or choice == "a spider":
            fourth_chapter()
            break
        else:
            print('\n"You guessed incorrectly. Try again"')
            guesses -= 1
            if guesses == 0:
                you_die()
                break

def third_chapter():
    third_paragraph = """
--------------------------------------------------------------

"Very good! Another correct answer. This is getting interesting!"    

"I'm sure I'll see you again soon adventurer!"

The Riddler vanishes again in another flash of light.
"""
    print(third_paragraph)
    path_three = """Infront of you there are three pathways.

There is a walkway that leads around to the right, the end of the
path is visible and it looks like a dead end. 

There is a path directly infront of you that leads forwards and 
disappears around a corner.

There is also a steep path to your left which ascends upwards
and turns left again. The end of the path is hidden.
"""
    print(path_three)
    while play_game:
        choice = input("Which path do you take? (left/right/forward) \n").lower().strip()
        if choice == "left" or choice == "l":
            third_riddle()
            break
        elif choice == "right" or choice == "r":
            right = """
--------------------------------------------------------------

You decide to take a closer look at the seemingly dead end to
your right.

You walk to the end of the passage and run your hands along the stone
walls blocking your way.

You feel something underneath your hand. You crouch down to look.

You notice some small words carved into the stone wall.

The words read: "The answer to the Riddlers next riddle is a six letter
word beginning with S. You're welcome."
"""
            print(right)
            while play_game:
                back = input("Do you want to return back to the last junction or exit the labyrinth? (back/exit) \n").lower().strip()
                if back == "back" or back == "b":
                    back_paragraph = """
--------------------------------------------------------------

You retrace your steps back to where you were.
                    """
                    print(back_paragraph)
                    break
                elif back == "exit" or back == "e":
                    quit()
                else:
                    print("\nInvalid input. Please try again. \n")
        elif choice == "forward" or choice == "f":
            forward = """
--------------------------------------------------------------            

You follow the path forwards as it turns to the right and then
the left.

You notice the torchlight start to dim as you continue.

The path gets darker and darker until you have to put your hands
up infront of you to guide you.

It is now pitch black. You hear the faint sound of running water..

You step down with your left foot and the floor cracks and gives way.

You trip and fall forwards and crash through the floor.

You fall head-first down into the pit. You feel yourself descending
rapidly.

You hear running water beneath you.

You hit the water and it all goes black.

GAME OVER.
"""
            print(forward)
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

def second_riddle():
    riddle_two = riddle[1]["riddle"]
    riddle_two_answer = riddle[1]["correct"]
    path_two = """
--------------------------------------------------------------

You decide to follow the advice of the carvings on the wall and 
take the right path.

You can't help but wonder what could possibly be down the left path?

As you proceed down the right path, it turns to the left and continues
down into a long passage.

You slowly walk down the passageway. You get the feeling something is
about to happen.

Suddenly there is another flash of light and the Riddler appears infront
of you.

"Well well... I think it's time for another riddle!"

The Riddler points at you.

"Riddle me this."
    """
    print(path_two)
    for char in riddle_two:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    guesses = 3
    while play_game:
        print(f"\nYou have {guesses} guesses left. \n")
        choice = input("What is your guess? \n").lower().strip()
        if choice == riddle_two_answer or choice == "a castle":
            third_chapter()
            break
        else:
            print('\n"You guessed incorrectly. Try again"')
            guesses -= 1
            if guesses == 0:
                you_die()
                break

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

def you_die():
    final_words = """
--------------------------------------------------------------

"Your three guesses are up." 

The Ridder raises his hand.

"You are not worthy... YOU FAILED! BE GONE!"

There is a bright flash and everything fades to black...

GAME OVER.
    """
    print(final_words)
    while play_game:
        start = input("Would you like to try again? (yes/no) \n").lower().strip()
        if start == "yes" or start == "y":
            print("Let it begin! \n")
            begin_labyrinth()
            break
        elif start == "no" or start == "n":
            quit()
        else:
            print("Invalid input. Please try again. \n")

def first_riddle():
    riddle_one = riddle[0]["riddle"]
    riddle_one_answer = riddle[0]["correct"]
    path_one = """
--------------------------------------------------------------

You walk forwards into the path leading straight into the labyrinth.

Suddenly a dark shadowy figure appears before you.

The figure's face is obscured by a dark black cloak.

The figure speaks in a quiet raspy voice: "I am the one they call... The Ridder."

"If you cannot guess my riddle in three, you die."

The Riddler points at you.

"Riddle me this."
    """
    print(path_one)
    for char in riddle_one:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    guesses = 3
    while play_game:
        print(f"\nYou have {guesses} guesses left. \n")
        choice = input("What is your guess? \n").lower().strip()
        if choice == riddle_one_answer or choice == "a river":
            second_chapter()
            break
        else:
            print('\n"You guessed incorrectly. Try again"')
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
                    back = """
--------------------------------------------------------------

You retrace your steps back to where you were.
                    """
                    print(back)
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
        print("\nLet it begin! \n")
        begin_labyrinth()
        break
    elif start == "no" or start == "n":
        quit()
    else:
        print("Invalid input. Please try again. \n")

