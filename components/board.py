from square import Square
class Board(object):
    """
        This class represents the board of the game.
        Provides useful methods for its use.
    """

    def __init__(self):
        """
            Initializes the 3x3 board with empty squares
        """
        self.content = []
        for i in range(1, 10):
            self.content.append(Square())

    def fill(self, position, value):
        """
            Tries to fill the square in the given position with a given value
        :param position: position of the board.
        :param value: value to set into the square
        :return: True if the operation was successfull
        """
        if position not in range(1, 10) or value == ' ':
            return False
        return self.content[position].fill(value)

    def reset(self):
        """
            Reinitializes the Board with its default values
        """
        for square in self.content:
            square.reset()

