from engine.piece.piece import Piece as p

class King(p):

    def __init__(self, team):
        self.team = team
        self.is_rockable = True
        if(team == 1):
            self.pos = [3, 0]
        else:
            self.pos = [3, 7]

    def is_legal(self, board, pos):
        if(not super().is_legal(pos)): # If not in board
            return False
        board_list = board.get_board()
        for i in range (0, 8):
            for j in range (0, 8):
                if(board_list[i][j] != None and board_list[i][j].team != self.team):
                    attacking =  board_list[i][j].get_attacking_pos(board)
                    if(attacking):
                        for e in  attacking:
                            if(e[0] == pos[0] and e[1] == pos[1]):
                                return False
        return True

    # Get possible next move
    def get_playable_pos(self, board):
        pos_list = []
        for i in range (-1, 2):
            for j in range (-1, 2):
                if(self.is_legal(board, [self.pos[0] + i, self.pos[1] + j])):
                    pos_list.append([self.pos[0] + i, self.pos[1] + j])
                    print(i, j)
        return pos_list

    def is_promo(self, board, pos):
        return False
    
    def get_attacking_pos(self, board):
        pos_list = []
        board_list = board.get_board()
        for i in range (0, 3):
            for j in range (0, 3):
                if(self.is_legal(board, [self.pos[0] + i, self.pos[1] + j]) and board_list[i][j]):
                    pos_list.append([i, j])
                    print(i, j)
        return pos_list

    def is_check(self, board):
        print("King check is_check")
        board_list = board.get_board()
        for i in range (0, 8):
            for j in range (0, 8):
                if(board_list[i][j] != None and board_list[i][j].team != self.team):
                    if (board_list[i][j].get_attacking_pos(board) != None):
                        for e in  board_list[i][j].get_attacking_pos(board):
                            if(e[0] == self.pos[0] and e[1] == self.pos[1]):
                                return True
                    else:
                        if(e[0] == self.pos[0] and e[1] == self.pos[1]):
                                return True
        return False

    def is_playable(self, board, pos):
        playable_pos = self.get_playable_pos(board)
        for e in playable_pos:
            if(e == pos):
                return True
        return False

<<<<<<< HEAD
    def get_type(self):
        return "K"
    
    def play(self, board, pos):
        if (self.is_legal(board, pos)):
            self.pos = pos
            return True
        return False
=======
    def play(self):
        self.is_rockable = False
>>>>>>> 51d4d4940f5f112a17944138cac1146306fb5928
