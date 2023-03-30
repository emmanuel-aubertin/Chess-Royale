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
    
    def get_playable_pos(board):
        pos_list = []
        # Le pion peut bouger en [x-1][y+1], [x+1][y+1] SI IL Y A UNE PIECE ENNEMIE
        # en [x][y+1] SI IL N Y A PAS DE PIECE ENNEMIE et en [x][y+2] SI IL EST 
        # TOUJOURS A SA POSITION DE DEPART