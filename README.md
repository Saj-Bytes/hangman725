# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


## Usage instructions
- You can guess one letter at a time.

## milestone_2.py
- there are 2 functions in this project

### 1st function: 'ask_for_input()
- this asks the user for input and checks to see if it is valid
    - i.e. if it is a single letter and is a letter from the alphabet
- this is a while loop that continues going until the user enters some valid input 

### 2nd function: 'check_guess()'
- this matches the users guess with the possible words
- if the letter chosen is in any of the words, it will return the letter and say it was a good guess
- otherwise it will say the chosen letter was not in the word

---
## File structure of the project
+ milestone_2.py
- this is just a file that gets user input
- and checks to see if it is valid
---

## milestone_3.py
- here we do the same as above, but also continue checking until the input is valid
- also checks if the letter is in the word 

## milestone_3_2.py
- here we use functions to make it more concise

---
## milestone_4.py
- In this file we create a Hangman class 

This class has the following methods:
### '__init__ method' - Used to initialise an instance from the Hangman class 
    + attributes used to initalise class
        - 'word_list' - we initialise the class by passing in a list; which is the different words that can be selected for the game
        - 'num_lives' - this is the number of lives and chances the user has to select the right characters - by default it is set to 5
    
    + Other attributes in this class
        - 'word' - this uses the random function to select a random word from the 'word_list' attribute passed into the function
        - 'word_guessed' - this converts the letters in the attribute 'word' to all '_' so we can play the game
        - 'num_letters' - this is the number of unique letters in the word that have not been guessed yet - default value of 0
        - 'list_of_guesses' - this is a list of the guesses that have already been tried 


### 'check_guess method' - checks to see if the letter we guess is valid and if it is in the word 
- 'guess' - takes this attribute as a parameter in this method

#### What does this method do? 
- converts this 'guess' into lowercase 
- checks to see if the 'guess' is in the 'word' attribute
- checks to see which letters are in the 'word' from our 'guess' and stores this in an attribute called 'words_with_letter'
- then if 'words_with_letter' is not empty, for every letter in the word, if we guess correctly, it finds the index position of the letter
- then replaces the '_' in the 'word_guessed' attribute with the letter we chose in 'guess' 
- it then reduces the attribute 'num_letters' by 1 and prints a message saying it was a good guess
- if we don't guess correctly, it reduces the 'num_lives' by 1 and print a message saying it was not a good guess and prints the new 'num_lives' left


### ask_for_input() - asks user to take a guess

#### What does this method do?
- 'Guess' - Continuously asks the user for input, asking the user to enter a single letter - this is store as the 'guess' attribute
- Performs some checks on the 'guess' 
    - checks to see if it is valid ; only valid if it is one letter and is from the alphabet
        -  if not valid, it prints a message saying letter chosen is invalid
    - checks to see if we have already guessed this letter
        - uses the 'list_of_guesses' to check if the 'guess' is a part of this list
    - if all checks are fine, it runs the check_guess() method on the guess 
        - after running this method it adds the 'guess' to the 'list_of_guesses' list 


## How to call the function
- Create a list of words 
- Then you can create an instance of the Hangman class and parse in the list
- Call the ask_for_input() method on this instance

---
## milestone_5.py
- In this file we create a function 'play_game' in order to play the game
- We also made some changes to the original milestone_4.py file for the hangman class

### Changes made to milestone_4.py
+ ask_for_input() method
    - Removed the while loop as it was infinitely looping
    - added another elif condition that checked for no user input i.e. "" empty string and print invalid message


### play_game function
What does this function do?
- This method takes a list 'word_list' as a parameter and instantiates a Hangman object from the Hangman Class
- It then runs through a loop checking certain conditions
    + if the number of lives is 0, it breaks out the loop and prints a message
    + if the number of letters is more than 0, it calls the ask_for_input() method from the Hangman class to ask user for input
    + otherwise if the 'num_lives' attribute is 0 and the 'num_letters' attribute is less than 0, it breaks out the loop and prints a message saying the user has won.

### How to use the function
- create a list of chosen words for the game
- parse this list into the play_game() function
