from engine.piece.piece import Piece as p

class Queen(p):
    def __init__(self, team, pos):
        self.team = team
        self.pos = pos

    def is_legal(self, board, pos):
        print("Queen legal")
        board_list = board.get_board()
        if(not super().is_legal(pos)): # If not in board
            print("Out of the broad")
            return False
        print("Checking horizontal/vertcal")

        if(self.pos[1] == pos[1]): # if horizontal move
            print("Vertical move")
            for i in range(self.pos[0]+1, pos[0]):
                print("Checking : "+ str(i) + " " + str(self.pos[1]))
                if(board_list[i][self.pos[1]]):
                    return False # There is a piece between the place and the rook
        if(self.pos[0] == pos[0]): # if vertical move
            print("Horizontal move")
            for i in range(self.pos[1]+1, pos[1]):
                print("i: " + str(i))
                if(board_list[self.pos[0]][i]):
                    print(str(board_list[i][self.pos[0]]))
                    return False # There is a piece between the place and the rook 
        pos_1 = self.pos[1]
        pos_0 = self.pos[0]
        for _ in range(self.pos[0]+1, max(pos[0]+1, pos[1]+1)):
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
                if(pos_0 - pos[0]  != 0):
                    return False
                return True
            if(pos_0 - pos[0]  == 0):
                if(pos_1 - pos[1] != 0):
                    return False
                return True
            if(board_list[pos_0][pos_1]):
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