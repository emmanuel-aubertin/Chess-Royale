from engine.piece.piece import Piece as p

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
        board_list = board.get_board()

        # ROOK LIKE MOVEMENT
        for i in range (self.pos[0], 8):
            if(board_list[i][self.pos[1]]): # if piece break
                pos_list.append([i, self.pos[1]])
                break;
            if(self.is_legal(board, [i, self.pos[1]]) and i != self.pos[1]):
                pos_list.append([i, self.pos[1]])
        for i in range (0, self.pos[0]):
            if(board_list[i][self.pos[1]]): # if piece break
                pos_list.append([i, self.pos[1]])
                break;
            if(self.is_legal(board, [i, self.pos[1]]) and i != self.pos[1]):
                pos_list.append([i, self.pos[1]])

        for i in range (self.pos[1], 8):
            if(board_list[self.pos[0]][i]): # if piece break
                pos_list.append([self.pos[0], i])
                break;
            if(self.is_legal(board, [self.pos[0], i]) and i != self.pos[1]):
                pos_list.append([self.pos[0], i])
        for i in range (0, self.pos[0]):
            if(board_list[i][self.pos[1]]): # if piece break
                pos_list.append([self.pos[0], i])
                break;
            if(self.is_legal(board, [self.pos[0], i]) and i != self.pos[1]):
                pos_list.append([self.pos[0], i])

        # BISHOP LIKE MOVEMENT
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

    def is_promo(self, board, pos):
        return False

    def get_attacking_pos(self, board):
        pos_list = []
        board_list = board.get_board()
        playable_list = self.get_playable_pos()
        for e in playable_list:
            if(board_list[e[0]][e[1]]): # If there is a piece on playable case add it
                pos_list.append(e)
        return pos_list
   
    def get_type(self):
        return "Q"
    
    def play(self, board, pos):
        if (self.is_legal(board, pos)):
            self.pos = pos
            return True
        return False