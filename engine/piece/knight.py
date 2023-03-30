from piece import Piece as p

class Knight:
    def __init__(self, team, id):
        self.team = team
        self.id = id
        self.pos = pos # Position du knight
        if (team == 0):
            if (id==0):
                pos = [1, 7]
            else:
                pos = [6, 7]
        else:
            if (id==0):
                pos = [1, 0]
            else:
                pos = [6, 0]

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