import sys
from time import sleep
from riddles import riddle
from storyboard import *
from title import title_art

play_game = True

def typewriter(text):
    for char in text:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

print(title_art)
typewriter(intro_paragraph)

def play_again():
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

def go_back():
    while play_game:
        back = input("Do you want to return back to the last junction\
or exit the labyrinth? (back/exit) \n").lower().strip()
        if back == "back" or back == "b":
            print(back)
            break
        elif back == "exit" or back == "e":
            quit()
        else:
            print("\nInvalid input. Please try again. \n")

def you_die():
    print(final_words)
    play_again()

def riddle_me_this(riddle_question, riddle_answer, next_path, alt_answer):
    for char in riddle_question:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    guesses = 3
    while play_game:
        print(f"\nYou have {guesses} guesses left. \n")
        choice = input("What is your guess? \n").lower().strip()
        if choice == riddle_answer or choice == alt_answer:
            next_path()
            break
        else:
            print('\n"You guessed incorrectly. Try again"')
            guesses -= 1
            if guesses == 0:
                you_die()
                break

def door_riddle():
    available_questions = 1
    while play_game:
        if available_questions == 1:
            choice = input("Choose door or ask question? (door/ask) \n")\
                .lower().strip()
            if choice == "door" or choice == "d":
                choice = input("Which door do you choose? (right/left) \n")\
                    .lower().strip()
                if choice == "right" or choice == "r":
                    right_door()
                    break
                elif choice == "left" or choice == "l":
                    fourth_riddle()
                    break
                else:
                    print("Invalid input. Please try again. \n")
            elif choice == "ask" or choice == "a":
                print(which_question)
                available_questions -= 1
                choice = input("Which question do you ask? (a/b/c/d) \n")\
                    .lower().strip()
                if choice == "a" or choice == "question a":
                    print("\nThe left door leads to death.\n")
                elif choice == "b" or choice == "question b":
                    print("\nThe right door leads to death.\n")
                elif choice == "c" or choice == "question c":
                    print("\nThe other figure would say the left door leads to\
death.\n")
                elif choice == "d" or choice == "question d":
                    print("\nThe other figure would say the left door leads to\
death.\n")
                else:
                    print("Invalid input. Please try again. \n")
            else:
                print("Invalid input. Please try again. \n")
        else:
            choice = input("Which door do you choose? (right/left) \n")\
                .lower().strip()
            if choice == "right" or choice == "r":
                right_door()
                break
            elif choice == "left" or choice == "l":                    
                fourth_riddle()
                break
            else:
                print("Invalid input. Please try again. \n")


def take_treasure(): 
    print(bad_ending)
    play_again()

def leave():
    print(good_ending)
    play_again()

def end():
    print(end_paragraph)
    while play_game:
        choice = input("Do you take the treasure or leave without it? (\
take/leave) \n").lower().strip()
        if choice == "take" or choice == "t":
            take_treasure()
            break
        elif choice == "leave" or choice == "l":
            leave()
            break
        else:
            print("Invalid input. Please try again. \n")


def sixth_riddle():
    print(path_ten)
    riddle_question = riddle[5]["riddle"]
    riddle_answer = riddle[5]["correct"]
    next_path = end
    alt_answer = "naught"
    riddle_me_this(riddle_question, riddle_answer, next_path, alt_answer)

def fifth_riddle():
    print(path_nine)
    riddle_question = riddle[4]["riddle"]
    riddle_answer = riddle[4]["correct"]
    next_path = sixth_riddle
    alt_answer = "a tree"
    riddle_me_this(riddle_question, riddle_answer, next_path, alt_answer)


def fifth_chapter():
    print(fifth_paragraph)
    print(path_eight)
    while play_game:
        choice = input("Which path will you choose? (left/right) \n")\
            .lower().strip()
        if choice == "right" or choice == "r":
            fifth_riddle()
            break
        elif choice == "left" or choice == "l":
            print(left_descent)
            play_again()
        else:
            print("Invalid input. Please try again. \n")

def fourth_riddle():
    riddle_question = riddle[3]["riddle"]
    riddle_answer = riddle[3]["correct"]
    next_path = fifth_chapter
    alt_answer = "the moon"
    print(path_seven)
    riddle_me_this(riddle_question, riddle_answer, next_path, alt_answer)

def right_door():
    print(right_door_choice)
    play_again()

def fourth_chapter():
    print(fourth_paragraph)
    print(path_six)
    door_riddle()

def third_riddle():
    riddle_question = riddle[2]["riddle"]
    riddle_answer = riddle[2]["correct"]
    next_path = fourth_chapter
    alt_answer = "a spider"
    print(path_five)
    riddle_me_this(riddle_question, riddle_answer, next_path, alt_answer)

def third_chapter():
    print(third_paragraph)
    print(path_four)
    while play_game:
        choice = input("Which path do you take? (left/right/forward) \n")\
            .lower().strip()
        if choice == "left" or choice == "l":
            third_riddle()
            break
        elif choice == "right" or choice == "r":
            print(right)
            go_back()
        elif choice == "forward" or choice == "f":
            print(forward)
            play_again()
        else:
            print("Invalid input. Please try again. \n")

def second_riddle():
    riddle_question = riddle[1]["riddle"]
    riddle_answer = riddle[1]["correct"]
    next_path = third_chapter
    alt_answer = "a castle"
    print(path_three)
    riddle_me_this(riddle_question, riddle_answer, next_path, alt_answer)

def second_chapter():
    print(second_paragraph)
    print(path_two)
    while play_game:
        choice = input("Which path will you choose? (left/right) \n")\
            .lower().strip()
        if choice == "right" or choice == "r":
            second_riddle()
            break
        elif choice == "left" or choice == "l":
            print(second_left)
            play_again()
        else:
            print("Invalid input. Please try again. \n")

def first_riddle():
    riddle_question = riddle[0]["riddle"]
    riddle_answer = riddle[0]["correct"]
    next_path = second_chapter
    alt_answer = "a river"
    print(path_one)
    riddle_me_this(riddle_question, riddle_answer, next_path, alt_answer)
        
def begin_labyrinth():
    print(first_paragraph)
    while play_game:
        choice = input("Which path will you choose? (forward/left) \n")\
            .lower().strip()
        if choice == "forward" or choice == "f":
            first_riddle()
            break
        elif choice == "left" or choice == "l":
            print(left)
            go_back()
        else:
            print("Invalid input. Please try again. \n")

while play_game:
    start = input("Do you wish to enter the Labyrinth of Riddles? (yes/no)\
        \n").lower().strip()
    if start == "yes" or start == "y":
        print("\nLet it begin! \n")
        begin_labyrinth()
        break
    elif start == "no" or start == "n":
        quit()
    else:
        print("Invalid input. Please try again. \n")

