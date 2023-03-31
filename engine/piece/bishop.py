from engine.piece.piece import Piece as p

class Bishop(p):
    def __init__(self, team, pos):  # pos = 2, 5
        self.team = team
        self.pos = pos 

    def is_legal(self, board, pos):
        if not(abs(self.pos[0] - pos[0]) == abs(self.pos[1] - pos[1])):
            return False
        if(self.pos[0] == pos[0] or self.pos[1] == pos[1]):
            return False
        board_list = board.get_board()
        if(board_list[pos[0]][pos[1]] and board_list[pos[0]][pos[1]].team == self.team):
            return False
        print("Is bishop lega")
        print("pos = [" + str(pos[0]) + ", " + str(pos[1]) + "]")
        if(not super().is_legal(pos)):
            print("Out of the broad")
            return False
        pos_1 = self.pos[1]
        pos_0 = self.pos[0]
        '''for _ in range(self.pos[0]+1, max(pos[0]+1, pos[1]+1)):
            if(self.pos[0] > pos[0]):
                pos_0 -= 1
            else:
                pos_0 += 1
            if(self.pos[1] > pos[1]):
                pos_1 -= 1
            else:
                pos_1 += 1
            print("Checking pos ==> " + str(pos_0) + " " + str(pos_1))
            if(pos_1 - pos[1] == 0):
                if(pos_0 - pos[0]  != 0 ):
                    return False
                return True
            if(pos_0 - pos[0]  == 0):
                if(pos_1 - pos[1] != 0):
                    return False
                return True
            if(board_list[pos_0][pos_1]):
                return False'''
        for i in range(self.pos[0]+1, 8):
            if (board_list[i][i]):
                return False
        for i in range(self.pos[0]-1, 0):
            if (board_list[i][i]):
                return False
        for i in range(self.pos[1]+1, 8):
            if (board_list[i][i]):
                return False
        for i in range(self.pos[1]-1, 0):
            if (board_list[i][i]):
                return False
        return True

    def get_playable_pos(self, board):
        pos_list = []
        board_list = board.get_board()
        for i in range(0,8):
            for j in range(0,8):
                if(self.is_legal(board, [i, j])):
                    pos_list.append([i, j])
        return pos_list
    
    def get_attacking_pos(self, board):
        pos_list = []
        board_list = board.get_board()
        playable_list = self.get_playable_pos(board)
        for e in playable_list:
            print(e)
            if(board_list[int(e[0])][int(e[1])]): # If there is a piece on playable case add it
                pos_list.append(e)
        return pos_list
    
    def play(self, board, pos):
        print("Bishop play")
        if(not self.is_legal(board, pos)):
            return False
        self.pos = pos
        return True
    
    def is_promo(self, board, pos):
        return False
    
    def get_type(self):
        return "B"