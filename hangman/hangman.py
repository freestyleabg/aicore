import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has

    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_guesses: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(guess)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        self.guess = None
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_" for element in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The letter to be checked
        '''
        self.guess = guess
        found = False
        if guess.lower() in self.word.lower():
            for index, letter in enumerate(self.word):
                if letter == guess:
                    found = True
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        if found:
            print(f"Good guess! {guess} is in the word.")
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_guess method.
        '''
        while True:
            guess = input("Enter a single letter: ").lower()
            if guess.isalpha() and len(guess) == 1 and guess not in self.list_of_guesses:
                break
            elif not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

        self.check_guess(guess)
        self.list_of_guesses.append(guess)


def play_game(word_list_entry):
    num_lives = 5
    game = Hangman(word_list_entry, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon', 'mango']
    play_game(word_list)
