import random

options = ['rock', 'paper', 'scissors']
# cpu_choice = random.randint(1, 3)
# print("Options: ")
# [print(f"{i}: {j.capitalize()}") for i, j in enumerate(options, 1)]
# user_choice = int(input("Enter the number corresponding to your choice: "))

def get_cpu_choice():
    cpu_choice = random.randint(1, 3)
    return cpu_choice

def get_user_choice():
    print("Options: ")
    [print(f"{i}: {j.capitalize()}") for i, j in enumerate(options, 1)]
    user_choice = int(input("Enter the number corresponding to your choice: "))
    return user_choice

def get_winner():
    if user_choice > cpu_choice and user_choice != 3:
        print("You win!")
    elif user_choice == cpu_choice:
        print("It's a draw!")
    else:
        print("You lose.")


cpu_choice = get_cpu_choice()
user_choice = get_user_choice()
print(f"User: {options[user_choice].capitalize()}, CPU: {options[cpu_choice].capitalize()}")
get_winner()
