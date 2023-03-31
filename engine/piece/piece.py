from abc import ABC, abstractmethod

# Extends ABC for create an abstract class
class Piece:
    def get_playable_pos(board):
        pass


    def is_playable(board):
        pass
    
    # True if pos is in the Board
    def is_legal(board, pos):
        if (pos[0] < 8 and pos[0] >= 0 and pos[1] < 8 and pos[1] >= 0):
            return True
        return False


    def is_promo(board, pos):
        pass


    def get_attacking_pos(board, pos):
        pass


    def get_type(self): 
        # Return letter of type
        # K = King      |   Q = Queen
        # P = Pawn      |   R = Rook (Tower)
        # B = Bishop    |   N = Knight
        pass
