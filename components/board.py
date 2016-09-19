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
        if position not in range(0, 9) or value == ' ':
            return False
        return self.content[position].fill(value)

    def reset(self):
        """
        Reinitializes the Board with its default values
        """
        for square in self.content:
            square.reset()

    def __str__(self):
        res = "X\Y 1  2  3 \n"
        for i in range(0,9):
            if i % 3 == 0:
                if i == 0: # omg this is so bad...
                    res += "1  "
                else:
                    res += str(i >> 1)+"  "
            res += str(self.content[i])
            if i % 3 == 2:
                res += '\n'
        return res