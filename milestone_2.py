import random

#list of random words
word_list = ["grapes","mango","watermelon","orange","banana"]
print(word_list)

word = random.choice(word_list)
print(word)

#user guess
guess = input("Enter a single letter: ")

if len(guess) == 1 & guess.isalpha() :
    print("Good guess")
else:
    print("Oops! That is not a valid input")