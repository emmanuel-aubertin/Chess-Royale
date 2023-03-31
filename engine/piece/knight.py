from engine.piece.piece import Piece as p

class Knight(p):
    def __init__(self, team, pos):
        self.team = team
        self.pos = pos

    def is_legal(self, board, pos):
        print("Is knight legal")
        if(not super().is_legal(pos)): # If not in board
            print("Out of board")
            return False
        board_list = board.get_board()
        if(board_list[pos[0]][pos[1]] and board_list[pos[0]][pos[1]].team == self.team):
            return False
        if(board_list[pos[0]][pos[1]]!=None):
            if(self.pos[0] < 6 and pos[0] == self.pos[0] + 2 and pos[1] == self.pos[1] + 1 and not board_list[pos[0]][pos[1]] and board_list[pos[0]][pos[1]].team != self.team):
                return True
            if(self.pos[0] < 6 and self.pos[1] > 0 and pos[0] == self.pos[0] + 2 and pos[1] == self.pos[1] - 1 and not board_list[pos[0]][pos[1]] and board_list[pos[0]][pos[1]].team != self.team):
                return True
            if(self.pos[0] > 1 and self.pos[1] < 7 and pos[0] == self.pos[0] - 2 and pos[1] == self.pos[1] + 1 and not board_list[pos[0]][pos[1]] and board_list[pos[0]][pos[1]].team != self.team ):
                return True
            if(self.pos[0] > 1 and self.pos[1] > 0 and pos[0] == self.pos[0] - 2 and pos[1] == self.pos[1] - 1 and not board_list[pos[0]][pos[1]] and board_list[pos[0]][pos[1]].team != self.team ):
                return True
            if(self.pos[0] > 0 and self.pos[1] < 6 and pos[0] == self.pos[0] - 1 and pos[1] == self.pos[1] + 2 and not board_list[pos[0]][pos[1]] and board_list[pos[0]][pos[1]].team != self.team):
                return True
            if(self.pos[0] < 7 and self.pos[1] < 6 and pos[0] == self.pos[0] + 1 and pos[1] == self.pos[1] + 2 and not board_list[pos[0]][pos[1]] and board_list[pos[0]][pos[1]].team != self.team):
                return True
            if(self.pos[0] > 0 and self.pos[1] > 1 and pos[0] == self.pos[0] - 1 and pos[1] == self.pos[1] - 2 and not board_list[pos[0]][pos[1]] and board_list[pos[0]][pos[1]].team != self.team ):
                return True
            if(self.pos[0] < 7 and self.pos[1] > 1 and pos[0] == self.pos[0] + 1 and pos[1] == self.pos[1] - 2 and not board_list[pos[0]][pos[1]] and board_list[pos[0]][pos[1]].team != self.team ):
                return True
        else:
            if (self.pos[0] < 6 and pos[0] == self.pos[0] + 2 and pos[1] == self.pos[1] + 1 and not board_list[pos[0]][pos[1]]):
                return True
            if (self.pos[0] < 6 and self.pos[1] > 0 and pos[0] == self.pos[0] + 2 and pos[1] == self.pos[1] - 1 and not board_list[pos[0]][pos[1]]):
                return True
            if (self.pos[0] > 1 and self.pos[1] < 7 and pos[0] == self.pos[0] - 2 and pos[1] == self.pos[1] + 1 and not board_list[pos[0]][pos[1]]):
                return True
            if (self.pos[0] > 1 and self.pos[1] > 0 and pos[0] == self.pos[0] - 2 and pos[1] == self.pos[1] - 1 and not board_list[pos[0]][pos[1]]):
                return True
            if (self.pos[0] > 0 and self.pos[1] < 6 and pos[0] == self.pos[0] - 1 and pos[1] == self.pos[1] + 2 and not board_list[pos[0]][pos[1]]):
                return True
            if (self.pos[0] < 7 and self.pos[1] < 6 and pos[0] == self.pos[0] + 1 and pos[1] == self.pos[1] + 2 and not board_list[pos[0]][pos[1]]):
                return True
            if (self.pos[0] > 0 and self.pos[1] > 1 and pos[0] == self.pos[0] - 1 and pos[1] == self.pos[1] - 2 and not board_list[pos[0]][pos[1]]):
                return True
            if (self.pos[0] < 7 and self.pos[1] > 1 and pos[0] == self.pos[0] + 1 and pos[1] == self.pos[1] - 2 and not board_list[pos[0]][pos[1]]):
                return True
        return False

    '''def get_playable_pos(self, board): 
        pos_list = []
        board_list = board.get_board()
        if(self.is_legal(board,self.pos)):
            pos_list.append([self.pos[0] + 2, self.pos[1] + 1])
        if(board_list[self.pos[0] + 2][ self.pos[1] - 1] and board_list[self.pos[0] + 2][ self.pos[1] - 1].team != self.team and self.is_legal(board, [self.pos[0] + 2, self.pos[1] - 1])):
            pos_list.append([self.pos[0] + 2, self.pos[1] - 1])
        if(board_list[self.pos[0] - 2][ self.pos[1] + 1] and board_list[self.pos[0] - 2][ self.pos[1] + 1].team != self.team and self.is_legal(board, [self.pos[0] - 2, self.pos[1] + 1])):
            pos_list.append([self.pos[0] - 2, self.pos[1] + 1])
        if(board_list[self.pos[0] - 2][ self.pos[1] - 1] and board_list[self.pos[0] - 2][ self.pos[1] - 1].team != self.team and self.is_legal(board, [self.pos[0] - 2, self.pos[1] - 1])):
            pos_list.append([self.pos[0] - 2, self.pos[1] - 1])
        if(board_list[self.pos[0] - 1][ self.pos[1] + 2] and board_list[self.pos[0] - 1][ self.pos[1] + 2].team != self.team and self.is_legal(board, [self.pos[0] - 1, self.pos[1] + 2])):
            pos_list.append([self.pos[0] - 1, self.pos[1] + 2])
        if(board_list[self.pos[0] + 1][ self.pos[1] + 2] and board_list[self.pos[0] + 1][ self.pos[1] + 2].team != self.team and self.is_legal(board, [self.pos[0] + 1, self.pos[1] + 2])):
            pos_list.append([self.pos[0] + 1, self.pos[1] + 2])
        if(board_list[self.pos[0] - 1][ self.pos[1] - 2] and board_list[self.pos[0] - 1][ self.pos[1] - 2].team != self.team and self.is_legal(board, [self.pos[0] - 1, self.pos[1] - 2])):
            pos_list.append([self.pos[0] - 1, self.pos[1] - 2])
        if(board_list[self.pos[0] + 1][ self.pos[1] - 2] and board_list[self.pos[0] + 1][ self.pos[1] - 2].team != self.team and self.is_legal(board, [self.pos[0] + 1, self.pos[1] - 2])):
            pos_list.append([self.pos[0] + 1, self.pos[1] - 2])
        return pos_list'''

    def get_playable_pos(self, board):
        pos_list = []
        board_list = board.get_board()
        for i in range(0,8):
            for j in range(0,8):
                if(self.is_legal(board, [i, j])):
                    pos_list.append([i, j])
        return pos_list
    
    def is_promo(self, board, pos):
        return False
    
    def get_type(self):
        return "N"
    
    def play(self, board, pos):
        if (self.is_legal(board, pos)):
            self.pos = pos
            return True
        return False
