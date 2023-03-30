from piece import Piece as p

class Bishop:
    def __init__(self, team, pos):  # pos = 2, 5
        self.team = team
        self.pos = pos 

    def get_playable_pos(self):
        pos_list = []
        for i in range(0, 7):
            if(self.is_legal()):
                pos_list.append([self.pos[0] + i, self.pos[0] + i])
                pos_list.append([self.pos[0] + i, self.pos[0] - i])
                pos_list.append([self.pos[0] - i, self.pos[0] + i])
                pos_list.append([self.pos[0] - i, self.pos[0] - i])