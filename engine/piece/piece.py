from abc import ABC, abstractmethod

# Extends ABC for create an abstract class
class Piece(ABC):

    @abstractmethod
    def get_playable_pos(board):
        pass

    @abstractmethod
    def is_playable(board):
        pass
    
    # True if pos is in the Board
    def is_legal(board, pos):
        return (pos[0] < 8 and pos[0] >= 0 and pos[1] < 8 and pos[1] >= 0)

    @abstractmethod
    def is_promo(board, pos):
        pass

    @abstractmethod
    def get_attacking_pos(board, pos):
        pass

    @abstractmethod
    def get_type(): 
        # Return letter of type
        # K = King      |   Q = Queen
        # P = Pawn      |   R = Rook (Tower)
        # B = Bishop    |   N = Knight
        pass