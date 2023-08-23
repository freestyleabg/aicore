import random
import time
import numpy as np
import cv2
from keras.models import load_model
import keyboard

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(4)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
options = ['rock', 'paper', 'scissors', 'false reading']


class RockPaperScissors:
    def __init__(self, num_wins=0, num_loss=0):
        self.winner = None
        self.num_wins = num_wins
        self.num_loss = num_loss
        self.cpu_choice = None
        self.user_choice = int
        self.options = ['rock', 'paper', 'scissors']

    def get_cpu_choice(self):
        self.cpu_choice = random.randint(1, 3)
        return self.cpu_choice

    def get_winner(self, user_choice, cpu_choice):
        if user_choice > cpu_choice and user_choice != 3:
            self.winner = "Player"
            print("You win!")
            self.num_wins += 1
        elif user_choice == cpu_choice:
            print("It's a draw!")
        else:
            self.winner = "CPU"
            print("You lose.")
            self.num_loss += 1


def get_prediction():
    """Displays webcam, with countdown timer"""
    start_time = time.time()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame from the webcam.")
            break

        # print("Original frame shape:", frame.shape)
        resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
        # print("Resized frame shape:", resized_frame.shape)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1  # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        rounded_prediction = np.round(prediction, 2)
        print(rounded_prediction)

        # Countdown
        countdown_time = 6
        running_time = time.time() - start_time
        running_time_inverse = abs(countdown_time - running_time)
        # Draw Countdown
        countdown = cv2.putText(frame, str(round(running_time_inverse, 0)),
                                (450, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 5)
        # Show webcam
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) and running_time > countdown_time:
            break
        # # Press q to close the window
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    max_prediction = np.argmax(prediction)
    return max_prediction


def play():
    # name = input("What's your name?: ")
    print(f"Hey Andre! lets play Rock Paper Scissors")
    num_wins = 0
    num_loss = 0
    game = RockPaperScissors(num_wins, num_loss)
    play_again = True
    while play_again:
        cpu_choice = game.get_cpu_choice()
        user_choice = get_prediction() + 1
        print(f"\nTimes up! You chose {options[user_choice - 1].capitalize()}")
        if user_choice > 3:
            break
        # print(f"User: {game.options[user_choice-1].capitalize()}, CPU: {game.options[cpu_choice-1].capitalize()}")
        print(f"CPU chose {game.options[cpu_choice - 1].capitalize()}")
        game.get_winner(user_choice, cpu_choice)
        time.sleep(2)
        # Stops game if wins/losses is more than 3
        if game.num_wins >= 3 or game.num_loss >= 3:
            print(f"\n{game.winner} wins!")
            break
        else:
            print(f"\nWins: {game.num_wins}, Losses: {game.num_loss}")
            print("\nPress c to continue. Press another key to quit")
            if keyboard.read_key() == "c":
                print("You pressed 'c'.")
                play_again = True

                time.sleep(2)
            else:
                break


play()
