from engine.piece.piece import Piece as p

class Pawn(p):
    is_promoted = False

    def __init__(self, team, pos):
        self.team = team
        self.pos = pos

    def is_legal(self, board, pos):
        print("Is pawn legal")
        board_list = board.get_board()
        if(not super().is_legal(pos)):
            print("Out of board")
            return False
        print(str(pos[0]) + " == " + str(self.pos[0]-1) +"and " + str(pos[1])  + "== " + str(self.pos[1])  +" and  not " + str(board_list[pos[0]][pos[1]]) + " |||| " + str())
        if((pos[0] == self.pos[0]-1 and pos[1]) == self.pos[1] and not board_list[pos[0]][pos[1]]):
            return True
        if((pos[0] == self.pos[0]+1 and pos[1]) == self.pos[1] and not board_list[pos[0]][pos[1]]):
            return True
        if(pos[0] == self.pos[0]+1 and pos[1] == self.pos[1]+1 and board_list[pos[0]][pos[1]] and board_list[pos[0]][pos[1]].team != self.team):
            return True
        if(pos[0] == self.pos[0]-1 and pos[1] == self.pos[1]-1 and board_list[pos[0]][pos[1]] and board_list[pos[0]][pos[1]].team != self.team):
            return True
        return False
    
    def is_promote(self, board):
        if (self.team):
            if (board.curr_pos() == 0):
                return True
        else:
            if (board.curr_pos() == 7):
                return True
        return False
    
    def get_playable_pos(self, board):
        pos_list = []
        board_list = board.get_board()
        if(self.team==0):
            print(board_list[self.pos[0] - 1][self.pos[1]] == None or board_list[self.pos[0] - 1][self.pos[1]])
            if (board_list[self.pos[0] - 1][self.pos[1]] == None or board_list[self.pos[0] - 1][self.pos[1]]):
                print("1")
                pos_list.append([self.pos[0] - 1, self.pos[1]])
            if (board_list[self.pos[0] - 1][self.pos[1] + 1] == None or board_list[self.pos[0] - 1][self.pos[1] + 1]):
                print("2")
                pos_list.append([self.pos[0] - 1, self.pos[1] + 1])
            if (board_list[self.pos[0] - 1][self.pos[1] - 1]):
                print("3")
                pos_list.append([self.pos[0] - 1, self.pos[1] - 1])
            print(board_list[self.pos[0]])
            if (self.pos[0] == 6):
                print("4")
                pos_list.append([self.pos[0] - 2, self.pos[1]])

        if (self.team == 1):
            if (board_list[self.pos[0]][self.pos[1] + 1]):
                print("5")
                pos_list.append([self.pos[0], self.pos[1] + 1])
            if (board_list[self.pos[0] + 1][self.pos[1] + 1]):
                print("6")
                pos_list.append([self.pos[0] + 1, self.pos[1] + 1])
            if (board_list[self.pos[0] - 1][self.pos[1] + 1]):
                print("7")
                pos_list.append([self.pos[0] - 1, self.pos[1] + 1])
            if (self.pos[1] == 1):
                print("8")
                pos_list.append([self.pos[0], self.pos[1] + 2])
        return pos_list

    def get_type(self):
        return "P"
    
    def play(self, board, pos):
        if (self.is_legal(board, pos)):
            self.pos = pos
            return True
        return False