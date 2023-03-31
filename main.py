from tkinter import *
from engine.board import Board
import playsound # pip install playsound==1.2.2 AppKit

def sound():
    playsound.playsound('sounds/ChessMove1.mp3')

print("Call constructor")
board = Board()

board.print_board()


print("#####################################################")
print("Check test")
print("#####################################################")
#board.is_check(0)

bishop = board.get_board()[0][2]

list_playable = board.get_board()[0][2].get_playable_pos(board)


for e in list_playable:
    print(e)

board.print_board()