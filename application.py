from tkinter import *
from engine.board import Board as Board
import playsound # pip install playsound==1.2.2 AppKit

def OST():
    playsound.playsound('sounds/OST.mp3', False)

OST()

def Sound():
    playsound.playsound('sounds/ChessMove1.mp3')

# Definitions of main window
board2=Board()


selected_piece =[None]

canvas_item_possibility=[]

game_finish=[False]
canvs_lis=[None]
#Fonction to print futur positon of our piece

root = Tk()
root.geometry("800x800")
root.title("Chess Royale")

frame = Frame(root)
frame.pack()

# Definition of canvas
canvas = Canvas(frame,width=800, height=800, bg='#b58863')
canvas.pack(expand = YES)

board = PhotoImage(file="images/standard-pack/Board.png")
canvas.create_image(400, 400, image=board)

# Adding the board
#board = PhotoImage(file = "images/standard-pack/Board.png")
#canvas.create_image(400, 400, image = board)
def transition_second_screen():
    root.geometry("800x800")
    root.title("Try")

    # Adding the board
    board = PhotoImage(file="images/standard-pack/Board2.png")
    canvas.create_image(400, 400, image=board)

    # Adding pieces to the board
    # White
    WP = PhotoImage(file="images/standard-pack/WP.png")
    WR = PhotoImage(file="images/standard-pack/WR.png")
    WB = PhotoImage(file="images/standard-pack/WB.png")
    WQ = PhotoImage(file="images/standard-pack/WQ.png")
    WK = PhotoImage(file="images/standard-pack/WK.png")
    WN = PhotoImage(file="images/standard-pack/WN.png")

    WP1=canvas.create_image(0, 600, anchor=NW, image=WP)
    WP2=canvas.create_image(100, 600, anchor=NW, image=WP)
    WP3=canvas.create_image(200, 600, anchor=NW, image=WP)
    WP4=canvas.create_image(300, 600, anchor=NW, image=WP)
    WP5=canvas.create_image(400, 600, anchor=NW, image=WP)
    WP6=canvas.create_image(500, 600, anchor=NW, image=WP)
    WP7=canvas.create_image(600, 600, anchor=NW, image=WP)
    WP8=canvas.create_image(700, 600, anchor=NW, image=WP)
    WR1=canvas.create_image(0, 700, anchor=NW, image=WR)
    WN1=canvas.create_image(100, 700, anchor=NW, image=WN)
    WB1=canvas.create_image(200, 700, anchor=NW, image=WB)
    WQ1=canvas.create_image(300, 700, anchor=NW, image=WQ)
    WK1=canvas.create_image(400, 700, anchor=NW, image=WK)
    WB2=canvas.create_image(500, 700, anchor=NW, image=WB)
    WN2=canvas.create_image(600, 700, anchor=NW, image=WN)
    WR2=canvas.create_image(700, 700, anchor=NW, image=WR)

    # Black
    BP = PhotoImage(file="images/standard-pack/BP.png")
    BR = PhotoImage(file="images/standard-pack/BR.png")
    BB = PhotoImage(file="images/standard-pack/BB.png")
    BQ = PhotoImage(file="images/standard-pack/BQ.png")
    BK = PhotoImage(file="images/standard-pack/BK.png")
    BN = PhotoImage(file="images/standard-pack/BN.png")

    BP1=canvas.create_image(0, 100, anchor=NW, image=BP)
    BP2=canvas.create_image(100, 100, anchor=NW, image=BP)
    BP3=canvas.create_image(200, 100, anchor=NW, image=BP)
    BP4=canvas.create_image(300, 100, anchor=NW, image=BP)
    BP5=canvas.create_image(400, 100, anchor=NW, image=BP)
    BP6=canvas.create_image(500, 100, anchor=NW, image=BP)
    BP7=canvas.create_image(600, 100, anchor=NW, image=BP)
    BP8=canvas.create_image(700, 100, anchor=NW, image=BP)
    BR1=canvas.create_image(0, 0, anchor=NW, image=BR)
    BN1=canvas.create_image(100, 0, anchor=NW, image=BN)
    BB1=canvas.create_image(200, 0, anchor=NW, image=BB)
    BQ1=canvas.create_image(300, 0, anchor=NW, image=BQ)
    BK1=canvas.create_image(400, 0, anchor=NW, image=BK)
    BB2=canvas.create_image(500, 0, anchor=NW, image=BB)
    BN2=canvas.create_image(600, 0, anchor=NW, image=BN)
    BR2=canvas.create_image(700, 0, anchor=NW, image=BR)

    def load_canvas(list):
        canvas.delete("all")
        board = PhotoImage(file="images/standard-pack/Board2.png")
        canvas.create_image(400, 400, image=board)
        canvas.pack()

        for i in range(len(list)):
            for j in range(len(list[0])):
                canvas.create_image(j*100, i*100, anchor=NW, image=list[i][j])
        root.mainloop()


    global canvas_list
    canvas_list=[[BR,BN,BB,BQ,BK,BB,BN,BR],
                [BP,BP,BP,BP,BP,BP,BP,BP],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [WP,WP,WP,WP,WP,WP,WP,WP],
                 [WR,WN,WB,WQ,WK,WB,WN,WR]
                ]

    def get_mouse_pos(event):
        if (len(str(event.x)) == 2):
            x = 0
        else:
            x = int(str(event.x)[0])
        if (len(str(event.y)) == 2):
            y = 0
        else:
            y = int(str(event.y)[0])
        return [x, y]


    def play(event):
        #global selected_piece
        global canvas_list
        if (selected_piece[0] == None):
            for j in canvas_item_possibility:
                canvas.delete(j)

            position = get_mouse_pos(event)
            x = position[0]
            y = position[1]
            game_array = board2.get_board()
            selected_piece[0] = game_array[y][x]
            if (selected_piece[0] == None):
                return
            possible_moves = selected_piece[0].get_playable_pos(board2)
            print(possible_moves)
            for move in possible_moves:
                oval = canvas.create_oval((move[1] * 100) + 30, (move[0] * 100) + 30,
                                            ((move[1] + 1) * 100) - 30, ((move[0] + 1) * 100) - 30,
                                            fill="black")
                canvas_item_possibility.append(oval)
        else:
            position = get_mouse_pos(event)
            x = position[0]
            y = position[1]
            game_array = board2.get_board()
            possible_moves = selected_piece[0].get_playable_pos(board2)
            for move in possible_moves:
                if ([y,x] == move): #The move is valid, we play it
                    for j in canvas_item_possibility:
                        canvas.delete(j)
                    temp = canvas_list[selected_piece[0].pos[0]][selected_piece[0].pos[1]]
                    canvas_list[selected_piece[0].pos[0]][selected_piece[0].pos[1]] = None
                    canvas_list[y][x] = temp
                    print(board2.play(selected_piece[0].team, selected_piece[0].pos, [y, x]))
                    selected_piece[0] = None
                    board2.print_board()
                    load_canvas(canvas_list)
                    return
            #The move was not valid, we update de selected piece
            selected_piece[0] = game_array[y][x]
            return




    canvas.bind("<Button-1>", play)
    canvas.pack()
    button_game.destroy()
    button_quit.destroy()
    root.mainloop()

#Button for transition
logo = PhotoImage(file="images/logo2.png")
canvas.create_image(-100, 0, anchor=NW, image=logo)

button_game = Button(
    frame,
    text = "1 vs AI",
    height = 3,
    width = 20,
    bg = "#f1d9b5",
    command=transition_second_screen)

button_game.place(x = 350, y = 500)

button_quit = Button(
    frame,
    text ="Quitter",
    height = 3,
    width = 20,
    bg = "#f1d9b5",
    command=root.destroy)

button_quit.place(x = 350, y = 600)

def on_enter(e):
    button_game['background'] = '#b58863'

def on_enter2(e):
    button_quit['background'] = '#b58863'

def on_leave(e):
    button_game['background'] = "#f1d9b5"

def on_leave2(e):
    button_quit['background'] = "#f1d9b5"

button_game.bind("<Enter>", on_enter)
button_quit.bind("<Enter>", on_enter2)
button_game.bind("<Leave>", on_leave)
button_quit.bind("<Leave>", on_leave2)

# Starting the window
root.mainloop()