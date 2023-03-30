# type: ignore
from tkinter import *
from PIL import ImageTk, Image

# Definitions of main window
root = Tk()
root.geometry("800x800")
root.title("Chess Royale")

frame = Frame(root)
frame.pack()

# Definition of canvas
canvas = Canvas(frame, bg="black", width = 800, height = 800)
canvas.pack(expand = YES) 

# Adding the board
board = PhotoImage(file = "images\standard-pack\Board.png")
canvas.create_image(400, 400, image = board)

# Adding pieces to the board
# White
WP = PhotoImage(file = "images\standard-pack\WP.png")
WR = PhotoImage(file = "images\standard-pack\WR.png")
WB = PhotoImage(file = "images\standard-pack\WB.png")
WQ = PhotoImage(file = "images\standard-pack\WQ.png")
WK = PhotoImage(file = "images\standard-pack\WK.png")
WN = PhotoImage(file = "images\standard-pack\WN.png")

canvas.create_image(0, 600, anchor = NW, image = WP)
canvas.create_image(100, 600, anchor = NW, image = WP)
canvas.create_image(200, 600, anchor = NW, image = WP)
canvas.create_image(300, 600, anchor = NW, image = WP)
canvas.create_image(400, 600, anchor = NW, image = WP)
canvas.create_image(500, 600, anchor = NW, image = WP)
canvas.create_image(600, 600, anchor = NW, image = WP)
canvas.create_image(700, 600, anchor = NW, image = WP)
canvas.create_image(0, 700, anchor = NW, image = WR)
canvas.create_image(100, 700, anchor = NW, image = WN)
canvas.create_image(200, 700, anchor = NW, image = WB)
canvas.create_image(300, 700, anchor = NW, image = WQ)
canvas.create_image(400, 700, anchor = NW, image = WK)
canvas.create_image(500, 700, anchor = NW, image = WB)
canvas.create_image(600, 700, anchor = NW, image = WN)
canvas.create_image(700, 700, anchor = NW, image = WR)

# Black
BP = PhotoImage(file = "images\standard-pack\BP.png")
BR = PhotoImage(file = "images\standard-pack\BR.png")
BB = PhotoImage(file = "images\standard-pack\BB.png")
BQ = PhotoImage(file = "images\standard-pack\BQ.png")
BK = PhotoImage(file = "images\standard-pack\BK.png")
BN = PhotoImage(file = "images\standard-pack\BN.png")

canvas.create_image(0, 100, anchor = NW, image = BP)
canvas.create_image(100, 100, anchor = NW, image = BP)
canvas.create_image(200, 100, anchor = NW, image = BP)
canvas.create_image(300, 100, anchor = NW, image = BP)
canvas.create_image(400, 100, anchor = NW, image = BP)
canvas.create_image(500, 100, anchor = NW, image = BP)
canvas.create_image(600, 100, anchor = NW, image = BP)
canvas.create_image(700, 100, anchor = NW, image = BP)
canvas.create_image(0, 0, anchor = NW, image = BR)
canvas.create_image(100, 0, anchor = NW, image = BN)
canvas.create_image(200, 0, anchor = NW, image = BB)
canvas.create_image(300, 0, anchor = NW, image = BQ)
canvas.create_image(400, 0, anchor = NW, image = BK)
canvas.create_image(500, 0, anchor = NW, image = BB)
canvas.create_image(600, 0, anchor = NW, image = BN)
canvas.create_image(700, 0, anchor = NW, image = BR)

# Starting the window
root.mainloop()