#!/home/csakou/Documents/Python/hang_man/venv/bin/python3
import random
import string
from player import Player

class Hang_Man:
    def __init__(self, player):
        self.set_word()
        self.set_alphabet()
        self.set_player_lives()
        self.set_characters_not_in_word()

    def set_word(self):
        try:
            with open('word_list.txt', 'r', newline='\n', encoding='utf-8') as word_list_file:
                word_list = word_list_file.read().split('\n')
                self.word = random.choice(word_list).upper()
        except LookupError:
            print("Word list file does not exist!")
            exit(1)

    def set_alphabet(self):
        self.alphabet = list(string.ascii_uppercase)

    def set_player_lives(self):
        self.player_lives = self.get_word_length()

    def set_characters_not_in_word(self):
        self.characters_not_in_word = ['_']*24

    def update_characters_not_in_word(self, character, position):
        self.characters_not_in_word[position] = character

    def get_word(self):
        return self.word

    def get_alphabet(self):
        return self.alphabet

    def get_word_length(self):
        return len(self.get_word())

    def get_player_lives(self):
        return self.player_lives

    def get_characters_not_in_word(self):
        return self.characters_not_in_word

    def get_character_pos_in_alphabet(self, character):
        for offset, char in enumerate(self.get_alphabet()):
            if character == char:
                return offset

    def decrease_player_lives(self):
        if self.player_lives <= 0:
            print(f'I am sorry {player.get_name()}, you are out of lives. Better luck next time!')
        self.player_lives -= 1

    def check_choice(self, choice):
        if choice in self.get_word():
            for offset, item in enumerate(self.get_word()):
                if choice == item:
                    player.update_characters_found(item, offset)
        else:
            print("That letter is not in this word!")
            self.update_characters_not_in_word(choice, self.get_character_pos_in_alphabet(choice))
            self.decrease_player_lives()

    def display(self, characters_found):
        print(characters_found)

    def start(self):
        player.set_characters_found(self.get_word_length())
        print(f"Hello {player.get_name()}, let's play a game of 'Hang Man'!")

        while True:
            self.display(player.get_characters_found())
            self.display(self.get_characters_not_in_word())
            self.check_choice(player.make_choice())

    def restart(self):
        pass

    def end(self):
        pass

if __name__ == "__main__":
    player = Player()
    game = Hang_Man(player)
    game.start()