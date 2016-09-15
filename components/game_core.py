from board import Board

class GameCore(object):
    """
    This class should be used to implement the main game
    """

    def __init__(self):
        self.board = Board()
        self.current_turn = 1
        self.turns_count = 0
        self.p1_victories = 0
        self.p2_victories = 0

    def _horizontal_line(self):
        for i in range(0,9,3):
            if self.board.content[i] == self.board.content[i+1] \
                    and self.board.content[i] == self.board.content[i+2]:
                return True
        return False

    def _vertical_line(self):
        for i in range(0,3):
            if self.board.content[i] == self.board.content[i+3] \
                   and self.board.content[i] == self.board.content[i+6]:
                return True
        return False

    def _diagonal_line(self):
        return (self.board.content[0] == self.board.content[4]
               and self.board.content[0] == self.board.content[8]) \
               or \
               (self.board.content[6] == self.board.content[4]
               and self.board.content[6] == self.board.content[2])

    def update_turn(self):
        if self.current_turn == 1:
            self.current_turn = 2
        else:
            self.current_turn = 1

    def has_draw(self):
        return self.turns_count == 9

    def has_winner(self):
        if self.turns_count < 6 or self.has_draw():
            return False
        return self._horizontal_line() or self._vertical_line()\
               or self._diagonal_line()

    def fill(self,position,value):
        if self.board.fill(position,value):
            self.turns_count += 1
            if self.has_winner():
                if self.current_turn == 1:
                    self.p1_victories += 1
                else:
                    self.p2_victories += 1
            else:
                if not self.has_draw():
                    self.update_turn()
            return True
        return False

    def new_game(self):
        self.board.reset()
        self.update_turn()
        self.turns_count = 0

    def reset(self):
        self.board.reset()
        self.current_turn = 1
        self.turns_count = 0
        self.p1_victories = 0
        self.p2_victories = 0

    def __str__(self):
        res = "Player 1: "+str(self.p1_victories)+" - Player 2: "\
              + str(self.p2_victories)+'\n'+str(self.board)
        return res
