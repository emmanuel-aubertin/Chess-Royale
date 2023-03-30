class Board:
    board = [8][8]
    
    def __init__(self):
        for i in range(0, 8):
            for j in range(0, 8):
                self.board[i][j] = None