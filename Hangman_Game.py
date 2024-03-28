'''
>>> Author: JAAR
>>> Date: 03/27/2024
>>> Program: Hangman Game
>>> Version 1.2
'''

'''
>>> Generates an instance of a game of hangman for the player. A word is selected at random from a dictionary based on size inputted by the player. If there isn't a word of that size in the dictionary, the player will be prompted for another length.
>>> The Players win/loss ratio will be tracked and the percent wins will be given after all games conclude.
'''

import random

'''
>>> Asks the user for an input and then verifies the input was an integer. Afterwards collects all words of that length from the dictionary. A random word is then selected from the list to be used as the answer for the current game.
Return: str

>>> Update: Returns string representing the answer for hangman game. Gets answer from a file with words in plain text.
'''
def get_word()-> str :
    list = []
    while not list :
        try:
            # Gets a length for a word
            word_length = int(input('Enter a number and I will generate a word of that length: '))

            # Checks if the Dictionary contains a word of that length.
            with open("Dictionary", 'r') as file :
                data = file.read()
                list = [word for word in data.split() if len(word) == word_length]

            if len(list) == 0 :
                raise TypeError

        except ValueError :
            print('Your input was invalid, try again.')
            continue
        except TypeError :
            print('No word in the dictionary exist with that size.')

    # get a random word from the list.
    return list[random.randint(0, len(list) - 1)]

'''
-------------------------------------------------------------------------------
>>> main
'''
print('Lets play Hangman!')
GUESSES_ALLOWED = 10
response = 'yes'
results = [] # TODO: Results isn't in use yet; at the end of each game. Update to have either a win or loss represented in the results.

while response == 'yes':
    response = None
    guesses_used = 0 # resets guesses used.
    guessed_letters = [] # Update: Contains a list of all letters already used.
    answer = list(get_word()) # Update: Uses list for answer vs str.
    print(*answer)
    blank_word = [ "_" for _ in enumerate(answer)] # Update: Uses pythonic syntax to fill in blank word.
    print(*blank_word)

    while answer != blank_word and guesses_used < GUESSES_ALLOWED :
        guess = ""
        # Checks to see if the length of the input is 1 and if it's alphabetical.
        while len(guess) != 1 or (len(guess) == 1 and not guess.isalpha()) :
            guess = input('Enter a guess: ').lower()

        # Update: Check if the guess was already used and prompts error if so. Otherwise, adds the guess to the list of guesses used.
        if guess in guessed_letters :
            print("You've already entered that letter!")
            continue
        else :
            guessed_letters.append(guess)

        # Checks to see if the input is an answer key and updates the guess counter as needed.
        if guess in answer :
            for index, char in enumerate(answer) :
                if char == guess :
                    blank_word[index] = guess
        else :
            guesses_used += 1
            print(f'You have {GUESSES_ALLOWED - guesses_used} guesses left!')

        if answer == blank_word :
            print(f'Congratulation! You got it right with {GUESSES_ALLOWED - guesses_used} guesses remaining')
            print(f'The answer was: {"".join(answer)}')
        elif guesses_used == 10 : # Update: Displays a different output when the player looses.
            print(f'You\'ve used all {GUESSES_ALLOWED}! The answer was {"".join(answer)}.')
        else:
            print(*blank_word)

    while response != 'yes' and response != 'no' :
        response = input('Do you want to play again?: ').lower()

    # TODO: Once the games end, will show the user their final scores. How many they got right and wrong.
