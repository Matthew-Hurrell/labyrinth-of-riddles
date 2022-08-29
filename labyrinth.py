import sys
from time import sleep
from riddles import riddle
from storyboard import *
from title import title_art

print(title_art)

print(intro_paragraph)

play_game = True

def take_treasure(): 
    print(bad_ending)
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

def leave():
    print(good_ending)
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

def end():
    print(end_paragraph)
    while play_game:
        choice = input("Do you take the treasure or leave without it? (take/leave) \n").lower().strip()
        if choice == "take" or choice == "t":
            take_treasure()
            break
        elif choice == "leave" or choice == "l":
            leave()
            break
        else:
            print("Invalid input. Please try again. \n")


def sixth_riddle():
    riddle_six = riddle[5]["riddle"]
    riddle_six_answer = riddle[5]["correct"]
    print(path_ten)
    for char in riddle_six:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    guesses = 3
    while play_game:
        print(f"\nYou have {guesses} guesses left. \n")
        choice = input("What is your guess? \n").lower().strip()
        if choice == riddle_six_answer:
            end()
            break
        else:
            print('\n"You guessed incorrectly. Try again"')
            guesses -= 1
            if guesses == 0:
                you_die()
                break

def fifth_riddle():
    riddle_five = riddle[4]["riddle"]
    riddle_five_answer = riddle[4]["correct"]
    print(path_nine)
    for char in riddle_five:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    guesses = 3
    while play_game:
        print(f"\nYou have {guesses} guesses left. \n")
        choice = input("What is your guess? \n").lower().strip()
        if choice == riddle_five_answer or choice == "a tree":
            sixth_riddle()
            break
        else:
            print('\n"You guessed incorrectly. Try again"')
            guesses -= 1
            if guesses == 0:
                you_die()
                break


def fifth_chapter():
    print(fifth_paragraph)
    print(path_eight)
    while play_game:
        choice = input("Which path will you choose? (left/right) \n").lower().strip()
        if choice == "right" or choice == "r":
            fifth_riddle()
            break
        elif choice == "left" or choice == "l":
            print(left_descent)
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
    print(path_seven)
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
    print(fourth_paragraph)
    print(path_six)
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
    print(path_five)
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
    print(third_paragraph)
    print(path_four)
    while play_game:
        choice = input("Which path do you take? (left/right/forward) \n").lower().strip()
        if choice == "left" or choice == "l":
            third_riddle()
            break
        elif choice == "right" or choice == "r":
            print(right)
            while play_game:
                back = input("Do you want to return back to the last junction or exit the labyrinth? (back/exit) \n").lower().strip()
                if back == "back" or back == "b":
                    print(back)
                    break
                elif back == "exit" or back == "e":
                    quit()
                else:
                    print("\nInvalid input. Please try again. \n")
        elif choice == "forward" or choice == "f":
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
    print(path_three)
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
    print(second_paragraph)
    print(path_two)
    while play_game:
        choice = input("Which path will you choose? (left/right) \n").lower().strip()
        if choice == "right" or choice == "r":
            second_riddle()
            break
        elif choice == "left" or choice == "l":
            print(second_left)
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
    print(first_paragraph)
    while play_game:
        choice = input("Which path will you choose? (forward/left) \n").lower().strip()
        if choice == "forward" or choice == "f":
            first_riddle()
            break
        elif choice == "left" or choice == "l":
            print(left)
            while play_game:
                dead_end_choice = input("Do you want to return back \
or do you want to exit the labyrinth (back/exit) \n").lower().strip()
                if dead_end_choice == "back" or dead_end_choice == "b":
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

