import random

class Hangman:

    def __init__(self, word_list, num_lives = 5):
        #attributes
        self.word_list = word_list #a list of words
        self.num_lives = num_lives #no of lives the player has at the start of the game 

        #other attributes
        self.word = random.choice(word_list) #random word choice from the word list
        self.word_guessed = ['_']*len(self.word)   #list of letters of all the words - convert letters in chosen word to _
        


        self.num_letters = 0 #no of unique letters in the word that have not been guessed yet
        self.list_of_guesses = [] #list of the guesses that have already been tried 


   
    #check to see if guess is in the word
    
    def check_guess(self, guess):
        guess.lower()

        words_with_letter = [w for w in self.word_list if guess in self.word]


        if words_with_letter:
            for letter in self.word:
                if letter == self.guess:
                    pos_of_letter = self.word.find(letter) #finds the index position of the letter
                    self.word_guessed[pos_of_letter] = letter #replaces the _ in words_guessed with the letter
                
            self.num_letters -= 1
            #for word in words_with_letter:
            print(f'Good guess! {guess} is in the word')
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word')
            print(f'You have {self.num_lives} lives left')
           



    def ask_for_input(self):
        while True:
            self.guess = input("Enter a single letter: ") #asks user for input
           
            #checks to see if it is valid
            if not (len(self.guess) == 1 & self.guess.isalpha()) :
                print("Invalid letter. Please, enter a single alphabetical character")
            elif self.guess in self.list_of_guesses:
                 print("You already tried that letter!")
            else:
                self.check_guess(self.guess)
                self.list_of_guesses += self.guess


list1 = ['apple', 'banana', 'cherry']
testing = Hangman(list1)


testing.ask_for_input()






        



# #method to check
