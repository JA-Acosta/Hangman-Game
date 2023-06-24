# JAAR
# 06/23/2023
# Hangman Game
# Version 1

'''
>>> Generates an instance of a game of hangman for the user
'''

'''
Verifies if an input is a number
'''



'''
-------------------------------------------------------------------------------
>>> main
'''

import inspect
import random

print('Lets play Hangman!')

WORD_LIST = ['one', 'three', 'four', 'seven', 'a', 'or', 'the', 'cat']
updated_word_list = []
answer = None
while answer not in WORD_LIST :
    word_length = None
    while not isinstance(word_length, int) :
        try:
            word_length = int(input('Enter a number and I will generate a word of that length: '))
        except ValueError:
            print('Your input was invalid, try again.')

    # create a new list with a word of the length in question
    for word in WORD_LIST :
        if len(word) == word_length :
            updated_word_list.append(word)
    if not len(updated_word_list) == 0 :
        answer = updated_word_list[random.randint(0, len(updated_word_list) - 1)]
    print(answer)


