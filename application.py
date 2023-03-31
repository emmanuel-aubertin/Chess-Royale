import tkinter
from tkinter import *
from engine.board import Board as  Board

# Definitions of main window

board2=Board()

item_select=[False]
item_possibilit=[None]
canvas_item_possibility=[]
piece=[None]
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

# Adding the board
#board = PhotoImage(file = "images\standard-pack\Board.png")
#canvas.create_image(400, 400, image = board)
def transition_second_screen():
    root.geometry("800x800")
    root.title("Try")

    # Adding the board
    board = PhotoImage(file="images\standard-pack\Board.png")
    canvas.create_image(400, 400, image=board)

    # Adding pieces to the board
    # White
    WP = PhotoImage(file="images\standard-pack\WP.png")
    WR = PhotoImage(file="images\standard-pack\WR.png")
    WB = PhotoImage(file="images\standard-pack\WB.png")
    WQ = PhotoImage(file="images\standard-pack\WQ.png")
    WK = PhotoImage(file="images\standard-pack\WK.png")
    WN = PhotoImage(file="images\standard-pack\WN.png")

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
    BP = PhotoImage(file="images\standard-pack\BP.png")
    BR = PhotoImage(file="images\standard-pack\BR.png")
    BB = PhotoImage(file="images\standard-pack\BB.png")
    BQ = PhotoImage(file="images\standard-pack\BQ.png")
    BK = PhotoImage(file="images\standard-pack\BK.png")
    BN = PhotoImage(file="images\standard-pack\BN.png")

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

    canvs_list=[[BR1,BN1,BB1,BQ1,BK1,BB2,BN2,BR2],
                [BP1,BP2,BP3,BP4,BP5,BP6,BP7,BP8],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [WR1,WN1,WB1,WQ1,WK1,WB2,WN2,WR2],
                [WP1,WP2,WP3,WP4,WP5,WP6,WP7,WP8]]

    def exception(event, item_possibility=item_possibilit, piece=piece, item_select=item_select, canvs_list=canvs_lis):
        print(item_select[0])
        fini = False
        # Check if item was not selected
        if (item_select[0] == False):
            value_x = 0
            value_y = 0
            x_done = False
            y_done = False
            # Calcul position in our board
            for i in range(8):
                if (i * 100 > event.x and x_done != True):
                    value_x = (i - 1)
                    x_done = True
                elif (i * 100 == event.x and x_done != True):
                    value_x = (i)
                    x_done = True
                if (i * 100 > event.y and y_done != True):
                    value_y = (i - 1)
                    y_done = True
                elif (i * 100 == event.y and y_done != True):
                    value_y = (i)
                    y_done = True
                if (y_done and x_done):
                    break
            piece[0] = board2.get_board()[value_y][value_x]
            # If we find a piece we get is different possibility
            if (piece[0] != None):
                item_possibility[0] = piece[0].get_playable_pos(board2)
                if (item_possibility[0] != None):
                    for i in item_possibility[0]:
                        position = i
                        canvas.create_oval((position[1] * 100) + 30, (position[0] * 100) + 30,
                                           ((position[1] + 1) * 100) - 30, ((position[0] + 1) * 100) - 30, fill="black")
                        myoval = canvas.create_oval((position[1] * 100) + 30, (position[0] * 100) + 30,
                                                    ((position[1] + 1) * 100) - 30, ((position[0] + 1) * 100) - 30,
                                                    fill="black")
                        canvas_item_possibility.append(myoval)
                        item_select[0] = True
        else:  # Check if a item is select
            value_x = 0
            value_y = 0
            x_done = False
            y_done = False
            # Calcul position in our board
            for i in range(8):
                if (i * 100 > event.x and x_done != True):
                    value_x = (i - 1)
                    x_done = True
                elif (i * 100 == event.x and x_done != True):
                    value_x = (i)
                    x_done = True
                if (i * 100 > event.y and y_done != True):
                    value_y = (i - 1)
                    y_done = True
                elif (i * 100 == event.y and y_done != True):
                    value_y = (i)
                    y_done = True
                if (y_done and x_done):
                    break
            piece_resultat = board2.get_board()[value_x][value_y]
            # Search if where we clicke was a possibility
            print(value_x, " ", value_y)
            print(item_possibility)
            for j in item_possibility:
                for i in j:
                    print(i)
                    print(value_x, " ", value_y)
                    if (i[0] == value_y and i[1] == value_x):
                        print(piece[0].pos[0], " ", piece[0].pos[1])
                        print(canvs_list)
                        board2.get_board()[piece[0].pos[0]][piece[0].pos[1]] = piece[0]
                        canvas.itemconfigure(canvs_list[piece[0].pos[0]][piece[0].pos[1]], x=value_y, y=value_x)
                        piece[0].pos = [value_y, value_x]
                        # Check if the game is finish
                        # if(board.is_finish()):
                        #   game_finish=True
                        #  fini=True
                        # break
                        piece[0] = None
                        # Destroy every possibility in the board
                        for j in canvas_item_possibility:
                            print(j)
                            canvas.delete(j)
                        item_select = False
                        item_possibility = None
                        fini = True
                        # resultat=minmax(10,board,1)
                        # resultat[2].go(resultat[1][0],resultat[1][0])
                        # if (board.is_finish()):
                        #    fini = True
                        #    game_finish=True
                        break
            # In the case were you clicked in another piece
            if (piece_resultat != piece and fini != True):
                # Check if you clicked was a piece . So we change possibility
                if (piece_resultat != None):
                    for j in canvas_item_possibility:
                        canvas.delete(j)
                    piece = piece_resultat
                    item_possibility = board.get(value_x, value_y).possibility
                    for i in item_possibility:
                        position = i.get_position()
                        myoval = canvas.create_oval((position[0] * 100) + 30, (position[1] * 100) + 30,
                                                    ((position[0] + 1) * 100) - 30, ((position[1] + 1) * 100) - 30)
                        canvas_item_possibility.append(myoval)

    canvas.bind("<Button-1>", exception)
    canvas.pack()
    canvas.create_oval(330, 330, 370, 370,fill="black")
    button_game.destroy()
    button_quit.destroy()
    root.mainloop()

#Button for transition
logo = PhotoImage(file="images\logo2.png")
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