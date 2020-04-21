#!/home/csakou/Documents/Python/hang_man/venv/bin/python3
from player import Player

class Hang_Man(Player):
    def __init__(self):
        self.set_word()

    def set_word(self):
        try:
            with open('word_list.txt', 'r', newline='\n', encoding='utf-8') as word_list_file:
                word_list = word_list_file.read().split('\n')
                self.word = random.choice(word_list)
        except LookupError:
            print("Word list file does not exist!")
            exit(1)