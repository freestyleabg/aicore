import random
import time
import numpy as np
import cv2
from keras.models import load_model

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(4)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
options = ['rock', 'paper', 'scissors', 'false reading']

class RockPaperScissors:
    def __init__(self, num_wins=0, num_loss=0):
        self.num_wins = num_wins
        self.num_loss = num_loss
        self.cpu_choice = None
        self.user_choice = int
        self.options = ['rock', 'paper', 'scissors']

    def get_cpu_choice(self):
        self.cpu_choice = random.randint(1, 3)
        return self.cpu_choice


    def get_user_choice(self):
        print("\nOptions: ")
        [print(f"{i}: {j.capitalize()}") for i, j in enumerate(self.options, 1)]
        self.user_choice = int(input("Enter the number corresponding to your choice: "))
        return self.user_choice

    def get_winner(self, user_choice, cpu_choice):
        self.user_choice = user_choice
        self.cpu_choice = cpu_choice
        if self.user_choice > self.cpu_choice and self.user_choice != 3:
            print("You win!")
            self.num_wins += 1
        elif self.user_choice == self.cpu_choice:
            print("It's a draw!")
        else:
            print("You lose.")
            self.num_loss += 1
        print(f"Wins: {self.num_wins}, Losses: {self.num_loss}")

def get_prediction():
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame from the webcam.")
            break
        print("Original frame shape:", frame.shape)
        resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
        print("Resized frame shape:", resized_frame.shape)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1  # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        rounded_prediction = np.round(prediction, 2)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(rounded_prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    max_prediction = np.argmax(prediction)
    return max_prediction

def play():
    num_wins = 0
    num_loss = 0
    game = RockPaperScissors(num_wins, num_loss)
    play_again = True
    while play_again:
        cpu_choice = game.get_cpu_choice()
        # user_choice = game.get_user_choice()
        user_choice = get_prediction()+1
        if user_choice > 3:
            break
        print(f"User: {game.options[user_choice-1].capitalize()}, CPU: {game.options[cpu_choice-1].capitalize()}")
        game.get_winner(user_choice, cpu_choice)
        time.sleep(2)
        again = input("Again? y")
        if "y" in again:
            play_again = True
        else:
            break


play()