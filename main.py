endgame = 0

pawnEvalWhite = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0
]
pawnEvalBlack = list(reversed(pawnEvalWhite))

knightEval = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50
]

bishopEvalWhite = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20
]
bishopEvalBlack = list(reversed(bishopEvalWhite))

rookEvalWhite = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0
]
rookEvalBlack = list(reversed(rookEvalWhite))

queenEval = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20
]

kingEvalWhite = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30
]
kingEvalBlack = list(reversed(kingEvalWhite))

kingEvalEndGameWhite = [
    50, -30, -30, -30, -30, -30, -30, -50,
    -30, -30, 0, 0, 0, 0, -30, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -20, -10, 0, 0, -10, -20, -30,
    -50, -40, -30, -20, -20, -30, -40, -50
]
kingEvalEndGameBlack = list(reversed(kingEvalEndGameWhite))

board = [
    ["bt", "bkn", "bb", "bk", "bq", "bb", "bkn", "bt"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["t", "kn", "b", "k", "q", "b", "kn", "t"]
]


def getScore(piece_list):
    score = 0
    for i in piece_list:
        x = i.pos[0]
        y = i.pos[1]
        type = i.get_type()
        if (type == "P"):
            score += (10 + (pawnEvalWhite[x][y]) / 2)
            continue
        if (type == "N"):
            score += (30 + (knightEval[x][y]) / 2)
            continue
        if (type == "B"):
            score += (30 + (bishopEvalWhite[x][y]) / 2)
            continue
        if (type == "R"):
            score += (50 + (rookEvalWhite[x][y]) / 2)
            continue
        if (type == "Q"):
            score += (90 + (queenEval[x][y]) / 2)
            continue
        if (type == "K"):
            if (endgame):
                score += 900 + (kingEvalEndGameWhite[x][y]) / 2
            else:
                score += 900 + (kingEvalWhite[x][y]) / 2
            continue


def getScoreBlack(piece_list):
    score = 0
    for i in piece_list:
        x = i.pos[0]
        y = i.pos[1]
        type = i.get_type()
        if (type == "P"):
            score -= (-10 - (pawnEvalBlack[x][y]) / 2)
            continue
        if (type == "N"):
            score -= (-30 - (knightEval[x][y]) / 2)
            continue
        if (type == "B"):
            score -= (-30 - (bishopEvalBlack[x][y]) / 2)
            continue
        if (type == "R"):
            score -= (-50 - (rookEvalBlack[x][y]) / 2)
            continue
        if (type == "Q"):
            score -= (-90 - (queenEval[x][y]) / 2)
            continue
        if (type == "K"):
            if (endgame):
                score -= 900 - (kingEvalEndGameBlack[x][y]) / 2
            else:
                score -= 900 - (kingEvalBlack[x][y]) / 2
            continue


def evaluate(piece_list, color):
    if not color:  # white
        return getScore(piece_list)
    else:
        return getScoreBlack(piece_list)


def minmax(nbhauteur, board, color):  # Board = array of piecies
    piece_list = board.get_piece_list(color)
    movement = None
    piece = None
    if nbhauteur < 0:
        return evaluate(piece_list, color), movement, piece
    if not color:  # white
        max = 0
        for i in piece_list:
            move_list = i.get_playable_pos()  # Get all moves possible for this piece
            for j in move_list:
                board_copie = board  # Clone the current board

                # Mooving the piece
                board_copie[i.pos[0]][i.pos[1]] = None
                board_copie[j[0]][j[1]] = i

                # Editing the object position
                i.pos = j

                if (board_copie.is_checkmate()):
                    max = 10000
                    movement = j
                    piece = i
                    return max, movement, piece

                resultat = minmax(nbhauteur - 1, board_copie, not color)
                if resultat[0] > max:
                    max = resultat[0]
                    movement = j
                    piece = i
    else:  # black
        min = 999999999
        for i in piece_list:
            move_list = i.get_playable_pos()  # Get all moves possible for this piece
            for j in move_list:
                board_copie = board  # Clone the current board

                # Mooving the piece
                board_copie[i.pos[0]][i.pos[1]] = None
                board_copie[j[0]][j[1]] = i

                # Editing the object position
                i.pos = j

                if (board_copie.is_checkmate()):
                    min = -10000
                    movement = j
                    piece = i
                    return min, movement, piece

                resultat = minmax(nbhauteur - 1, board_copie, not color)
                if resultat[0] < min:
                    min = resultat[0]
                    movement = j
                    piece = i
    if not color:  # white
        return max, movement, piece
    else:
        return min, movement, piece
