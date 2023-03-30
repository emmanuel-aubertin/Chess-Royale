
def miximaxe(nbhauteur,noeud,color):
    if nbhauteur<0:
        return evaluation(getBoard,color)
    if color=="white":
        boardWhite= getWhite()
        maxi=0
        position=get_playable_post(board)
        for j in position:
            board_copie=board
            board_copie[noeud.pos[0]][noeud.pos[1]]="null"
            board_copie[j[0]][j[1]]=i.get_type
            boardBlack = getBlack()
            for x in boardBlack:
                resultat=miximaxe(nbhauteur-1,x,"black")
                if resultat > max :
                    max=resultat
    else:
        boardBlack = getBlack()
        min = 999999999
        position = get_playable_post(board)
        for j in position:
            board_copie = board
            board_copie[noeud.pos[0]][noeud.pos[1]] = "null"
            board_copie[j[0]][j[1]] = i.get_type
            boardWhite= getWhite()
            for x in boardWhite:
                resultat = miximaxe(nbhauteur-1,x, "white")
                if resultat < min:
                    min = resultat