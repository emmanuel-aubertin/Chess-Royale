from piece import Piece as p
from piece import King
from rook import Rook
from knight import Knight
from pawn import Pawn
from bishop import Bishop
from Queen import Queen

class Board:
    

    def __init__(self):
        board = [8][8]
        for i in range(0, 8):
            for j in range(0, 8):
                self.board[i][j] = None
        for i in range(0, 8):
            board[1][i] = Pawn(0, [1, i])
            board[6][i] = Pawn(1, [6, i])
        
        board[0][0] = Rook(0, [0, 0])
        board[7][0] = Rook(1, [7, 0])

        board[0][1] = Knight(0, [0, 1])
        board[7][1] = Knight(1, [7, 1])

        board[0][2] = Bishop(0, [0, 2])
        board[7][2] = Bishop(1, [7, 2])

        board[0][3] = King(0, [0, 3])
        board[7][3] = King(1, [7, 3])

        board[0][4] = Queen(0, [0, 4])
        board[7][4] = Queen(1, [7, 4])

        board[0][5] = Bishop(0, [0, 5])
        board[7][5] = Bishop(1, [7, 5])

        board[0][6] = Knight(0, [0, 6])
        board[7][6] = Knight(1, [7, 6])

        board[0][7] = Rook(0, [0, 7])
        board[7][7] = Rook(1, [7, 7])
