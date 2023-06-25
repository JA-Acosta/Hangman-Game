# JAAR
# 06/25/2023
# Hangman Game
# Version 1.1

'''
>>> Generates an instance of a game of hangman for the user
'''

import random

def input_length()-> int :
    word_length = None

    while not isinstance(word_length, int) or word_length < 1 :
        try:
            word_length = int(input('Enter a number and I will generate a word of that length: '))
        except ValueError:
            print('Your input was invalid, try again.')
    return word_length

'''
-------------------------------------------------------------------------------
>>> main
'''

print('Lets play Hangman!')
GUESSES_ALLOWED = 10
WORD_LIST = ['one', 'three', 'four', 'seven', 'a', 'or', 'the', 'cat']
updated_word_list = []
answer = None

while answer not in WORD_LIST :
    word_length = input_length()

    for word in WORD_LIST :
        if len(word) == word_length :
            updated_word_list.append(word)

    if not len(updated_word_list) == 0 :
        answer = updated_word_list[random.randint(0, len(updated_word_list) - 1)]

    answer_char_list = list(answer)
    blank_word = []

    # TODO: convert to a lambda
    for char in answer :
        blank_word.append('_')

    print(answer)
    print(*blank_word)

guesses_used = 0

while answer_char_list != blank_word and guesses_used < GUESSES_ALLOWED :
    guess = "Guess"

    while len(guess) != 1 or (len(guess) == 1 and not guess.isalpha()) :
        guess = input('Enter a guess: ')

    if guess in answer :
        blank_word[answer.index(guess)] = guess
    else :
        guesses_used += 1
        print(f'You have {GUESSES_ALLOWED - guesses_used} guesses left!')

    if answer_char_list == blank_word :
        print(f'Congratulation! You got it right with {GUESSES_ALLOWED - guesses_used} guesses remaining')
        print(f'The answer was: {answer}')
    else:
        print(*blank_word)