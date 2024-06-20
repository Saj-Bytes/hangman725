import random 
from milestone_4 import Hangman

#Function that takes 'word_list' as a parameter
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives= num_lives)
        
    while True:
        if num_lives == 0:
            print("You Lost!")
            break
        if game.num_letters>0:
            game.ask_for_input()
        if not (num_lives==0 & game.num_letters>0):
            print("Congratulations. You won the game!")
            



list2 = ['apple', 'banana', 'cherry']
play_game(list2)