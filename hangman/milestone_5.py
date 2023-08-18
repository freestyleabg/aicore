import random


word_list = ["mangoes", "bananas", "grapes", "strawberries", "apples"]
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.guess = None
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_" for element in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        self.guess = guess
        if guess.lower() in self.word.lower():
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[self.word.index(guess)] = guess
                    print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter: ").lower()
            if guess.isalpha() is False and len(guess) > 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif any(guess in element for element in self.list_of_guesses):
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
def play_game(word_list_entry):
    num_lives=5
    game = Hangman(word_list_entry, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives != 0 and not game.num_letters >= 1:
            print("Congratulations. You won the game!")
            break

play_game(word_list)