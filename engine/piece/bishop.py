from engine.piece.piece import Piece as p

class Bishop(p):
    def __init__(self, team, pos):  # pos = 2, 5
        self.team = team
        self.pos = pos 

    def is_legal(self, board, pos):
        board_list = board.get_board()
        print("Is bishop lega")
        print("pos = [" + str(pos[0]) + ", " + str(pos[1]) + "]")
        if(not super().is_legal(pos)):
            print("Out of the broad")
            return False
        pos_1 = self.pos[1] 
        for i in range(self.pos[0]+1, pos[0]):
            
            if(self.pos[1] > pos[1]):
                print("Minus")
                pos_1 -= 1
            else:
                print("Max")
                pos_1 += 1
            print("Checking pos ==> " + str(i) + " " + str(pos_1))
            if(board_list[i][pos_1]):
                return False
        return True

    def get_playable_pos(self, board):
        pos_list = []
        board_list = board.get_board()
        j = 1
        for i in range(self.pos[0], 8):
            if(board_list[i, self.pos[1] + j]):
                pos_list.append([i, self.pos[1] + j])
                break
            if(self.is_legal(board, [i, self.pos[1] + j])):
                pos_list.append([i, self.pos[1] + j])
            j += 1
        j = 1
        for i in range(0, self.pos[0]):
            if(board_list[i, self.pos[1] + j]):
                pos_list.append([i, self.pos[1] + j])
                break
            if(self.is_legal(board, [i, self.pos[1] + j])):
                pos_list.append([i, self.pos[1] + j])
            j += 1
        j = 1
        for i in range(self.pos[1], 8):
            if(board_list[self.pos[0] + j, i]):
                pos_list.append([self.pos[0] + j, i])
                break
            if(self.is_legal(board, [self.pos[0] + j, i])):
                pos_list.append([self.pos[0] + j, i])
            j += 1
        j = 1
        for i in range(0, self.pos[1]):
            if(board_list[self.pos[0] + j, i]):
                pos_list.append([self.pos[0] + j, i])
                break
            if(self.is_legal(board, [self.pos[0] + j, i])):
                pos_list.append([self.pos[0] + j, i])
            j += 1
        return pos_list
    
    def get_attacking_pos(self, board):
        pos_list = []
        board_list = board.get_board()
        playable_list = self.get_playable_pos()
        for e in playable_list:
            if(board_list[e[0]][e[1]]): # If there is a piece on playable case add it
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