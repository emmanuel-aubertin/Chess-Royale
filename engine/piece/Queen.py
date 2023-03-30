from piece import Piece as p

class Queen(p):

    def __init__(self, team, pos):
        self.team = team
        self.pos = pos

    def is_legal(board, pos):
        if (not super().is_legal(pos)):  # If not in board
            return False
        if (board[pos[0]][pos[1]]!="none"):
            return False
        return True

    # Get possible next move
    def get_playable_pos(self, board):
        pos_list = []
        for i in range(-7, 7):
            for j in range(-7, 7):
                if(self.is_legal([(self.pos[0]+i),(self.pos[1]+j)])):
                    pos_list.append([self.pos[0] + i, self.pos[1] + j])
                    print(i, j)
        return pos_list

    def is_promo(board, pos):
        return False

    def get_attacking_pos(board,self):
        pos_list = []
        for i in range(-7,7):
            for j in range(-7,7):
                if (super().is_legal([self.pos[0]+i,self.pos[1]+j])):  # Get only pos in the board
                    pos_list.append([i, j])
                    print(i, j)
        return pos_list

    def is_playable(self, board, pos):
        playable_pos = self.get_playable_pos(board)
        for e in playable_pos:
            if (e == pos):
                return True
        return False