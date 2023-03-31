from tkinter import *
from engine.board import Board
import playsound # pip install playsound==1.2.2 AppKit

def sound():
    playsound.playsound('sounds/ChessMove1.mp3')

print("Call constructor")
board = Board()
board.print_board()

print("#####################################################")
print(board.play(1, [1, 4], [2, 4]))
print("\n\nMOVE\n\n")
board.print_board()
sound()

print("#####################################################")
print(board.play(1, [0, 3], [4, 5]))
print("\n\nMOVE\n\n")
board.print_board()

print("#####################################################")
print(board.play(1, [0, 0], [2, 0]))
print("\n\nMOVE\n\n")
board.print_board()