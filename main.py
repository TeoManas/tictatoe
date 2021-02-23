import os
import tkinter

Table = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def viewMatrix():
    print(Table[0] + "|" + Table[1] + "|" + Table[2])
    print(Table[3] + "|" + Table[4] + "|" + Table[5])
    print(Table[6] + "|" + Table[7] + "|" + Table[8])

def chosePos():
    for i in range(8):
        if i % 2 == 0:
            viewMatrix()
            pos = input("Choose empty position(1-9) X : ")
            pos = int(pos)
            if 1 <= pos < 10:
                if Table[pos - 1] != " ":
                    break
                else:
                    Table[pos - 1] = "X"
                    if i >= 2:
                        if checkWin():
                            winStatementX()
                            break
            else:
                break
            os.system('cls')
        else:
            viewMatrix()
            pos = input("Choose empty position(1-9) O : ")
            pos = int(pos)
            if 1 <= pos < 10:
                if Table[pos - 1] != " ":
                    break
                else:
                    Table[pos - 1] = "O"
                    if i >= 2:
                        if checkWin():
                            winStatementO()
                            break
            else:
                break
            os.system('cls')

def checkRow():
    if Table[0] == Table[1] == Table[2] == "O" or Table[0] == Table[1] == Table[2] == "X":
        return True
    elif Table[3] == Table[4] == Table[5] == "O" or Table[3] == Table[4] == Table[5] == "X":
        return True
    elif Table[6] == Table[7] == Table[8] == "O" or Table[6] == Table[7] == Table[8] == "X":
        return True
    else:
        return False

def checkColumns():
    if Table[0] == Table[3] == Table[6] == "O" or Table[0] == Table[3] == Table[6] == "X":
        return True
    elif Table[1] == Table[4] == Table[7] == "O" or Table[1] == Table[4] == Table[7] == "X":
        return True
    elif Table[2] == Table[5] == Table[8] == "O" or Table[2] == Table[5] == Table[8] == "X":
        return True
    else:
        return False

def checkDiag():
    if Table[0] == Table[4] == Table[8] == "O" or Table[0] == Table[4] == Table[8] == "X":
        return True
    elif Table[2] == Table[4] == Table[6] == "O" or Table[2] == Table[4] == Table[6] == "X":
        return True
    else:
        return False

def checkWin():
    if checkRow():
        return True
    if checkColumns():
        return True
    if checkDiag():
        return True
    else:
        return False

def winStatementX():
    print("Congrats. Player X won")

def winStatementO():
    print("Congrats. Player O won")

chosePos()
viewMatrix()
