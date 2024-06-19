import random

#list of random words
word_list = ["grapes","mango","watermelon","orange","banana"]

guess = input("Enter a single letter: ")


#checking for valid input
def ask_for_input():
    while True:
        if len(guess) == 1 & guess.isalpha() :
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character")
            guess = input("Enter a single letter: ")

    check_guess(guess)



#checks which words contain the letter we guessed from the input
def check_guess(guess):
    guess.lower()

    words_with_letter = [word for word in word_list if guess in word]
    #print(words_with_letter)

    if words_with_letter:
        for word in words_with_letter:
        #for word in words_with_letter:
            print(f'Good guess! {guess} is in the word')
            break
            
    else:
        print(f'Sorry, {guess} is not in the word')



ask_for_input()
