"""
A class to create a Hang Man game session

Attributes
-----------
player : Player
    An object created from the imported class Player to represent the player.
word : str
    A random word that the player will have to find, gotten from a word list file.
alphabet : list
    A list with all the letters of the alphabet of the current set language.
player_lives : int
    The number of lives the player has left.
letters_used : list
    A list containing the letters of the alphabet the player has already used.
player_letters_found : list
    A list representing the letters the player has found in the word.

Methods
--------

set_word()
    Opens a file that contains words and chooses one at random.
    Exits if the file doesn't exist.
update_letters_used(letter, position)
    Updates the list of the used letters of the alphabet.
update_player_letters_found()
    Updates the list containing the letters of the word the player has found.
get_word()
    Returns the word the player is currently trying to find.
get_letter_pos_in_alphabet(letter)
    Finds and returns the position of the given letter in the alphabet.
get_player_letters_found()
    Returns the list containing the letters the player has found in the word.
decrease_player_lives()
    Decrements the player lives by one.
player_choice()
    Gets players input of a letter of the alphabet.
check_choice(choice)
    Checks if the letter the player chose exists in the word in search.
display_word()
    Prints the list that contains the letters the player has found.
display_letters_used()
    Prints the letters the player has used so far.
display_lives()
    Prints the lives the player currently has.
update_display()
    Updates the terminal with the current state of the game
    (letters found, letters used and lives).
check_state()
    Checks the state of the game to see if the player has run out of lives or
    if the player has found the word.
play()
    Starts the game of hang man.
"""

import os
import sys
import random
import string
from player import Player

class Hang_Man:
    def __init__(self):
        self.player = Player()
        self.word = self.set_word()
        self.alphabet = list(string.ascii_uppercase)
        self.player_lives = len(self.get_word())
        self.letters_used = ['']*len(self.alphabet)
        self.player_letters_found = ['_' for i in range(len(self.get_word()))]

    def set_word(self):
        try:
            with open('word_list.txt', 'r', newline='\n', encoding='utf-8') as word_list_file:
                word_list = word_list_file.read().split('\n')
                word = random.choice(word_list).upper()
        except:
            print('Something went wrong with the word list file provided.')
            sys.exit(1)
        finally:
            word_list_file.close()
            return word

    def update_letters_used(self, letter, position):
        self.letters_used[position] = letter

    def update_player_letters_found(self, letter, position):
        self.player_letters_found[position] = letter

    def get_word(self):
        return self.word

    def get_letter_pos_in_alphabet(self, letter):
        for offset, char in enumerate(self.alphabet):
            if letter == char:
                return offset

    def get_player_letters_found(self):
        return self.player_letters_found

    def decrease_player_lives(self):
        self.player_lives -= 1

    def player_choice(self):
        print(f'{self.player.name}, please choose a letter of the alphabet:')
        while True:
            choice = str(input("> ")).upper()
            if len(choice) != 1 or choice.isdigit() or choice in self.letters_used:
                print('You must choose a letter of the alphabet you have not used:')
                continue
            return choice

    def check_choice(self, choice):
        if choice in self.get_word():
            for offset, item in enumerate(self.get_word()):
                if choice == item:
                    self.update_player_letters_found(item, offset)
        else:
            self.decrease_player_lives()
        self.update_letters_used(choice, self.get_letter_pos_in_alphabet(choice))

    def display_word(self):
        print(' '.join(self.get_player_letters_found()))

    def display_letters_used(self):
        letters_used = [i for i in self.letters_used if i in list(string.ascii_uppercase)]
        print(''.join(letters_used))

    def display_lives(self):
        print('Lives left: {}'.format('#'*self.player_lives))

    def update_display(self):
        os.system('clear')
        self.display_word()
        self.display_letters_used()
        self.display_lives()

    def check_state(self):
        if self.player_lives <= 0:
            print(f'Sorry {self.player.get_name()}, looks like you are out of guesses.')
            print('Better luck next time!')
            return 1
        if ''.join(self.get_player_letters_found()) == self.get_word():
            print(f'Congratulations! You have found the word "{self.get_word()}".')
            return 1
        return 0

    def play(self):
        state = 1
        print(f"Hello {self.player.get_name()}, let's play a game of Hang Man!")

        while state == 0:
            self.update_display()
            self.check_choice(self.player_choice())
            state = self.check_state()

if __name__ == '__main__':
    game = Hang_Man()
    game.play()