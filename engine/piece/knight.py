from piece import Piece as p

class Knight:
    def __init__(self, team):
        self.team = team

    def is_legal(self, pos):
        return super().is_legal(pos)

    def get_playable_pos(self, board): 
        pos_list = []
        board_list = board.get_board()
        if(board_list[self.pos[0] + 2, self.pos[1] + 1] or board_list[self.pos[0] + 2, self.pos[1] + 1].team != self.team and self.is_legal([self.pos[0] + 2, self.pos[1] + 1])):
            pos_list.append([self.pos[0] + 2, self.pos[1] + 1])
        if(board_list[self.pos[0] + 2, self.pos[1] - 1] or board_list[self.pos[0] + 2, self.pos[1] - 1].team != self.team and self.is_legal([self.pos[0] + 2, self.pos[1] - 1])):
            pos_list.append([self.pos[0] + 2, self.pos[1] - 1])
        if(board_list[self.pos[0] - 2, self.pos[1] + 1] or board_list[self.pos[0] - 2, self.pos[1] + 1].team != self.team and self.is_legal([self.pos[0] - 2, self.pos[1] + 1])):
            pos_list.append([self.pos[0] - 2, self.pos[1] + 1])
        if(board_list[self.pos[0] - 2, self.pos[1] - 1] or board_list[self.pos[0] - 2, self.pos[1] - 1].team != self.team and self.is_legal([self.pos[0] - 2, self.pos[1] - 1])):
            pos_list.append([self.pos[0] - 2, self.pos[1] - 1])
        if(board_list[self.pos[0] - 1, self.pos[1] + 2] or board_list[self.pos[0] - 1, self.pos[1] + 2].team != self.team and self.is_legal([self.pos[0] - 1, self.pos[1] + 2])):
            pos_list.append([self.pos[0] - 1, self.pos[1] + 2])
        if(board_list[self.pos[0] + 1, self.pos[1] + 2] or board_list[self.pos[0] + 1, self.pos[1] + 2].team != self.team and self.is_legal([self.pos[0] + 1, self.pos[1] + 2])):
            pos_list.append([self.pos[0] + 1, self.pos[1] + 2])
        if(board_list[self.pos[0] - 1, self.pos[1] - 2] or board_list[self.pos[0] - 1, self.pos[1] - 2].team != self.team and self.is_legal([self.pos[0] - 1, self.pos[1] - 2])):
            pos_list.append([self.pos[0] - 1, self.pos[1] - 2])
        if(board_list[self.pos[0] + 1, self.pos[1] - 2] or board_list[self.pos[0] + 1, self.pos[1] - 2].team != self.team and self.is_legal([self.pos[0] + 1, self.pos[1] - 2])):
            pos_list.append([self.pos[0] + 1, self.pos[1] - 2])
        return pos_list
    
    def get_attacking_pos(board):
        pos_list = []
        for i in range (0, 3):
            for j in range (0, 3):
                if(super().is_legal()): # Get only pos in the board
                    pos_list.append([i, j])
                    print(i, j)
        return pos_list
    
    def is_promo(board, pos):
        return False
    
    def play(self, pos):     
        play_list = self.get_playable_pos()
        for e in play_list:
            if(e == pos):
                self.pos = pos
                return True
        return False            
