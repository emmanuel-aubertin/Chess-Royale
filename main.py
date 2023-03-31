from tkinter import *
from engine.board import Board

print("Call constructor")
board = Board()

board.print_board()
print("#####################################################")
print(board.play(0, [0, 6], [0, 5]))
print("\n\nMOVE\n\n")
board.print_board()

print("#####################################################")
print(board.play(1, [4, 4], [3, 4]))
print("MOVE\n\n")
board.print_board()