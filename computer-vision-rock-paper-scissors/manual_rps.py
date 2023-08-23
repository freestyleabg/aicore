import random
import time


class RockPaperScissors:
    def __init__(self, num_wins=0, num_loss=0):
        self.num_wins = num_wins
        self.num_loss = num_loss
        self.cpu_choice = None
        self.user_choice = None
        self.options = ['rock', 'paper', 'scissors']

    def get_cpu_choice(self):
        self.cpu_choice = random.randint(1, 3)

    def get_user_choice(self):
        print("\nOptions: ")
        [print(f"{i}: {j.capitalize()}") for i, j in enumerate(self.options, 1)]
        self.user_choice = int(input("Enter the number corresponding to your choice: "))

    def get_winner(self):
        if self.user_choice > self.cpu_choice and self.user_choice != 3:
            print("You win!")
            self.num_wins += 1
        elif self.user_choice == self.cpu_choice:
            print("It's a draw!")
        else:
            print("You lose.")
            self.num_loss += 1
        print(f"Wins: {self.num_wins}, Losses: {self.num_loss}")


def play():
    num_wins = 0
    num_loss = 0
    game = RockPaperScissors(num_wins, num_loss)
    while True:
        game.get_cpu_choice()
        game.get_user_choice()
        print(f"User: {game.options[game.user_choice-1].capitalize()}, CPU: {game.options[game.cpu_choice-1].capitalize()}")
        game.get_winner()
        time.sleep(2)


play()
