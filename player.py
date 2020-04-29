"""
A class used to represent a Player

Attributes
----------

name : str
    A string between 1-16 charactres representing the players name.

Methods
-------

validate_name(name):
    Checks if the name given by the user is valid.

get_name():
    Returns the players name
"""

class Player:
    def __init__(self):
        """
        Initializes Player object and requests the name of the player
        """
        print("Hello player, please input your name. It must be between 1-16 characters:")
        name = input('> ')
        self.name = self.validate_name(name)

    def validate_name(self, name):
        """
        Validates if the name of the player is in the correct form

        Parameters
        ----------

        name : str
            The name the user inputted
        """
        if len(name) <= 0 or len(name) > 16:
            raise ValueError('Your name must be in between 1-16 characters:')
        return name

    def get_name(self):
        """
        Returns
        --------

        name : str
            The name of the player
        """
        return self.name