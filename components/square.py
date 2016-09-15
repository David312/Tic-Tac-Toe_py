class Square(object):
    """
        As the name of the class says, this represents a square of the board.

        This class provides methods to get and set new values into the Square

    """
    def __init__(self):
        """
            Initializes the square and sets its contents to the default
            value ' ' (empty)
        """
        self.content = ' '

    def is_filled(self):
        """
            Tells you if the Square is filled with some content
        :return: True if the Square has some content in it
        """
        return self.content != ' '

    def fill(self,new_value):
        """
            Fills the Square with a given value if possible
        :param new_value: The value you want to put into the Square. IT HAS TO BE A CHARACTER
        :return: True if it was possible to set the new value
        """
        if not self.is_filled() and type(new_value)==str and len(new_value) == 1:
            self.content = new_value
            return True
        return False

    def content(self):
        """
            Returns the content of the Square
        :return: Square content
        """
        return self.content

    def reset(self):
        """
            Reinitializes the Square to its default value
        """
        self.content = ' '

    def __str__(self):
        return self.content