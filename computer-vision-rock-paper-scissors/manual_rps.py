import random


# options = ['rock', 'paper', 'scissors']
# cpu_choice = random.randint(1, 3)
# print("Options: ")
# [print(f"{i}: {j.capitalize()}") for i, j in enumerate(options, 1)]
# user_choice = int(input("Enter the number corresponding to your choice: "))

class RockPaperScissors:
    def __init__(self, num_wins=0):
        self.num_wins = num_wins
        self.cpu_choice = None
        self.user_choice = None
        self.options = ['rock', 'paper', 'scissors']

    def get_cpu_choice(self):
        self.cpu_choice = random.randint(1, 3)

    def get_user_choice(self):
        print("Options: ")
        [print(f"{i}: {j.capitalize()}") for i, j in enumerate(self.options, 1)]
        self.user_choice = int(input("Enter the number corresponding to your choice: "))

    def get_winner(self):
        if self.user_choice > self.cpu_choice and self.user_choice != 3:
            print("You win!")
        elif self.user_choice == self.cpu_choice:
            print("It's a draw!")
        else:
            print("You lose.")

    def play(self):
        self.get_cpu_choice()
        self.get_user_choice()
        self.get_winner()
        print(f"User: {self.options[self.user_choice-1].capitalize()}, CPU: {self.options[self.cpu_choice-1].capitalize()}")


p = RockPaperScissors()
p.play()