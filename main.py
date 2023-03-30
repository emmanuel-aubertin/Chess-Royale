from tkinter import *
from engine.board import Board

print("Call constructor")
board = Board()

board.print_board()

window = Tk()
window.geometry("700x700")
window.title('Chess Royale')
window.mainloop()

