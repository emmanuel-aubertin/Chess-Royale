from tkinter import *
from engine.board import Board

print("Call constructor")
board = Board()

board.print_board()
print("#####################################################")
print(board.play(1, [1, 0], [2, 0]))
print("\n\nMOVE\n\n")
board.print_board()



