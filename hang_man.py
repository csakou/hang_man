#!/home/csakou/Documents/Python/hang_man/venv/bin/python3
import os
import random
import string
from player import Player


class Hang_Man:
    def __init__(self):
        self.set_word()
        self.set_alphabet()
        self.set_player_lives()
        self.set_characters_used()
        self.set_player_characters_found()

    def set_word(self):
        try:
            with open('word_list.txt', 'r', newline='\n', encoding='utf-8') as word_list_file:
                word_list = word_list_file.read().split('\n')
                self.word = random.choice(word_list).upper()
        except LookupError:
            print("Word list file does not exist!")
            exit(1)
        finally:
            word_list_file.close()

    def set_alphabet(self):
        self.alphabet = list(string.ascii_uppercase)

    def set_player_lives(self):
        self.player_lives = self.get_word_length()

    def set_characters_used(self):
        self.characters_not_in_word = ['']*26

    def update_characters_used(self, character, position):
        self.characters_not_in_word[position] = character

    def set_player_characters_found(self):
        try:
            self.player_characters_found = ['_' for i in range(self.get_word_length())]
        except Exception as e:
            print(e)

    def update_player_characters_found(self, character, position):
        try:
            self.player_characters_found[position] = character
        except Exception as e:
            print(e)

    def get_word(self):
        return self.word

    def get_alphabet(self):
        return self.alphabet

    def get_word_length(self):
        return len(self.get_word())

    def get_player_lives(self):
        return self.player_lives

    def get_characters_used(self):
        return self.characters_not_in_word

    def get_character_pos_in_alphabet(self, character):
        for offset, char in enumerate(self.get_alphabet()):
            if character == char:
                return offset

    def get_player_characters_found(self):
        return self.player_characters_found

    def decrease_player_lives(self):
        self.player_lives -= 1

    def player_choice(self):
        print(f"{player.name}, please choose a letter of the alphabet:")
        while True:
            try:
                choice = str(input("> ")).upper()
                if len(choice) != 1 or choice.isdigit():
                    raise ValueError
                return choice
            except ValueError:
                print("You must choose a letter of the alphabet:")

    def check_choice(self, choice):
        if choice in self.get_word():
            for offset, item in enumerate(self.get_word()):
                if choice == item:
                    self.update_player_characters_found(item, offset)
        else:
            print("That letter is not in this word!")
            self.decrease_player_lives()
        self.update_characters_used(choice, self.get_character_pos_in_alphabet(choice))

    def display_word(self, item):
        print('  '.join(item))

    def display_letters_used(self, item):
        print(''.join(set(item) & set(string.ascii_uppercase)))

    def clear_terminal(self):
        os.system('clear')

    def play(self):
        print(f"Hello {player.get_name()}, let's play a game of 'Hang Man'!")

        while True:
            self.display_word(self.get_player_characters_found())
            self.display_word(self.get_characters_used())
            self.check_choice(self.player_choice())
            self.clear_terminal()
            self.check_state()

    def check_state(self):
        if self.get_player_lives() <= 0:
            print(f"Sorry {player.get_name()}, looks like you are out of guesses.")
            print("Better luck next time!")
            exit()
        if ''.join(self.get_player_characters_found()) == self.get_word():
            print(f"Congratulations! You have found the word '{self.get_word()}'")
            exit()

if __name__ == "__main__":
    player = Player()
    game = Hang_Man()
    game.play()