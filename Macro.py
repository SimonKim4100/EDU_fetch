from pynput.keyboard import Controller, Key
import time
import random

keyboard = Controller()


def human_like_input(keys, interval_range):
    for key in keys:
        with keyboard.pressed(key):
            time.sleep(0.1)  # Simulate key press duration
        time.sleep(0.1)  # Simulate release delay
        time.sleep(random.uniform(*interval_range))


if __name__ == "__main__":
    keys_to_press = ["t", "j", "k"]
    time_interval_range = (9, 11)  # Random interval between 9 and 11 seconds

    time.sleep(5)
    while True:
        human_like_input(keys_to_press, time_interval_range)
