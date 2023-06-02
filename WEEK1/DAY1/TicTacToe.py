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

def AI():
    validMove = [i for i in range(9) if i not in (O+X)]
    V = [-100]*9
    for m in validMove:
        tempX = X + [m]
        V[m],forceMove = evalOX(O,tempX)
        if(len(forceMove)>0):
            move = [i for i in forceMove if i in validMove]
            return random.choice(move)
    maxV = max(V)
    print(V)
    imaxV = [i for i, j in enumerate(V) if j == maxV]
    return random.choice(imaxV)
        
def evalOX(O,X):
    SO,SX,forceMove = calSOX(O,X)
    return 1+SX-SO,forceMove
def calSOX(O,X):
    SO = 0
    SX = 0
    forceMove = []
    for w in win:
        o = [i in O for i in w]
        x = [i in X for i in w]
        if not any(x):
            nO = o.count(True)
            SO += nO
            if nO == 2:
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
    displayOX()
    while True:
        move = input("Your move: ")
        while  (move.isdigit() == False) or int(move) in O+X or int(move) not in range(9):
            move = input("Invalid move, please input again: ")
        move = int(move)
        O.append(move)
        if checkWin(O):
            print("You win")
            break
        if len(O)+len(X) == 9:
            print("Draw")
            break
        X.append(AI())
        displayOX()
        if checkWin(X):
            print("I win")
            break
        if len(O)+len(X) == 9:
            print("Draw")
            break
