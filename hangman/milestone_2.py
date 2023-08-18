import random

word_list = ["mangoes", "bananas", "grapes", "strawberries", "apples"]
word = random.choice(word_list)
def check_guess(guess):
    if guess.lower() in word.lower():
        print(f"Good guess! '{guess.upper()}' is in the word.")
    else:
        print(f"Sorry, '{guess.upper()}' is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Enter a single letter: ")
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()