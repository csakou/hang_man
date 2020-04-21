#!/home/csakou/Documents/Python/hang_man/venv/bin/python3
import random

class Player:
    def __init__(self):
        self.set_name()
        self._lives = 0
        print(self.name, self.lives)

    def set_name(self):
        print("Hello player. Please enter your name. It must have 1-16 characters:")
        while True:
            try:
                self.name = input("> ")
                if len(self.name) <= 0 or len(self.name) >16:
                    raise ValueError
                break
            except ValueError:
                print("Your name must be in between 1-16 characters:")

    def set_lives(self, lives):
        self._lives = lives

    def get_name(self):
        return self.name

    def get_lives(self):
        return self._lives

    def __new__(self):
        return self

if __name__ == "__main__":
    player = Player()