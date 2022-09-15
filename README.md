# **_The Labyrinth of Riddles_**

The Labyrinth of Riddles is a terminal game which a user can interact with via the Code Institute mock terminal on Heroku.

The target audience is anyone interested in text and puzzle based computer games. The audience will mainly include teens and above, men and women. Also anyone that has an interest in riddles and word games.

The goal of this online program is to provide a fun and interactive role-playing game where users can test their puzzle solving skills for entertainment purposes.

Navigating the game should be easy and intuitive for all users. The puzzle content should be challenging but well balanced for a diverse audience. Text should be well displayed and easy to read. The narrative should be coherent and engaging to encourage users to continue to progress through the game.

Link to the live site - [The Labyrinth of Riddles](https://labyrinth-of-riddles.herokuapp.com/)

![The Labyrinth of Riddles Main Image](readme-images/labyrinth-of-riddles.png)

# Contents

* [**User Experience UX**](<#user-experience-ux>)
    * [User Stories](<#user-stories>)
    * [Structure](<#structure>)
    * [Typography](<#typography>)
* [**Features**](<#features>)
    * [**Existing Features**](<#existing-features>)
        * [Title](<#title>)
        * [Storyboard](<#storyboard>)
        * [Riddles](<#riddles>)
        * [Labyrinth Structure](<#labyrinth-structure>)
        * [Typewriter Effect](<#typewriter-effect>)
        * [Input Validation](<#input-validation>)
        * [Process Name Function](<#process-name-function>)
        * [Chapter Functions](<#chapter-functions>) 
        * [Riddle Functions](<#riddle-functions>) 
        * [Riddle Me This Function](<#riddle-me-this-function>) 
        * [Door Riddle Function](<#door-riddle>)       
        * [Play Again Function](<#play-again-function>) 
        * [Exit Function](<#exit-function>) 
        * [Go Back Function](<#go-back-function>) 
        * [You Die Function](<#play-again-function>) 
        * [End Function](<#end-function>) 
        * [Multiple Endings](<#multiple-endings>) 
    * [**Future Features**](<#future-features>)
* [**Technologies Used**](<#technologies-used>)
* [**Testing**](<#testing>)
     * [**Validator Tests**](<#validator-tests>)
     * [**Terminal Tests**](<#terminal-tests>)
     * [**Input Validation Tests**](<#input-validation-tests>)
     * [**Bugs**](<#bugs>)
        * [Resolved](<#resolved>)
        * [Unresolved](<#unresolved>)
* [**Deployment**](<#deployment>)
     * [**Project Deployment Via Heroku**](<#project-deployment-via-heroku>)
* [**Credits**](<#credits>)
    * [**Content**](<#content>)
    * [**Media**](<#media>)
    * [**Code**](<#code>)
*  [**Acknowledgements**](<#acknowledgements>)

# User Experience UX

## User Stories

* As a user I want to be able to understand the purpose and intention of the program when it first starts.
* As a user I want to be given the option to start or end the program with my first interaction.
* As a user I want the program navigation to be intuitive and easy to understand.
* As a user I want to be given the opportunity to exit the program frequently and easily.
* As a user I want to be warned that I will lose my progress if I exit the program and be given the opportunity to go back if I change my mind.
* As a user I want my input to be validated and error checked so I can re-enter my choice if it is invalid.
* As a user I want the storyline and narrative to be coherent, engaging and well structured.
* As a user I want the text to be well laid out and easy to read.
* As a user I want the puzzles and riddles to be challenging but well balanced.
* As a user I want to have three guesses at each riddle before losing the game.
* As a user I want a change in typography to help me differentiate between normal text and important sections.
* As a user to be given the option to play again if I win or lose.
* As a user I want different endings and outcomes based on my choices.
* As a user I want to be able to go back to a previous junction if I face a dead end in the labyrinth.
* As a user I want to be presented with multiple choices throughout the game that allow me to choose my own path.

[Back to top](<#contents>)

## Structure 

The Labyrinth of Riddles is structured using various loops and functions to allow a user to navigate through a digital labyrinth with text based commands. The program is purely text based and the user is unaware of the structure of the labyrinth while playing. Each choice presented to the user displays the options and text based input required to make that option. The user progresses through the labyrinth linearly and can only complete the labyrinth if they make all the correct navigational and riddle choices. If a user finds a dead end they are given the option to return to the previous junction. If a user character dies the user is given the option to return to the beginning of the labyrinth to start again. An option to exit the labyrinth/program is presented as an alternative option to the user with each choice they make.

[Back to top](<#contents>)

## Typography 

Because The Labyrinth of Riddles is a terminal program, style and design options are very limited. Font type and colour is default to the terminal but escape codes are used when printing the riddle elements to the terminal to make them more eye-catching to the user. The riddle dictionary items all contain bold (\033[1m) and italic (\x1B[3m) escape commands as well as the closing codes at the end of each riddle (\x1B[0m) and (\033[0m) to ensure the subsequent text isn't also affected.

[Back to top](<#contents>)

# Features

The Labyrinth of Riddles contains many features which help to enhance the users overall experience. Back-end functionality and interactivity are integral to a positive user experience within the limitations of this terminal-based project.

## Existing Features

### Title

The title for The Labyrinth of Riddles is the first element displayed in the terminal when the program begins. It is ASCII word art generated using an online program called [Patorjk](http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=The%20Labyrinth%20%0Aof%20Riddles). The font style is called ANSI Shadow. The title is saved into a separate python module called title.py and saved into a variable called title_art. The title module is imported into the run.py file and the title variable is printed to the terminal from the run.py module. Although styling is limited within the terminal, word art is used to work within those limitations to provide a basic yet eye catching beginning to the program. 

![The Labyrinth of Riddles Title](readme-images/title.png)

[Back to top](<#contents>)

### Storyboard

The large paragraphs of text required for the storyboard are saved into variables in a seperate python module called storyboard.py. This helps to avoid unnecessary clutter in the run.py main python module. The storyboard variables consist of multi-line strings defined by the triple quotation marks opening and closing syntax. This allows for all indentation and paragraphing to remain easily editable and consistent. The storyboard.py module is imported into the run.py file along with all its contents. All storyboard variables are printed to the terminal using the typewriter function from the run.py file. Variables are printed in the relevant chapters in the story as the user progresses through the labyrinth. The story is all original but elements are inspired by the [Labyrinth](https://www.imdb.com/title/tt0091369/) movie. Text content is written to engage the user in the storyline with fantasy role playing elements. The user charater is kept gender neutral to not alienate any audience interested in playing.

![Storyboard.py file](readme-images/storyboard.png)

![Storyboard Intro Paragraph](readme-images/storyboard-two.png)

![Storyboard Path Choice](readme-images/storyboard-three.png)

[Back to top](<#contents>)

### Riddles

The riddles used throughout the program are saved into a separate python module called riddles.py. These riddles are saved into a variable called riddle which contains a list of dictionaries. Each dictionary contains a riddle with the key of riddle and a riddle answer with the key of correct. The riddle list of dictionaries is imported into the run.py module so it can be used in the program. The riddle elements of the dictionaries also contain opening and closing escape codes for bold and italicized text. They also contain escape characters for line breaks. There are six riddles with corresponding correct answers saved into the riddle list of dictionaries. Riddles are then accessed and printed to the terminal using the typewriter effect from the run.py file in the riddle me this function. 

![Riddles.py list](readme-images/riddles.png)

![Riddle Terminal Display](readme-images/riddle-two.png)

[Back to top](<#contents>)

### Labyrinth Structure

The Labyrinth of Riddles maze structure is based off of an image found online at [Difference Between](http://www.differencebetween.info/difference-between-maze-and-labyrinth). The use of an image for the maze structure greatly helped with the planning stage of the labyrinth. Navigational choices throughout the Labyrinth of Riddles follow the structure of the maze image. Dead ends either lead to characters deaths or the opportunity to go back to the previous junction. Each correct navigational choice leads to another riddle and progression to the next chapter.

![Labyrinth Structure Image](readme-images/Labyrinth-structure.png)

[Back to top](<#contents>)

### Typewriter Effect

A typewriter effect is used to add a minor animation effect to large blocks of text. This provides a more interesting experience for the user and also helps the user to differentiate new text elements from previous paragraphs. It also provides a time delay between printing each character to roughly similate a users reading speed. The typewriter function is defined in the run.py python module. The function is passed variables containing strings as an argument and uses a loop to print each character within the string with a slight time delay. To enable this functionality, run.py imports sys (system), and sleep from the time module at the beginning of the program. Text is then printed to the terminal using the typewriter effect by passing in a storyboard text variable in the appropriate chapter or section of the program.

![Typewriter Function](readme-images/typewriter-function.png)

![Calling The Typewriter Function](readme-images/typewriter.png)

![Typewriter Terminal Display](readme-images/typewriter-terminal.png)

[Back to top](<#contents>)

### Input Validation

Input validation is a very crucial element in the functionality of the Labyrinth of Riddles. All user inputs are strings which are removed of any capitalisation and stripped of any surrounding whitespace before being processed. This is done using the .lower() and .strip() inbuilt python functions. 

User inputs for navigational choices are evaluated using an if/elif/else statement inside a while loop. A user is presented with a list of input options when they are prompted to make a choice of two or more options. The if statement then checks for valid user text input, and if a string in the if/elif statement matches a user input the user is directed to the next function and the break statement is used to break out of the loop. If no matches to the user input are found the else statement is activated and "Invalid input. Please try again." is printed to the terminal. The loop then returns to the beginning with the prompt for the user to make a choice. This loop continues until a valid input from the user is entered. All navigational choices can also be made by simply typing the first letter of the word.

User inputs for riddles are validated slightly differently. A while loop and if/elif/else statements are still used in the riddle me this function but any invalid input will be processed as incorrect and will decrease the users number of available guesses by one. If this wasn't processed differently the user would have unlimited guesses for each riddle and then the game wouldn't be as challenging. User input for the riddles is compared against the correct key value in the riddle dictionary and also the alternative answer passed into the riddle me this function from the previous function. A matching answer to either of these passes the user to the next chapter and breaks the user out of the loop. The user is also given the option to exit the program. 

The process name function also requires a lot of input validation before being processed. The username is only accepted when it is above zero characters and below 20 characters long. It also cannot contain symbols or numbers. The length of the user input is tested using len(name) and an if statement. Absence of numbers and symbols is tested using a for loop and an or statement testing each character with isalpha() and isspace(). This is how it is evaluated to not include any digits or symbols. If it passes this test the user input is stripped of any excess whitespace using " ".join(name.split()) and each first letter of each word is capitalised using .title(). This is then assigned to a global variable of user name using the global statement. If the user input doesn't statisfy any of the previous conditions the input must contain either a number or a symbol. The input is then passed to the next elif statement and is looped through again using a for loop and the isdigit() method to determine if any numbers are present. If numbers are detected the user is informed and the loop repeats. If no numbers are detected the else statement is triggered as the user must have a symbol in the input. The user is informed of this and the loop repeats.

![Input Validation Function Example](readme-images/input-validation.png)

![Input Validation Terminal Display](readme-images/input-validation-two.png)

![Process Name Function Terminal Display](readme-images/process-name-function-terminal.png)

[Back to top](<#contents>)

### Process Name Function

The process name function is called on run.py at the beginning of the program after the intro paragraph is printed to the terminal. The purpose of the function is to prompt the user for their name and then process and evaluate the user input to ensure it meets certain criteria. If the name passes all tests it is saved into a global username variable on run.py. This variable is then used throughout the story elements in the program to insert the users name into the story for a more personal user experience. The function feaatures a while loop which repeats until a suitable username is entered. When a user enters a name the string is stripped of all surrounding whitespace and processed to lowercase characters. An if/elif/else statement is then used to evaluate the user input. If the username length is less that one character or the username is greater than twenty characters the user is informed that their input is either too long or too short and the loop repeats. The characters of the user input are then looped through. If the characters are all alphanumeric and/or contain spaces the global username variable is updated to the user name input value using the global statement and stripped of excess whitespace using " ".join(name.split()) with the first letter of each word capitalised using .title(). The break statement is also used to break out of the loop. If the name input doesn't satisfy any of the previous conditions then it must contain either a symbol or a number. The final elif statement loops through the characters in the user input name again and checks if they are digits. If any of them are the user is informed that the name cannot contain a number and the loop is repeated. Finally the else statement informs the user that the name cannot contain a symbol and the loop is repeated.

![Process Name Function](readme-images/process-name-function.png)

[Back to top](<#contents>)

### Chapter Functions

There are five chapter functions which are defined in the run.py module. The functions are normally called after a user makes a correct riddle choice. Chapter functions begin by using the typewriter effect to print one or more  variables from the storyboard module to the terminal. The user is then presented with a navigational choice which is a if/elif/else statement wrapped in a while loop. A valid user choice breaks the user out of the loop and calls the next function. The user is also given the option to exit the labyrinth/program at each navigational choice.

![Chapter Function](readme-images/chapter-function.png)

![Chapter Terminal Display](readme-images/chapter-terminal.png)

[Back to top](<#contents>)

### Riddle Functions

There are six riddles and six riddle functions in the Labyrinth of Riddles. The riddle functions are usually called by making a correct navigational choice. The main purpose of the riddle functions is to assign new riddle variables and then call and pass the riddle me this function the variables as arguments. They are also used to print storyboard text elements to the terminal. Variables assigned with the riddle functions are the riddle question dictionary location, the riddle answer dictionary location, the next path which calls the function that the user navigates to when the riddle is answered correctly and an alternative answer to the riddle.

![Riddle Functions](readme-images/riddle-functions.png)

[Back to top](<#contents>)

### Riddle Me This Function

The riddle me this function is the function used for each riddle section of the program. It is passed four arguments from the riddle functions - riddle_question, riddle_answer, next_path and alt_answer. The function is defined in the run.py module. The function first loops through the riddle_question string from the assigned riddle dictionary and uses the typewriter effect to print each character individually to the terminal. Then a variable called guesses is assigned the value of 3. A while loop is then defined which prints the users number of available guesses assigned to the guesses variable to the terminal. The user is also reminded that they can exit the labyrinth/program by typing "exit" into the input. The user is then prompted to make a guess at the answer to the riddle with an input. An if/elif/else statement is then defined to check if the user input matches a number of different answers. If the user choice matches the riddle_answer or alt_answer variables the user is correct and the break statement is used to break the user out of the loop. The next_path variable function is also called to send the user to the next function. The user input is also tested for the exit command which triggers the exit function. If the user input that doesn't match either the if or elif options the else statement is triggered and the guesses variable is decreased by the value of 1. Another if/else statement is then defined to check if the guesses variable is equal to zero. If the guesses variable is equal to zero this means the user has run out of guesses and the you_die function is called along with a break statement. Otherwise the user is advised that they guessed incorrectly and the loop repeats. 

![Riddle Me This Function](readme-images/riddle-me-this-function.png)

![Riddle Terminal Display](readme-images/riddle-two.png)

[Back to top](<#contents>)

### Door Riddle Function

The door riddle function is a larger function which features multiple nested if/elif/else statements. The purpose of this function is to provide the user with a new interesting challenge, which the user interacts with slightly differently in comparison to the riddle functions. The door riddle is based on a famous riddle which features in the [Labyrinth](https://www.imdb.com/title/tt0091369/) movie. First an available_questions variable is assigned the value of 1. Then a while loop is defined which checks if the value of the available_questions variable is 1. If it is the user is given the choice of whether to choose a door, ask a question, or exit the labyrinth/program. If the user chooses the door option they are given a choice of the left or right door. Choosing the left door is the correct option and breaks the loop and calls the fourth_riddle function. Choosing the right door calls the right_door function and also breaks the loop. Invalid input from the user repeats the door option loop until the user enters a valid option. If the user chooses the ask option instead of door the storyboard variable which_question is printed using the typewriter effect to the terminal which displays four question options to ask. Another while loop is defined with a user input asking the user which question they would like to ask. An if/elif/else statement is then defined to check user input to match with one of the four questions. If user input doesn't match the loop repeats itself until a valid input is obtained. If a valid input is entered by the user the answer to the matching question is printed to the terminal and the available_questions variable is decreased by the value of 1 making it 0. The nested loop is then broken out of using the break statement and the user is returned to the orginal loop. The value of the variable available_questions is tested, and if it does not equal 1 the user is then sent directly to the else statement which prompts the user to pick a door without the option to ask a question as they have already asked their one question. This else statement features another nested if/elif/else statement which functions exactly the same as if the user decided to choose a door before asking a question. 

![Door Riddle Function Part One](readme-images/door-riddle-one.png)

![Door Riddle Function Part Two](readme-images/door-riddle-two.png)

![Door Riddle Terminal Display Part One](readme-images/door-riddle-terminal.png)

![Door Riddle Terminal Display Part Two](readme-images/door-riddle-terminal-two.png)

[Back to top](<#contents>)

### Play Again Function

The play again function is defined on the run.py module. It is called when a player character dies or when the you_die function is called after failing a riddle challenge. The purpose of this function is to give the user an option to restart the game or quit the program. The function features a while loop which displays the question to the user of whether they would like to play again or not. The while loop contains an if/elif/else statement which checks the users input and either calls the begin_labyrinth function and breaks out of the loop, prints a goodbye message and calls the quit function or displays an invalid input message and repeats the loop. The loop repeats until a valid input is received from the user.

![Play Again Function](readme-images/play-again-function.png)

![Play Again Terminal Display](readme-images/play-again-terminal.png)

[Back to top](<#contents>)

### Exit Function

The exit function is called whenever a user enters the exit command into the terminal input. The purpose of this function is to provide the user with a visual reminder that they will lose their progress if they exit. The user is then given an opportunity to confirm their choice or return back to their previous position in the game. The function features a while loop with a nested if/elif/else statement. Confirming the exit will print a small goodbye message and quit the program. Invalid input will print a small invalid input message to the terminal and repeat the loop. If the user decides to return back the break statement is used to break out of the while loop and return to the previous function.

![Exit Function](readme-images/exit-function.png)

![Exit Terminal Display](readme-images/exit-terminal.png)

[Back to top](<#contents>)

### Go Back 

The go back function is called when a user reaches a dead end in the labyrinth. The purpose of this function is to give the user the choice to return back to their previous junction or exit the program/labyrinth. The function features a while loop with a nested if/elif/else statement. The user is asked whether they wish to return back or exit the labyrinth. Their input is processed and checked for a match against the two options and if no match is found an invalid input statement is printed to the terminal and the loop repeats until a valid user input is received. If the user chooses to go back, a small section of text is printed using the typewriter effect to the terminal and the loop is broken out of using the break statement. This returns the user to the previous function loop choice. If the user chooses to exit the program the exit function is called.

![Go Back Function](readme-images/go-back-function.png)

![Go Back Terminal Display](readme-images/go-back-terminal.png)

[Back to top](<#contents>)

### You Die Function

The you die function is called when a user runs out of guesses in the riddle challenges. The function prints the storyboard variable final_words using the typewriter effect to the terminal and then calls the play_again function to give the user the option to play again from the beginning. 

![You Die Function](readme-images/you-die-function.png)

![You Die Terminal Display](readme-images/you-die-terminal.png)

[Back to top](<#contents>)

### End Function

The end function is called when the user answers the final riddle correctly. The purpose of the end function is to print the final storyboard paragraph and give the user their final choice before concluding the game. This function also features a while loop with a nested if/elif/else statement. The user is given the option to take or leave the treasure. Taking the treasure calls the take_treasure function and breaks out of the loop. Leaving the treasure calls the leave function and breaks out of the loop. If the user input is invalid a please try again statement is printed to the terminal and the loop repeats. 

![End Function](readme-images/end-function.png)

![End Terminal Display](readme-images/end-terminal.png)

[Back to top](<#contents>)

### Multiple Endings

There are two possible endings at the end of the program after the end function is called. These endings are defined using the functions of take_treasure and leave. Both of these functions print their individual storyboard elements to the terminal using the typewriter effect and then call the play_again function to give the user the option to play again or quit the game/program. Multiple endings were added to enhance game replayability and the user overall experience. The endings also round off the narrative nicely and provide a good moral to the story.

![Ending Functions](readme-images/ending-functions.png)

![Take Treasure Terminal Display](readme-images/take-treasure-terminal.png)

![Leave Terminal Display](readme-images/leave-terminal.png)

[Back to top](<#contents>)

## Future Features

The Labyrinth of Riddles has many potential areas for future improvements/features.

* The labyrinth navigational elements could be randomized in a list which is shuffled for each playthrough so the correct labyrinth path is different each time. This could help improve replayability with users. 
* The trap locations and deaths could also be randomized to be triggered by different choices on each playthrough. This would also increase game difficulty on repeated playthroughs.  
* More riddles could be added to the riddle list and these could also be shuffled to be different on each user playthrough.
* The labyrinth could be extended to be larger with more choices and riddles. There could also be a new feature to allow a user to continue from a checkpoint using a code if their character dies or they exit the game.
* More possible alternate endings could be added based on user choices. Game narrative could be developed to make earlier user choices drastically effect the final outcome.
* The labyrinth could feature different settings for difficulty for less advanced users. Easier settings could reduce the size of the labyrinth and the difficulty of the riddles for novice or younger players.
* A leaderboard section could be implemented where users enter their name upon completion of the labyrinth. This section could also record the number of deaths before completion and whether the user became a riddler or not.

[Back to top](<#contents>)

# Technologies Used

* [Python](https://www.python.org/) - Python is a high level, general-purpose programming language. Used for all project functionality.
* [Heroku](https://www.heroku.com) - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud. Used to host the functioning application.
* [GitPod](https://gitpod.io/) - An open source developer platform for remote development. Used to edit and build the program.
* [GitHub](https://github.com/) - An online host for web and software development projects. Used to store the repository. Linked to Heroku for automatic deployement with new commits.
* [Git](https://git-scm.com/) - Software for tracking changes to files. Used with GitPod to add, commit and push code changes to the repository on GitHub. 
* [Apple Notes](https://www.icloud.com/notes) - A simple Apple app used to write and plan storyboard elements and content for the program.
* [Slack](https://www.icloud.com/notes) - An online messaging program designed for workplace collaboration. Used for advice and guidance from peers and tutors. 

[Back to top](<#contents>)

# Testing

The Labyrinth of Riddles has been tested extensively for bugs and errors throughout the development process.

## Validator Tests

All the Python code for each module included in this project has been passed through the [PEP8 online python validator tester](http://pep8online.com/). No errors were shown.

![Run.py Module Validator Test](readme-images/run-validator-test.png)

![Riddles.py Module Validator Test](readme-images/riddles-validator-test.png)

![Storyboard.py Module Validator Test](readme-images/storyboard-validator-test.png)

![Title.py Module Validator Test](readme-images/title-validator-test.png)

[Back to top](<#contents>)

## Terminal Tests

The Labyrinth of Riddles program has been tested extensively in the local terminal on GitPod and through the code insitute Heroku terminal. No errors in layout or functionality were found.

![Terminal Test](readme-images/terminal-test.png)

[Back to top](<#contents>)

## Input Validation Tests

The Labyrinth of Riddles program has been tested extensively to check for user input validation errors. All inputs have been tested for uppercase, lowercase and surrounding whitespace characters with no bugs or errors detected. All user data inputs are processed and evaluated logically and effectively. Invalid inputs are detected and processed accordingly for every user input.

[Back to top](<#contents>)

## Bugs

### Resolved 

* In the early to mid stages of development all the large text elements, the riddles and the title were being run directly from the run.py module. This quickly became very unwieldy to organise because of the line character limit. The code became very difficult to read and edit. Consequently the title, storyboard text elements and riddles were all moved into their own python modules. These modules were then imported into the run.py module for use. This helped relieve some of messiness and clutter in the run.py module.
* In the early stages of the project development there was no riddle me this function. Each riddle had a separate riddle function with all the text elements being added in manually from the run.py module. This was not an effective way of running the program so the separate code was condensed into one singular function which is passed variables as arguments for each riddle. This helped to cut down on the amount of excess code significantly. The riddles were also placed within a list of dictionaries to make access and organisation easier.
* During the development process there were many bugs caused by indentation and line limit issues. To resolve this line breaks had to be added frequently to keep the amount of characters on each line within the limit. This also created some confusion with the indentation on the next line following a line break. Lines were being indented following a line break when they should not have been. This was simply resolved by removing the excess whitespace.
* A bug also presented itself during development of the while loops in conjunction with the if/elif/else statements. In the early stages when a function was called from the if statement, the loop would also continue simultaneously. This was not the intended outcome. This bug created a continueous loop which the user could not escape from. This was resolved by breaking out of the loop using the frequent use of the break statement in the appropriate places.

[Back to top](<#contents>)

### Unresolved

* There is one unfortunate bug that hasn't been resolved. During the final stages of testing it was discovered that if a user types with the keyboard while the typewriter is printing storyboard elements to the terminal, the user characters appear in the terminal along with the printed text. These characters are then added into the user's next input choice, which is then processed by the program and could consequently lead to a correct user answer being evaluated as incorrect. To resolve this a function needs to be created to block user keyboard input while storyboard elements are being printed. Multiple potential solutions were trialled and tested but unfortunately, no easy fixes were found.

[Back to top](<#contents>)

# Deployment

## Project Deployment via Heroku

This is a guide on how to deploy a project via [Heroku](https://www.heroku.com). 

1. Type "pip3 freeze > requirements.txt" into the terminal command line to create a list of dependencies in the requirements.txt file for heroku to intall before starting the application.
2. Add, commit and push changes up to GitHub.
3. Open [Heroku](https://www.heroku.com) on the web browser and login or create an account.
4. Once the account is open/created, click the "New" button in the top right hand corner and then click "Create new app" from the dropdown menu.

![Heroku Deployment Create New App](readme-images/heroku-deployment-one.png)

5. Enter an app name (this has to be unique on Heroku) and choose the local region in the dropdown box below. Then click the "Create app" button.

![Heroku Deployment Choose Name and Region](readme-images/heroku-deployment-two.png)

6. When the app dashboard is open click the "Settings" tab in the menu bar. Scroll down to the "Config Vars" section and click the "Reavel Config Vars" button. Any sensitive information not sent to GitHub, that is required for the running of the app, must be entered manually in this section. Any protected .json files need to be entered here. Go back to the project and copy all the data in the .json file. Paste the data into the "Value" field. In the "Key" field enter "CREDS" in all capitals. Then click the "Add" button.
7. For projects using the Code Institute terminal, another Config Var needs to be added into this section. Enter "PORT" in all capitals into the "Key" field and "8000" into the "Value" field and click the "Add" button.

![Heroku Deployment Enter Config Vars](readme-images/heroku-deployment-three.png)

8. For projects using Python, scroll down to the "Buildpacks" section below. Click the "Add buildpack" button and select the "Python" option from the pop up window. Click the "Save Changes" button to exit the window.
9. For projects that use the Code Insitute terminal, repeat the process and click the "Add buildpack" button again and select the "Nodejs" option from the pop up window. Click the "Save Changes" button to exit the window.
10. Check the order of the buildpacks in the buildpacks section. Ensure that Python is above Nodejs. If it isn't, click and drag the Python bar using the three line icons until it is top of the list.

![Heroku Deployment Enter Buildpacks](readme-images/heroku-deployment-four.png)

11. Scroll up to the top of the page and click the "Deploy" tab on the main app menu. 
12. When the deployment page opens, scroll down to the "Deployment method" section and click and select the "GitHub" option to connect Heroku to the repository on GitHub. Scroll down and click the "Connect to GitHub" button. Log into GitHub in the pop-up window if required, otherwise this should be done automatically.

![Heroku Deployment Connect to GitHub](readme-images/heroku-deployment-five.png)

13. In the "Connect to GitHub" section enter the repository name into the repo-name field and click the "Search" button. The repository name should appear below the field. Click the "Connect" button to connect the GitHub repository to Heroku.

![Heroku Deployment Successfully Connected to GitHub](readme-images/heroku-deployment-six.png)

14. If the last step was successful the "Deploy" page should change. Scroll down the page to the "Automatic deploys" and "Manual deploy" sections. To enable automatic deploys with each new GitHub push click the "Enable Automatic Deploys" button. To manually deploy click the "Deploy branch" button in the "Manual deploy" section. Ensure the "main"/"master" branch is selected from the drop down menus for both of these options if that is the latest branch of the project.

![Heroku Deployment Manual or Automatic Deployment](readme-images/heroku-deployment-seven.png)

15. If deployment is successful a prompt should appear with a "View" button to view the deployed app. Click the button to view the app deployment.

[Back to top](<#contents>)

# Credits

In this section the various sources of code, content and tutorials for The Labyrinth of Riddles will be acknowledged and credited.

## Content

* Parts of the storyboard narrative in the Labyrinth of Riddles was inspired by the [Labyrinth](https://www.imdb.com/title/tt0091369/) movie.
* The Labyrinth structure was planned using an image from [Difference Between](http://www.differencebetween.info/difference-between-maze-and-labyrinth).
* Riddle content was sourced from [Parade](https://parade.com/947956/parade/riddles/), [Readers Digest](https://www.rd.com/article/riddles-for-adults/) and [Womans Day](https://www.womansday.com/life/entertainment/a39225370/riddles-for-adults/). 

[Back to top](<#contents>)

## Media

* The Labyrinth of Riddles ASCII word-art title is a font called ANSI Shadow from [Patorjk](http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20). 

[Back to top](<#contents>)

## Code 

* The typewriter effect code was acquired from [Stack Overflow](https://stackoverflow.com/questions/20302331/typing-effect-in-python).

[Back to top](<#contents>)

# Acknowledgements

The Labyrinth of Riddles is the third project submission for the [Code Institute](https://codeinstitute.net/) Higher National Diploma of Full Stack Software Development. The project focusses purely on back-end functionality with the Python programming language. I thoroughly enjoyed learning how to use Python to implement back-end data input processing into a basic program. I am very much looking forward to being able to tie together all the languages I have learnt in the previous modules to build a full stack application for my next project. 

I'd like to say a big thank you to my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for his feedback and guidance throughout this project. 

I would also like to thank the Code Institute Slack community, specifically the class of May 2022 for their support and feedback. Thank you to the Code Institute student care team and the tutor assistance. 

Next I will be building a full stack application. I'm excited to rise to the challenge and continue working on my skills as a developer!

Happy coding!

Matthew Hobbs-Hurrell

[Back to top](<#contents>)