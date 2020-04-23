#!/home/csakou/Documents/Python/hang_man/venv/bin/python3

class Player:
    def __init__(self):
        self.set_name()

    def set_name(self):
        print('Hello player. Please enter your name. It must have 1-16 characters:')
        while True:
            try:
                self.name = input("> ")
                if len(self.name) <= 0 or len(self.name) > 16:
                    raise ValueError
                break
            except ValueError:
                print('Your name must be in between 1-16 characters:')

    def get_name(self):
        return self.name

if __name__ == "__main__":
    player = Player()