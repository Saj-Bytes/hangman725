import random

class Hangman:
    '''
    This class is used to represent an instance of the Game of Hangman

    Attributes:
        - 'word_list' - Takes a list of attributes as a parameter - these are the words that can be chosen
        - 'num_lives' - The number of lives the user has - default value set to 5  
        - 'word' - random word choice from the word list
        - 'word_guessed  - list of letters of all the words - converts letters in chosen word to _
        - 'num_letters = 0' - No of unique letters in the word that have not been guessed yet
        - 'list_of_guesses'  - list of the guesses that have already been tried
    '''

    def __init__(self, word_list, num_lives = 5):
        '''
        Initialisation Method

        Arguments:
            - 'word_list' - Takes a list of attributes as a parameter - these are the words that can be chosen
            - 'num_lives' - The number of lives the user has - default value set to 5  

        See help(Hangman) for more info
        '''
        
        self.word_list = word_list 
        self.num_lives = num_lives 

        #other attributes
        self.word = random.choice(word_list) 
        self.word_guessed = ['_']*len(self.word)   
        self.num_letters = len(set(self.word))
        self.list_of_guesses = [] 


    def check_guess(self, guess):
        '''
        What does the function do?
            - checks to see if the letter we guess is valid and if it is in the word 

        Arguments:
            - 'guess': the letter we guess

        Attributes/Variables:
            - 'words_with_letter' - checks to see which letters are in the 'word' from our 'guess' and stores this here
            - 'pos_of_letter' - for every letter in the word, if we guess correctly, it finds the index position of the letter

        Returns:
            - if the guess we select is in the word, prints 'good guess' message
            - otherwise prints sorry message and prints new number of lives left
        '''
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
        '''
        What does the function do?
            - Continuously asks the user for input
                - asking the user to enter a single letter 
                - Stored in the 'guess' attribute
            - Runs the check_guess() method at the end after all checks
            - Adds 'guess' to 'list_of_guesses' 

        Arguments:
            - N/A

        Attributes/Variables:
            - N/A

        Returns: 
		        - Input message to enter a single letter
                - Prints message if invalid input
                - Prints message if you have already tried that letter
                -  
        '''
        #while True:
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