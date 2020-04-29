"""

"""

import os
import random
import string
from player import Player

class Hang_Man:
    def __init__(self):
        self.player = Player()
        self.set_word()
        self.alphabet = list(string.ascii_uppercase)
        self.player_lives = len(self.get_word())
        self.characters_used = ['']*26
        self.player_characters_found = ['_' for i in range(len(self.get_word()))]

    def set_word(self):
        try:
            with open('word_list.txt', 'r', newline='\n', encoding='utf-8') as word_list_file:
                word_list = word_list_file.read().split('\n')
                self.word = random.choice(word_list).upper()
        except LookupError:
            print('Word list file does not exist!')
            exit(1)
        finally:
            word_list_file.close()

    def update_characters_used(self, character, position):
        self.characters_used[position] = character

    def update_player_characters_found(self, character, position):
        self.player_characters_found[position] = character

    def get_word(self):
        return self.word

    def get_character_pos_in_alphabet(self, character):
        for offset, char in enumerate(self.alphabet):
            if character == char:
                return offset

    def get_player_characters_found(self):
        return self.player_characters_found

    def decrease_player_lives(self):
        self.player_lives -= 1

    def player_choice(self):
        print(f'{self.player.name}, please choose a letter of the alphabet:')
        while True:
            try:
                choice = str(input("> ")).upper()
                if len(choice) != 1 or choice.isdigit() or choice in self.characters_used:
                    raise ValueError
                return choice
            except ValueError:
                print('You must choose a letter of the alphabet you have not used:')

    def check_choice(self, choice):
        if choice in self.get_word():
            for offset, item in enumerate(self.get_word()):
                if choice == item:
                    self.update_player_characters_found(item, offset)
        else:
            self.decrease_player_lives()
        self.update_characters_used(choice, self.get_character_pos_in_alphabet(choice))

    def display_word(self):
        print(' '.join(self.get_player_characters_found()))

    def display_characters_used(self):
        characters_used = [i for i in self.characters_used if i in list(string.ascii_uppercase)]
        print(''.join(characters_used))

    def display_lives(self):
        print('Lives left: {}'.format('#'*self.player_lives))

    def update_display(self):
        os.system('clear')
        self.display_word()
        self.display_characters_used()
        self.display_lives()

    def check_state(self):
        if self.player_lives <= 0:
            print(f'Sorry {self.player.get_name()}, looks like you are out of guesses.')
            print('Better luck next time!')
            return 0
        if ''.join(self.get_player_characters_found()) == self.get_word():
            print(f'Congratulations! You have found the word "{self.get_word()}".')
            return 0
        return 1

    def play(self):
        state = 1
        print(f"Hello {self.player.get_name()}, let's play a game of Hang Man!")

        while state != 0:
            self.update_display()
            self.check_choice(self.player_choice())
            state = self.check_state()

if __name__ == '__main__':
    game = Hang_Man()
    game.play()