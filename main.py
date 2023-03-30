from tkinter import *
from engine.board import Board

print("Call constructor")
board = Board()

board.print_board()
board.get_board()
board.play(0, [6, 0], [5, 0])
print("\n\nMOVE\n\n")
board.print_board()

window = Tk()
window.geometry("700x700")
window.title('Chess Royale')
window.mainloop()