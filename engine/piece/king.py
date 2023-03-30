from piece import Piece as p

class King(p):

    def __init__(self, team):
        self.team = team
        if(team == 1):
            self.pos = [3, 0]
        else:
            self.pos = [3, 7]

    def is_legal(board, pos):
        if(not super().is_legal(pos)): # If not in board
            return False
        # NEED TO CHECK IF IT'S A SAFE PLACEÒ
        return True

    # Get possible next move
    def get_playable_pos(self, board):
        pos_list = []
        for i in range (0, 3):
            for j in range (0, 3):
                if(self.is_legal()):
                    pos_list.append([i, j])
                    print(i, j)
        return pos_list

    def is_promo(board, pos):
        return False
    
    def get_attacking_pos(board):
        pos_list = []
        for i in range (0, 3):
            for j in range (0, 3):
                if(super().is_legal()): # Get only pos in the board
                    pos_list.append([i, j])
                    print(i, j)
        return pos_list

    def is_checkmate(self, board):
        board_list = board.get_board()
        for i in range (0, 8):
            for j in range (0, 8):
                if(board_list[i][j] != None and board_list[i][j].team != self.team):
                    for e in  board_list[i][j].get_attacking_pos():
                        if(e[0] == self.pos[0] and e[1] == self.pos[1]):
                            return True
        return False


    def is_playable(self, board, pos):
        playable_pos = self.get_playable_pos(board)
        for e in playable_pos:
            if(e == pos):
                return True
        return False
