# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


##A description of the project: what it does, the aim of the project, and what you learned


##Installation instructions


##Usage instructions
- You can guess one letter at a time.

- there are 2 functions in this projects
+ 1st function: 'ask_for_input()
- this asks the user for input and checks to see if it is valid
    - i.e. if it is a single letter and is a letter from the alphabet
- this is a while loop that continues going until the user enters some valid input 

+ 2nd function: 'check_guess()'
- this matches the users guess with the possible words
- if the letter chosen is in any of the words, it will return the letter and say it was a good guess
- otherwise it will say the chosen letter was not in the word


##File structure of the project
+ milestone_2.py
- this is just a file that gets user input
- and checks to see if it is valid

+ milestone_3.py
- here we do the same as above, but also continue checking until the input is valid
- also checks if the letter is in the word 

+ milestone_3_2.py
- here we use functions to make it more concise