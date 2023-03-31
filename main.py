from tkinter import *
from engine.board import Board

print("Call constructor")
board = Board()

board.print_board()
print("#####################################################")
print(board.play(1, [1, 1], [2, 1]))
print("\n\nMOVE\n\n")
board.print_board()

print("#####################################################")
print(board.play(1, [0, 2], [2, 0]))
print("\n\nMOVE\n\n")
board.print_board()


print("#####################################################")
print(board.play(1, [2, 0], [7, 4]))
print("\n\nMOVE\n\n")
board.print_board()

