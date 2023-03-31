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
        print(str(pos[0]) + " ==  " + str(self.pos[0] + 2))
        if(pos[0] == self.pos[0] + 2 and pos[1] == self.pos[1] + 1 and not board_list[pos[0]][pos[1]] or board_list[pos[0]][pos[1]].team != self.team):
            return True
        if(pos[0] == self.pos[0] + 2 and pos[1] == self.pos[1] - 1 and not board_list[pos[0]][pos[1]] or board_list[pos[0]][pos[1]].team != self.team):
            return True
        if(pos[0] == self.pos[0] - 2 and pos[1] == self.pos[1] + 1 and not board_list[pos[0]][pos[1]] or board_list[pos[0]][pos[1]].team != self.team ):
            return True
        if(pos[0] == self.pos[0] - 2 and pos[1] == self.pos[1] - 1 and not board_list[pos[0]][pos[1]] or board_list[pos[0]][pos[1]].team != self.team ):
            return True
        if(pos[0] == self.pos[0] - 1 and pos[1] == self.pos[1] + 2 and not board_list[pos[0]][pos[1]] or board_list[pos[0]][pos[1]].team != self.team):
            return True
        if(pos[0] == self.pos[0] + 1 and pos[1] == self.pos[1] + 2 and not board_list[pos[0]][pos[1]] or board_list[pos[0]][pos[1]].team != self.team):
            return True
        if(pos[0] == self.pos[0] - 1 and pos[1] == self.pos[1] - 2 and not board_list[pos[0]][pos[1]] or board_list[pos[0]][pos[1]].team != self.team ):
            return True
        if(pos[0] == self.pos[0] + 1 and pos[1] == self.pos[1] - 2 and not board_list[pos[0]][pos[1]] or board_list[pos[0]][pos[1]].team != self.team ):
            return True
        return False
        

    def get_playable_pos(self, board): 
        pos_list = []
        if(self.is_legal()):
            pos_list.append([self.pos[0] + 2, self.pos[1] + 1])
            pos_list.append([self.pos[0] + 2, self.pos[1] - 1])
            pos_list.append([self.pos[0] - 2, self.pos[1] + 1])
            pos_list.append([self.pos[0] - 2, self.pos[1] - 1])
            pos_list.append([self.pos[0] - 1, self.pos[1] + 2])
            pos_list.append([self.pos[0] + 1, self.pos[1] + 2])
            pos_list.append([self.pos[0] - 1, self.pos[1] - 2])
            pos_list.append([self.pos[0] + 1, self.pos[1] - 2])
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