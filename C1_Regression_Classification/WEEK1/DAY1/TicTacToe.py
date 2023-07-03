# not use minimax algo so it is not perfect move
import numpy as np
import random

O = []
X = []
win = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8},
       {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
       {0, 4, 8}, {2, 4, 6}]


def checkWin(player):
    player_set = set(player)
    # "<=" is the symbol for issubset
    return any((win_set <= player_set) for win_set in win)


def displayOX():
    OX = np.array([' ']*9)
    OX[O] = 'O'
    OX[X] = 'X'
    print(OX.reshape(3, 3))

def algo():
    validMove = [i for i in range(9) if i not in (O+X)]
    V = [-100]*9
    for m in validMove:
        if checkWin(X + [m]):  # If can win with this move, do it
            return m
    for m in validMove:  # Original strategy
        V[m],forceMove = evalOX(O,X + [m])
        if(len(forceMove)>0):
            move = [i for i in forceMove if i in validMove]
            return random.choice(move)
    maxV = [i for i, j in enumerate(V) if j == max(V)]
    return random.choice(maxV)

def evalOX(O,X):
    SO,SX,forceMove = calSOX(O,X)
    return 1+SX-SO,forceMove
def calSOX(O,X):
    SO = SX = 0
    forceMove = []
    for w in win:
        o = [i in O for i in w]
        x = [i in X for i in w]
        if not any(x):
            SO += o.count(True)
            if(o.count(True)==2):
                forceMove = w
        if not any(o):
            SX += x.count(True)
    return SO,SX,forceMove
    
if __name__ == "__main__":
    print("Welcome to XO game")
    print("You are O, and I am X")
    print("You will start first")
    print("Please input number 0-8 to put your O")
    print(" 0 | 1 | 2 ")
    print("---+---+---")
    print(" 3 | 4 | 5 ")
    print("---+---+---")
    print(" 6 | 7 | 8 ")
    print("Input -1 to exit")
    while True:
        move = input("Your move (enter a number 0-8): ")
        try:
            move = int(move)
            if move == -1:
                break
            if move not in range(9) or move in O+X:
                print("Invalid move, please try again.")
                continue
        except ValueError:
            print("Invalid move, please try again.")
            continue
        O.append(move) # if optimal vs optimal expected : draw
        if checkWin(O):
            print("You win")
            break
        if len(O)+len(X) == 9:
            print("Draw")
            break
        X.append(algo())
        displayOX()
        if checkWin(X):
            print("I win")
            break
        if len(O)+len(X) == 9:
            print("Draw")
            break