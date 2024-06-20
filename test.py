import random

word_list = ["grapes","mango","watermelon","orange","banana"]

guess = input("Enter a single letter: ")


#word = random.choice(word_list)
word = "banana"

    # for guess in word:
    #     word_guess = word.replace( "_")
    #     print(word_guess)


#replace all letter with _
    # my_string = ['_ ']*len(word)
    # print(my_string)



#if letter exists in the word
# put that letter
#replace all other letters with _
result = []
for letter in word:
    if letter == guess:
        result += letter
    else:
        result += ['_']
        continue

#result = ''.join([char if char == guess else ['_ '] for char in word])
print(result)
#otherwise, replace all letter with _



