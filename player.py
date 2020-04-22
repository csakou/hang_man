#!/home/csakou/Documents/Python/hang_man/venv/bin/python3

class Player:
    def __init__(self):
        self.set_name()
        self.characters_found = []

    def set_name(self):
        print("Hello player. Please enter your name. It must have 1-16 characters:")
        while True:
            try:
                self.name = input("> ")
                if len(self.name) <= 0 or len(self.name) > 16:
                    raise ValueError
                break
            except ValueError:
                print("Your name must be in between 1-16 characters:")

    def set_characters_found(self, word_length):
        try:
            self.characters_found = ['_' for i in range(word_length)]
        except Exception as e:
            print(e)

    def make_choice(self):
        print(f"{self.name}, please choose a letter of the alphabet:")
        while True:
            try:
                choice = str(input("> ")).upper()
                if len(choice) != 1 or choice.isdigit():
                    raise ValueError
                return choice
            except ValueError:
                print("You must choose a letter of the alphabet:")

    def update_characters_found(self, character, position):
        try:
            self.characters_found[position] = character
        except Exception as e:
            print(e)

    def get_name(self):
        return self.name

    def get_characters_found(self):
        return self.characters_found

if __name__ == "__main__":
    player = Player()