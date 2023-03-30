from piece import Piece as p

class Bishop:
    def __init__(self, team, id):  # pos = 2, 5
        self.team = team
        self.id = id
        self.pos = pos # Position du bishop
        if (team == 0):
            if (id==0):
                pos = [2, 7]
            else:
                pos = [5, 7]
        else:
            if (id==0):
                pos = [2, 0]
            else:
                pos = [5, 0]

    def get_playable_pos(self):
        pos_list = []
        for i in range(0, 7):
            if(self.is_legal()):
                pos_list.append(self.pos[0] + i, self.pos[0] + i)
                pos_list.append(self.pos[0] + i, self.pos[0] - i)
                pos_list.append(self.pos[0] - i, self.pos[0] + i)
                pos_list.append(self.pos[0] - i, self.pos[0] - i)