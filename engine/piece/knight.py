from piece import Piece as p

class Knight:
    def __init__(self, team, pos):
        self.team = team
        self.id = id
        self.pos = pos


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