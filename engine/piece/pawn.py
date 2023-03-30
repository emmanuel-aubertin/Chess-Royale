from piece import Piece as p

class Pawn(p):
    is_promoted = False

    def __init__(self, team):
        self.team = team

    def is_promote(self, board):
        if (self.team):
            if (board.curr_pos() == 0):
                self.promote()
        else:
            if (board.curr_pos() == 7):
                self.promote()
    
    def get_playable_pos(self, board):
        pos_list = []
        board_list = board.get_board()
        if(board_list[self.pos[0], self.pos[1] + 1]):
            pos_list.append([self.pos[0], self.pos[1] + 1])
        if(board_list[self.pos[0] + 1, self.pos[1] + 1]):
            pos_list.append([self.pos[0] + 1, self.pos[1] + 1])
        if(board_list[self.pos[0] - 1, self.pos[1] + 1]):
            pos_list.append([self.pos[0] - 1, self.pos[1] + 1])