from abc import ABC, abstractmethod

# Extends ABC for create an abstract class
class Piece(ABC):

    @abstractmethod
    def get_playable_pos(board):
        pass

    @abstractmethod
    def is_playable(board):
        pass

    @abstractmethod
    def get_type(): 
        # Return letter of type
        # K = King      |   Q = Queen
        # P = Pawn      |   R = Rook (Tower)
        # B = Bishop    |   N = Knight
        pass

