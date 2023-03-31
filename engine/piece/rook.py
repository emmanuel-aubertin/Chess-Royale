from engine.piece.piece import Piece as p

class Rook(p):
    def __init__(self, team, pos):
        self.team = team
        self.pos = pos

    def is_legal(self, board, pos):
        print("Rook legal")
        board_list = board.get_board()
        if(not super().is_legal(pos)): # If not in board
            print("Out of the broad")
            return False
        if(board_list[pos[0]][pos[1]]!=None and board_list[pos[0]][pos[1]].team == self.team):
            return False
        if((pos[0] != self.pos[0] and pos[1] != self.pos[1])or ( pos[1] != self.pos[1] and pos[0] != self.pos[0])):
            return False
        if(self.pos[1] == pos[1]): # if horizontal move
            print("Vertical move")
            for i in range(self.pos[0]+1, 8):
                print("Checking : "+ str(i) + " " + str(self.pos[1]))
                if(board_list[i][self.pos[1]]!=None):
                    return False # There is a piece between the place and the rook
            for i in range(0,self.pos[0]-1):
                print("Checking : "+ str(i) + " " + str(self.pos[1]))
                if(board_list[i][self.pos[1]]!=None):
                    return False # There is a piece between the place and the rook
        if(self.pos[0] == pos[0]): # if vertical move
            print("Horizontal move")
            for i in range(self.pos[1]+1, 8):
                print("i: " + str(i))
                if(board_list[self.pos[0]][i]!=None):
                    print(str(board_list[i][self.pos[0]]))
                    return False # There is a piece between the place and the rook
            for i in range(0, self.pos[1]+1):
                print("i: " + str(i))
                if(board_list[self.pos[0]][i]!=None):
                    print(str(board_list[i][self.pos[0]]))
                    return False # There is a piece between the place and the rook
        return True

    '''
    def is_legal(self, board, pos):
        board_list=board.get_board()
        if (not super().is_legal(pos)):  # If not in board
            print("Out of the broad")
            return False
    '''

    # Get possible next move
    def get_playable_pos(self, board):
        pos_list = []
        board_list = board.get_board()



        for i in range (self.pos[0], 8):
            if(board_list[i][self.pos[1]]!=None): # if piece break
                if (board_list[i][self.pos[1]].team != self.team):
                    pos_list.append([i, self.pos[1]])
                break;
            if(self.is_legal(board, [i, self.pos[1]]) and i != self.pos[1]):
                pos_list.append([i, self.pos[1]])
        for i in range (self.pos[0],0,-1):
            if(board_list[i][self.pos[1]]!=None): # if piece break
                if (board_list[i][self.pos[1]].team != self.team):
                    pos_list.append([i, self.pos[1]])
                break;
            if(self.is_legal(board, [i, self.pos[1]]) and i != self.pos[1]):
                pos_list.append([i, self.pos[1]])



        for i in range (self.pos[1], 8):
            if(board_list[self.pos[0]][i]!=None): # if piece break
                if (board_list[self.pos[0]][i].team != self.team):
                    pos_list.append([self.pos[0], i])
                break;
            if(self.is_legal(board, [self.pos[0], i]) and i != self.pos[0]):
                pos_list.append([self.pos[0], i])
        for i in range (self.pos[1],0,-1):
            if(board_list[self.pos[0]][i]!=None): # if piece break
                if (board_list[self.pos[0]][i].team != self.team):
                    pos_list.append([self.pos[0], i])
                break;
            if(self.is_legal(board, [self.pos[0], i]) and i != self.pos[0]):
                pos_list.append([self.pos[0], i])
        return pos_list

    def is_promo(self, board, pos):
        return False
    
    def get_attacking_pos(self, board):
        pos_list = []
        board_list = board.get_board()
        playable_list = self.get_playable_pos(board)
        for e in playable_list:
            if(board_list[e[0]][e[1]]): # If there is a piece on playable case add it
                pos_list.append(e)
        return pos_list

    def is_playable(self, board, pos):
        playable_pos = self.get_playable_pos(board)
        for e in playable_pos:
            if(e == pos):
                return True
        return False

    def get_type(self):
        return "R"

    def play(self, board, pos):
        self.pos = pos
        return True