from engine.piece.piece import Piece as p
from engine.piece.king import King
from engine.piece.rook import Rook
from engine.piece.knight import Knight
from engine.piece.pawn import Pawn
from engine.piece.bishop import Bishop
from engine.piece.Queen import Queen

class Board:
    def __init__(self):
        print("NEW BOARD")
        self.board = [[0 for i in range(8)] for j in range(8)]
        
        for i in range(0, 8):
            for j in range(0, 8):
                self.board[i][j] = None
                
        for i in range(0, 8):

            self.board[1][i] = Pawn(1, [1, i])
            self.board[6][i] = Pawn(0, [6, i])


        self.board[0][0] = Rook(1, [0, 0]) # 0, 0

        self.board[7][0] = Rook(0, [7, 0])

        self.board[0][1] = Knight(1, [0, 1]) 
        self.board[7][1] = Knight(0, [7, 1])

        self.board[0][2] = Bishop(1, [0, 2])
        self.board[7][2] = Bishop(0, [7, 2])

        self.board[0][3] = Queen(1, [0, 3])
        self.board[7][3] = Queen(0, [7, 3])

        self.board[0][4] = King(1)
        self.board[7][4] = King(0)

        self.board[0][5] = Bishop(1, [0, 5])
        self.board[7][5] = Bishop(0, [7, 5])

        self.board[0][6] = Knight(1, [0, 6])
        self.board[7][6] = Knight(0, [7, 6])

        self.board[0][7] = Rook(1, [0, 7])
        self.board[7][7] = Rook(0, [7, 7])

    def get_board(self):
        return self.board

    def play(self, team, pos, new_pos):

        self.board[pos[0]][pos[1]].play(self, new_pos)
        self.board[new_pos[0]][new_pos[1]] = self.board[pos[0]][pos[1]]
        self.board[pos[0]][pos[1]] = None
        return True


    def print_board(self):
        for i in range(0, 8):
            for j in range(0, 8):
                if(self.board[i][j]):
                    print(self.board[i][j].get_type() + "\t\t", end="")
                    continue
                print("0"+ "\t\t", end="")
            print()
    
    def get_king(self, team):
        for i in range(0,8):
            for j in range(0,8):
                if(self.board[i][j] and self.board[i][j].get_type() == 'K' and self.board[i][j].team == team):
                    return self.board[i][j]
        return None

    def is_check(self, team):
        king = self.get_king(team)
        return king.is_check(self)