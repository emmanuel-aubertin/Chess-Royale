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

        self.board[0][0] = Rook(1, [0, 0])
        self.board[7][0] = Rook(0, [7, 0])

        self.board[4][4] = Knight(1, [4, 4]) # 0, 1
        self.board[7][1] = Knight(0, [7, 1])

        self.board[0][2] = Bishop(1, [0, 2])
        self.board[7][2] = Bishop(0, [7, 2])

        self.board[0][3] = Queen(1, [0, 3])
        self.board[7][3] = Queen(0, [7, 3])

        self.board[0][4] = King(1, [0, 4])
        self.board[7][4] = King(0, [7, 4])

        self.board[0][5] = Bishop(1, [0, 5])
        self.board[7][5] = Bishop(0, [7, 5])

        self.board[0][6] = Knight(1, [0, 6])
        self.board[7][6] = Knight(0, [7, 6])

        self.board[0][7] = Rook(1, [0, 7])
        self.board[7][7] = Rook(0, [7, 7])

    def get_board(self):
        return self.board

    def play(self, team, pos, new_pos):
        if(not self.board[pos[0]][pos[1]]):
            print("\n \tTeam = " + str(team) + "\tType : 0\tPos " + str(pos) + "\tNew Pos : " + str(new_pos))
            return False
        else:
            print("\n \tTeam = " + str(team) + "\tType : " + self.board[pos[0]][pos[1]].get_type() +"\tPos " + str(pos) + "\tNew Pos : " + str(new_pos))
            
        print("Team 0 is playing")
        #print("self.board[pos[0]][pos[1]].team == team ==> " + str(self.board[pos[0]][pos[1]].team == team))
        #print("self.board[pos[0]][pos[1]].play(self, new_pos) ==> " + str(self.board[pos[0]][pos[1]].play(self, new_pos)))
        if (self.board[pos[0]][pos[1]].team == team and self.board[pos[0]][pos[1]].play(self, new_pos)):   # checker si c'est égal à une pièce blanche
            self.board[new_pos[0]][new_pos[1]] = self.board[pos[0]][pos[1]]
            print("Old pos ("+ str(pos[0]) +  ", "+ str(pos[1]) + ") = " + self.board[pos[0]][pos[1]].get_type())
            self.board[pos[0]][pos[1]] = None
            print("Old pos ("+ str(pos[0]) +  ", "+ str(pos[1]) + ") = " + str(self.board[pos[0]][pos[1]]))
            print("New pos (" + str(new_pos[0]) +  ", "+ str(new_pos[1]) + ") = " + str(self.board[new_pos[0]][new_pos[1]]))
            return True
        return False

    def print_board(self):
        for i in range(0, 8):
            for j in range(0, 8):
                if(self.board[i][j]):
                    print(self.board[i][j].get_type() + "\t\t", end="")
                    continue
                print("0"+ "\t\t", end="")
            print()