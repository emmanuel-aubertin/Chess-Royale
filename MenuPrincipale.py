import tkinter
from tkinter import *
# Definitions of main window

item_selec=False
item_possibilit=None
canvas_item_possibility=list
piece=None
game_finish=False

#Fonction to print futur positon of our piece
def callback(event, item_select=item_selec, item_possibility=item_possibilit, piece=piece):
    fini=False
    #Check if item was not selected
    if(item_select==False):
        value_x=0
        value_y=0
        x_done=False
        y_done=False
        # Calcul position in our board
        for i in range(8):
            if(i*100>event.x and x_done!=True):
                value_x=(i-1)*100
                x_done=True
            elif(i*100==event.x and x_done!=True):
                value_x = (i) * 100
                x_done = True
            if (i * 100 > event.x and y_done!=True):
                value_x = (i - 1) * 100
                y_done = True
            elif (i * 100 == event.y and y_done!=True):
                value_y = (i) * 100
                y_done = True
            if(y_done and x_done):
                break
        piece=board.get(value_x,value_y)
        #If we find a piece we get is different possibility
        if(piece!=None):
            item_possibility=board.get(value_x,value_y).possibility
            for i in item_possibility:
                position=i.get_position()
                myoval=canvas.create_oval((position[0]*100)+30,(position[1]*100)+30,((position[0]+1)*100)-30,((position[1]+1)*100)-30)
                canvas_item_possibility.append(myoval)
    else:#Check if a item is select
        value_x = 0
        value_y = 0
        x_done = False
        y_done = False
        #Calcul position in our board
        for i in range(8):
            if (i * 100 > event.x and x_done != True):
                value_x = (i - 1) * 100
                x_done = True
            elif (i * 100 == event.x and x_done != True):
                value_x = (i) * 100
                x_done = True
            if (i * 100 > event.x and y_done != True):
                value_x = (i - 1) * 100
                y_done = True
            elif (i * 100 == event.y and y_done != True):
                value_y = (i) * 100
                y_done = True
            if (y_done and x_done):
                break
        piece_resultat=board.get(value_x,value_y)
        #Search if where we clicke was a possibility
        for i in item_possibility:
            if(i[0]==value_x and i[1]==value_y):
                piece.go(value_x,value_y)
                #Check if the game is finish
                if(board.is_finish()):
                    game_finish=True
                    fini=True
                    break
                piece=None
                #Destroy every possibility in the board
                for j in canvas_item_possibility:
                    canvas.destroy(j)
                item_select=False
                item_possibility=None
                fini=True
                resultat=minmax(10,board,1)
                resultat[2].go(resultat[1][0],resultat[1][0])
                if (board.is_finish()):
                    fini = True
                    game_finish=True
                break
        #In the case were you clicked in another piece
        if (piece_resultat != piece and fini==True):
            #Check if you clicked was a piece . So we change possibility
            if(piece_resultat!=None):
                for j in canvas_item_possibility:
                    canvas.destroy(j)
                piece = piece_resultat
                item_possibility = board.get(value_x, value_y).possibility
                for i in item_possibility:
                    position = i.get_position()
                    myoval = canvas.create_oval((position[0] * 100) + 30, (position[1] * 100) + 30,
                                                ((position[0] + 1) * 100) - 30, ((position[1] + 1) * 100) - 30)
                    canvas_item_possibility.append(myoval)


root = Tk()
root.geometry("800x800")
root.title("Chess Royale")

frame = Frame(root)
frame.pack()

# Definition of canvas
canvas = Canvas(frame,width=800, height=800)
canvas.pack(expand = YES)

# Adding the board
#board = PhotoImage(file = "images\standard-pack\Board.png")
#canvas.create_image(400, 400, image = board)
def transition_second_screen():
    root.geometry("800x800")
    root.title("Try")

    canvas.bind("<Button-1>",callback)

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


    canvas.create_image(0, 600, anchor=NW, image=WP)
    canvas.tag_bind(WP,'<Button-1>',callback)
    canvas.create_image(100, 600, anchor=NW, image=WP)
    canvas.create_image(200, 600, anchor=NW, image=WP)
    canvas.create_image(300, 600, anchor=NW, image=WP)
    canvas.create_image(400, 600, anchor=NW, image=WP)
    canvas.create_image(500, 600, anchor=NW, image=WP)
    canvas.create_image(600, 600, anchor=NW, image=WP)
    canvas.create_image(700, 600, anchor=NW, image=WP)
    canvas.create_image(0, 700, anchor=NW, image=WR)
    canvas.create_image(100, 700, anchor=NW, image=WN)
    canvas.create_image(200, 700, anchor=NW, image=WB)
    canvas.create_image(300, 700, anchor=NW, image=WQ)
    canvas.create_image(400, 700, anchor=NW, image=WK)
    canvas.create_image(500, 700, anchor=NW, image=WB)
    canvas.create_image(600, 700, anchor=NW, image=WN)
    canvas.create_image(700, 700, anchor=NW, image=WR)

    # Black
    BP = PhotoImage(file="images\standard-pack\BP.png")
    BR = PhotoImage(file="images\standard-pack\BR.png")
    BB = PhotoImage(file="images\standard-pack\BB.png")
    BQ = PhotoImage(file="images\standard-pack\BQ.png")
    BK = PhotoImage(file="images\standard-pack\BK.png")
    BN = PhotoImage(file="images\standard-pack\BN.png")

    canvas.create_image(0, 100, anchor=NW, image=BP)
    canvas.create_image(100, 100, anchor=NW, image=BP)
    canvas.create_image(200, 100, anchor=NW, image=BP)
    canvas.create_image(300, 100, anchor=NW, image=BP)
    canvas.create_image(400, 100, anchor=NW, image=BP)
    canvas.create_image(500, 100, anchor=NW, image=BP)
    canvas.create_image(600, 100, anchor=NW, image=BP)
    canvas.create_image(700, 100, anchor=NW, image=BP)
    canvas.create_image(0, 0, anchor=NW, image=BR)
    canvas.create_image(100, 0, anchor=NW, image=BN)
    canvas.create_image(200, 0, anchor=NW, image=BB)
    canvas.create_image(300, 0, anchor=NW, image=BQ)
    canvas.create_image(400, 0, anchor=NW, image=BK)
    canvas.create_image(500, 0, anchor=NW, image=BB)
    canvas.create_image(600, 0, anchor=NW, image=BN)
    canvas.create_image(700, 0, anchor=NW, image=BR)
    canvas.pack()
    canvas.create_oval(330, 330, 370, 370,fill="black")
    button_game.destroy()
    button_quit.destroy()



    root.mainloop()

#Button for transition
button_game = Button(frame,text ="1vsAI",command=transition_second_screen)
button_game.place(x=400,y=0)

#Button to quit
button_quit = Button(frame,text ="Quitter",command=root.destroy)
button_quit.place(x=400,y=20)
# Starting the window
root.mainloop()
