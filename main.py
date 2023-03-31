from tkinter import *
from engine.board import Board

print("Call constructor")
board = Board()

board.print_board()
print("#####################################################")
print(board.play(0, [6, 0], [5, 0]))
print("\n\nMOVE\n\n")
board.print_board()


print("#####################################################")
print(board.play(1, [0, 1], [2, 2]))
print("MOVE\n\n")
board.print_board()