from tkinter import *
from engine.board import Board
import playsound # pip install playsound==1.2.2

def sound():
    playsound.playsound('sounds\ChessMove1.mp3')

print("Call constructor")
board = Board()

board.print_board()


print("#####################################################")
print(board.play(0, [0, 6], [0, 5]))
print("\n\nMOVE\n\n")
board.print_board()
sound()

print("#####################################################")
print(board.play(1, [4, 4], [0, 4]))
print("MOVE\n\n")
board.print_board()
sound()