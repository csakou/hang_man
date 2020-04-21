#!/home/csakou/Documents/Python/hang_man/venv/bin/python3

import random

class Player:
    def __init__(self):
        self.name = ""
        self.word = random.choice(open("word_list.txt").read().split("\n"))
        self.lives = len(self.word) + 3

    def set_name(self):
        while len(self.name) <= 0 or len(self.name) > 16:
            print("Hello player. Please enter your name. It must have 1-16 characters:")
            self.name = input("> ")

    def get_name(self):
        return self.name

    def get_word(self):
        return self.word

    def __new__(self):
        return self

if __name__ == "__main__":
    player = Player()
    player.set_name()
