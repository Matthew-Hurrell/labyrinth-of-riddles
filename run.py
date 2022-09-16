# Module for typewriter effect
import sys
# Module for typewriter time delay
from time import sleep
# Module containing riddles list
from riddles import riddle
# Module containing storyboard variables with large sections of text
from storyboard import *
# Module containing project word-art title
from title import title_art

# Global variable for function loops
play_game = True

# Global variable for username
username = ""


def process_name():
    """
    Process name function.
    Called at beginning of program after intro paragraph.
    Features a while loop which continues until a suitable user input is
    obtained.
    User is prompted to enter a name. The user name input is processed
    to lowercase and stripped of all surrounding whitespace.
    There is then an if/elif/else statement to check if the username passes
    certain requirements. If the username length is less that one character
    or the username is greater than twenty characters the user is informed
    that their input is either too long or too short and the loop repeats.
    The characters of the user input are then looped through. If the characters
    are all alphanumeric and/or contain spaces the global username variable is
    updated to the user name input value stripped of excess whitespace with
    each first letter of each word capitalised. The break statement is also
    used to break out of the loop.
    If the name input doesn't satisfy the previous conditions then it must
    contain either a symbol or a number. The final elif statement loops
    through the characters in the user input name again and checks if they
    are digits. If any of them are the user is informed that the name cannot
    contain a number and the loop is repeated.
    Finally the else statement informs the user that the name cannot contain
    a symbol and the loop is repeated.
    """

    while play_game:
        name = input("    What is your name adventurer? \n    \
").lower().strip()
        if len(name) < 1:
            print("\n    Length of username is too short. Please try again.\n")
        elif len(name) > 20:
            print("\n    Length of username is too long. Please try again.\n")
        elif all(char.isalpha() or char.isspace() for char in name):
            global username
            username = " ".join(name.split()).title()
            break
        elif any(char.isdigit() for char in name):
            print("\n    Your name cannot contain a number. Please try again.\
\n")
        else:
            print("\n    Your name cannot contain a symbol. Please try again.\
\n")


# Prints word-art title to terminal
print(title_art)

# Prints intro paragraph to terminal
typewriter(intro_paragraph)


def play_again():
    """
    Play again function.
    Called when a user character dies or fails.
    Features a while loop which evaluates user input and either begins
    the program again from the start or exits the program.
    The loop continues until a valid input is received from the user.
    The user input is converted into lowercase and stripped of all
    surrounding whitespace before it is processed.
    """
    while play_game:
        start = input("    Do you wish to play again? (yes/no) \n    \
").lower().strip()
        if start == "yes" or start == "y":
            typewriter("\n    Let it begin! \n")
            begin_labyrinth()
            break
        elif start == "no" or start == "n":
            exit_labyrinth_function(username)
            quit()
        else:
            print("    Invalid input. Please try again. \n")


def exit():
    """
    Exit function.
    Called when a user enters exit into an input during the program.
    Features a while loop which prompts the user to confirm their
    decision to exit the program.
    Confirming the exit displays a short exit message and exits the program.
    Declining the exit breaks out of the loop and returns the user to the
    previous loop.
    The loop continues until a valid input is received from the user.
    The user input is converted into lowercase and stripped of all
    surrounding whitespace before it is processed.
    """
    while play_game:
        sure = input("\n    Are you sure you wish to exit? Progress\
 will be lost. (yes/no)\n    ").lower().strip()
        if sure == "yes" or sure == "y":
            exit_labyrinth_function(username)
            quit()
        elif sure == "no" or sure == "n":
            print("")
            break
        else:
            print("\n    Invalid input. Please try again. \n")


def go_back():
    """
    Go back function.
    Called when a user reaches a dead end in the labyrinth.
    Features a while loop which gives the user the option of returning back
    to the previous junction or exiting the labyrinth.
    Exiting the labyrinth calls the exit function.
    Returning back breaks out of the loop into the previous loop.
    The loop continues until a valid input is received from the user.
    The user input is converted into lowercase and stripped of all
    surrounding whitespace before it is processed.
    """
    while play_game:
        back = input("    Do you want to return back to the last junction\
 or exit the labyrinth?\n    (back/exit) \n    ").lower().strip()
        if back == "back" or back == "b":
            typewriter(return_back)
            break
        elif back == "exit" or back == "e":
            exit()
        else:
            print("\n    Invalid input. Please try again. \n")


def you_die():
    """
    Character death function.
    Called when a user runs out of guesses for any of the riddles.
    Prints the final words text variable from the storyboard module and
    calls the play again function.
    """
    final_words_function(username)
    play_again()


def riddle_me_this(riddle_question, riddle_answer, next_path, alt_answer):
    """
    Riddle function.
    Passed arguments from the current riddle function.
    Arguments include the riddle question and answer from the riddles module
    list as well as the next path to send the user when a correct answer
    is inputted and the alternate answer for the riddle.
    Guesses variable is defined as three and decreases by one with each
    incorrect answer.
    Riddle question is printed to the terminal using the typewriter effect
    loop.
    A while loop is defined which checks if the user input matches the riddle
    answer or alternative answer variables.
    If the user is correct the user is sent to the next path and is broken
    out of the loop.
    If the user is incorrect one is deducted from the guesses variable and
    the variable is checked to see if it is 0. If it is the user is out of
    guesses and the you die function is called.
    A user can also exit the program and the exit function is called.
    The loop continues until a valid input is received from the user.
    The user input is converted into lowercase and stripped of all
    surrounding whitespace before it is processed.
    """
    for char in riddle_question:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    guesses = 3
    while play_game:
        print(f"\n    You have {guesses} guess(es) left. \n")
        print('    To exit the labyrinth type "exit". \n')
        choice = input("    What is your guess? \n    ").lower().strip()
        if choice == riddle_answer or choice == alt_answer:
            next_path()
            break
        elif choice == "exit" or choice == "e" or choice == '"exit"':
            exit()
        else:
            guesses -= 1
            if guesses == 0:
                you_die()
                break
            else:
                typewriter('\n    "You guessed incorrectly. Try again"\n')


def door_riddle():
    """
    Door riddle function.
    Called when the user gets to the fourth chapter.
    Sets available questions variable to one and then defines a while loop.
    Inside the loop the available questions variable is checked if it is equal
    to one. If it is the user is asked whether they want to exit, choose a
    door or ask a question.
    Right door calls the right door function which ends in a death.
    Left door moves the user forward into the next chapter and calls the
    fourth riddle function.
    A user can also exit the program and the exit function is called.
    The loop continues until a valid input is received from the user.
    The user input is converted into lowercase and stripped of all
    surrounding whitespace before it is processed.
    If ask a question is selected another nested while loop is defined and
    the user chooses one question out of four options to ask.
    Each question choice prints an answer to the terminal, then reduces the
    available question variable by one and breaks out of the nested loop into
    the outer loop. The outer loop then tests the available questions
    variable and sends the user to another loop which just features a choice
    on which door without the option to ask a question.
    """
    available_questions = 1
    while play_game:
        if available_questions == 1:
            choice = input("    Choose door or ask question? (door/ask/exit)\
 \n    ").lower().strip()
            if choice == "door" or choice == "d":
                choice = input("    Which door do you choose? (right/left) \n \
   ").lower().strip()
                if choice == "right" or choice == "r":
                    right_door()
                    break
                elif choice == "left" or choice == "l":
                    fourth_riddle()
                    break
                else:
                    print("    Invalid input. Please try again. \n")
            elif choice == "ask" or choice == "a":
                typewriter(which_question)
                while play_game:
                    choice = input("    Which question do you ask? (a/b/c/d) \
 \n    ").lower().strip()
                    if choice == "a" or choice == "question a":
                        typewriter('\n    "The left door leads to death."\n')
                        available_questions -= 1
                        break
                    elif choice == "b" or choice == "question b":
                        typewriter('\n    "The right door leads to death."\n')
                        available_questions -= 1
                        break
                    elif choice == "c" or choice == "question c":
                        typewriter('\n    "The other figure would say the left\
 door leads to death."\n')
                        available_questions -= 1
                        break
                    elif choice == "d" or choice == "question d":
                        typewriter('\n    "The other figure would say the left\
 door leads to death."\n')
                        available_questions -= 1
                        break
                    else:
                        print("    Invalid input. Please try again. \n")
            elif choice == "exit" or choice == "e":
                exit()
            else:
                print("    Invalid input. Please try again. \n")
        else:
            choice = input("\n    Which door do you choose? (right/left/exit)\
 \n    ").lower().strip()
            if choice == "right" or choice == "r":
                right_door()
                break
            elif choice == "left" or choice == "l":
                fourth_riddle()
                break
            elif choice == "exit" or choice == "e":
                exit()
            else:
                print("    Invalid input. Please try again. \n")


def take_treasure():
    """
    Take treasure function.
    Called when the user opts to take the treasure at the end of the program.
    Displays the bad ending text from the storyboard module and calls the
    play again function.
    """
    typewriter(bad_ending)
    play_again()


def leave():
    """
    Leave function.
    Called when the user opts to leave the treasure and exit the labyrinth
    at the end of the program.
    Displays the good ending text from the storyboard module and calls the
    play again function.
    """
    good_ending_function(username)
    play_again()


def end():
    """
    End function.
    Called when the user answers the final riddle correctly.
    Prints the end paragraph from the storyboard module.
    Features a loop with a user input giving the user a choice to take
    or leave the treasure.
    The loop continues until a valid input is received from the user.
    The user input is converted into lowercase and stripped of all
    surrounding whitespace before it is processed.
    Taking the treasure calls the take treasure function and breaks out
    of the loop.
    Leaving the treasure calls the leave function and breaks out of the
    loop.
    """
    end_paragraph_function(username)
    while play_game:
        choice = input("    Do you take the treasure or leave without it? (\
take/leave) \n    ").lower().strip()
        if choice == "take" or choice == "t":
            take_treasure()
            break
        elif choice == "leave" or choice == "l":
            leave()
            break
        else:
            print("    Invalid input. Please try again. \n")


def sixth_riddle():
    """
    Sixth riddle function.
    Called after successfully answering the fifth riddle in the fifth riddle
    function.
    Prints path ten from the storyboard module.
    Sets variables to riddle question and riddle answer to the sixth riddle
    in the riddles list of dictionaries.
    Sets the variables for the next path to call the end function and the
    alternative answer to the string "naught".
    Calls riddle me this function and passes the variables declared into
    the function arguments.
    """
    path_ten_function(username)
    riddle_question = riddle[5]["riddle"]
    riddle_answer = riddle[5]["correct"]
    next_path = end
    alt_answer = "naught"
    riddle_me_this(riddle_question, riddle_answer, next_path, alt_answer)


def fifth_riddle():
    """
    Fifth riddle function.
    Called after taking the right path in the fifth chapter.
    Prints path nine from the storyboard module.
    Sets variables to riddle question and riddle answer to the fifth riddle
    in the riddles list of dictionaries.
    Sets the variables for the next path to call the end function and the
    alternative answer to the string "a tree".
    Calls riddle me this function and passes the variables declared into
    the function arguments.
    """
    path_nine_function(username)
    riddle_question = riddle[4]["riddle"]
    riddle_answer = riddle[4]["correct"]
    next_path = sixth_riddle
    alt_answer = "a tree"
    riddle_me_this(riddle_question, riddle_answer, next_path, alt_answer)


def fifth_chapter():
    """
    Fifth chapter function.
    Called after a user successfully answers the fourth riddle.
    Prints fifth paragraph and path eight from the storyboard module.
    Declares a loop which gives the user an option to either go left, right
    or exit the labyrinth.
    Right calls teh fifth riddle function and breaks out of the loop.
    Left prints the left decent text from the storyboard module and calls
    the play again function.
    Exit calls the exit function.
    The loop continues until a valid input is received from the user.
    The user input is converted into lowercase and stripped of all
    surrounding whitespace before it is processed.
    """
    fifth_paragraph_function(username)
    typewriter(path_eight)
    while play_game:
        choice = input("    Which path will you choose? (left/right/exit) \n\
    ").lower().strip()
        if choice == "right" or choice == "r":
            fifth_riddle()
            break
        elif choice == "left" or choice == "l":
            typewriter(left_descent)
            play_again()
        elif choice == "exit" or choice == "e":
            exit()
        else:
            print("    Invalid input. Please try again. \n")


def fourth_riddle():
    """
    Fourth riddle function.
    Called after the user chooses the correct door in the door riddle
    function.
    Prints path seven from the storyboard module.
    Sets variables to riddle question and riddle answer to the fourth riddle
    in the riddles list of dictionaries.
    Sets the variables for the next path to call the fifth chapter function
    and the alternative answer to the string "the moon".
    Calls riddle me this function and passes the variables declared into
    the function arguments.
    """
    riddle_question = riddle[3]["riddle"]
    riddle_answer = riddle[3]["correct"]
    next_path = fifth_chapter
    alt_answer = "the moon"
    typewriter(path_seven)
    riddle_me_this(riddle_question, riddle_answer, next_path, alt_answer)


def right_door():
    """
    Right door function.
    Called when the user choose to enter the right door in the door riddle
    function.
    Prints the right door choice text from the storyboard module.
    Calls the play again function.
    """
    typewriter(right_door_choice)
    play_again()


def fourth_chapter():
    """
    Fourth chapter function.
    Called when the user correctly answers the third riddle.
    Prints the fourth paragraph and path six variables from the storyboard
    module.
    Calls the door riddle function.
    """
    fourth_paragraph_function(username)
    path_six_function(username)
    door_riddle()


def third_riddle():
    """
    Third riddle function.
    Called after the user chooses the left option in the third chapter
    function.
    Prints path five from the storyboard module.
    Sets variables to riddle question and riddle answer to the third riddle
    in the riddles list of dictionaries.
    Sets the variables for the next path to call the fourth chapter function
    and the alternative answer to the string "a spider".
    Calls riddle me this function and passes the variables declared into
    the function arguments.
    """
    riddle_question = riddle[2]["riddle"]
    riddle_answer = riddle[2]["correct"]
    next_path = fourth_chapter
    alt_answer = "a spider"
    path_five_function(username)
    riddle_me_this(riddle_question, riddle_answer, next_path, alt_answer)


def third_chapter():
    """
    Third chapter function.
    Called when the user answers the second riddle correctly.
    Prints the third paragraph and path four variables from the storyboard
    module.
    Declares a while loop which asks the user which path they wish to take.
    Also gives the user an option the exit the program.
    The loop continues until a valid input is received from the user.
    The user input is converted into lowercase and stripped of all
    surrounding whitespace before it is processed.
    Left calls the third riddle function and breaks out of the loop.
    Right prints the right variable from the storyboard module and calls
    the go back function.
    Forward prints the forward variable from the storyboard module and
    calls the play again function.
    Exit calls the exit function.
    """
    third_paragraph_function(username)
    typewriter(path_four)
    while play_game:
        choice = input("    Which path do you take? (left/right/forward/exit)\
 \n    ").lower().strip()
        if choice == "left" or choice == "l":
            third_riddle()
            break
        elif choice == "right" or choice == "r":
            typewriter(right)
            go_back()
        elif choice == "forward" or choice == "f":
            typewriter(forward)
            play_again()
        elif choice == "exit" or choice == "e":
            exit()
        else:
            print("    Invalid input. Please try again. \n")


def second_riddle():
    """
    Second riddle function.
    Called after the user chooses the right option in the second chapter
    function.
    Prints path three from the storyboard module.
    Sets variables to riddle question and riddle answer to the second riddle
    in the riddles list of dictionaries.
    Sets the variables for the next path to call the third chapter function
    and the alternative answer to the string "a castle".
    Calls riddle me this function and passes the variables declared into
    the function arguments.
    """
    riddle_question = riddle[1]["riddle"]
    riddle_answer = riddle[1]["correct"]
    next_path = third_chapter
    alt_answer = "a castle"
    path_three_function(username)
    riddle_me_this(riddle_question, riddle_answer, next_path, alt_answer)


def second_chapter():
    """
    Second chapter function.
    Called when the user answers the first riddle correctly.
    Prints the second paragraph and path two variables from the storyboard
    module.
    Declares a while loop which asks the user which path they wish to take.
    Also gives the user an option the exit the program.
    The loop continues until a valid input is received from the user.
    The user input is converted into lowercase and stripped of all
    surrounding whitespace before it is processed.
    Right calls the second riddle function and breaks out of the loop.
    Left prints the second left variable from the storyboard function and
    calls the play again function.
    Exit calls the exit function.
    """
    second_paragraph_function(username)
    path_two_function(username)
    while play_game:
        choice = input("    Which path will you choose? (left/right/exit) \n\
    ").lower().strip()
        if choice == "right" or choice == "r":
            second_riddle()
            break
        elif choice == "left" or choice == "l":
            typewriter(second_left)
            play_again()
        elif choice == "exit" or choice == "e":
            exit()
        else:
            print("    Invalid input. Please try again. \n")


def first_riddle():
    """
    First riddle function.
    Called after the user chooses the forward option in the begin labyrinth
    function.
    Prints path one from the storyboard module.
    Sets variables to riddle question and riddle answer to the first riddle
    in the riddles list of dictionaries.
    Sets the variables for the next path to call the second chapter function
    and the alternative answer to the string "a river".
    Calls riddle me this function and passes the variables declared into
    the function arguments.
    """
    riddle_question = riddle[0]["riddle"]
    riddle_answer = riddle[0]["correct"]
    next_path = second_chapter
    alt_answer = "a river"
    typewriter(path_one)
    riddle_me_this(riddle_question, riddle_answer, next_path, alt_answer)


def begin_labyrinth():
    """
    Begin labyrinth function.
    Called when the user chooses to enter the labyrinth of riddles in the
    first play game loop.
    Prints the first paragraph and path two variables from the storyboard
    module.
    Declares a while loop which asks the user which path they wish to take.
    Also gives the user an option the exit the program.
    The loop continues until a valid input is received from the user.
    The user input is converted into lowercase and stripped of all
    surrounding whitespace before it is processed.
    Forward calls the first riddle function and breaks out of the loop.
    Left prints the left variable from the storyboard module and calls the
    go back function.
    Exit calls the exit function.
    """
    typewriter(first_paragraph)
    while play_game:
        choice = input("    Which path will you choose? (forward/left/exit) \n\
    ").lower().strip()
        if choice == "forward" or choice == "f":
            first_riddle()
            break
        elif choice == "left" or choice == "l":
            typewriter(left)
            go_back()
        elif choice == "exit" or choice == "e":
            exit()
        else:
            print("    Invalid input. Please try again. \n")


while play_game:
    """
    Start game while loop.
    The loop continues until a valid input is received from the user.
    The user input is converted into lowercase and stripped of all
    surrounding whitespace before it is processed.
    Asks the user if they wish to enter the labyrinth of riddles.
    Yes prints a small section of text to the terminal and calls the
    begin labyrinth function. It also breaks out of the loop.
    No calls the quit function and exits the program.
    """
    process_name()
    typewriter(f"\n    Welcome {username}. \n\n")
    start = input("    Do you wish to enter the Labyrinth of Riddles? (yes/no)\
\n    ").lower().strip()
    if start == "yes" or start == "y":
        typewriter("\n    Let it begin! \n")
        begin_labyrinth()
        break
    elif start == "no" or start == "n":
        exit_labyrinth_function(username)
        quit()
    else:
        print("    Invalid input. Please try again. \n")
