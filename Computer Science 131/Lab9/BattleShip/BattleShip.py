import turtle
import random

def firstBoard():
    board = []
    for j in range(10):
        tempRow = [0,0,0,0,0,0,0,0,0,0]
        board.append(tempRow)
    return board

def buildBoard(BattleBoard):
    print("   1 2 3 4 5 6 7 8 9 10 ")
    print('   _ _ _ _ _ _ _ _ _ _  ')
    for i in range(0,10):
        print(chr(i+65), end = ' |')
        for k in range(0,10):
            if BattleBoard[i][k] == 0 or BattleBoard[i][k] == '0':
                BattleBoard[i][k] = 0
                print(' ', end = ',')
            else:
                print(BattleBoard[i][k], end = ',')
        print()
    print('C\'mon Captain! Next Shot!')
    
def placeShips():
    boatList = []
    for j in range(1,6):
        head = random.randint(1,2)
        x = random.randint(0,9)
        y = random.randint(0,9)
        if j == 1:
            ship = 2
        elif j == 2 or j == 3:
            ship = 3
        else:
            ship = j
        if head == 1:
            if x + ship <= 10:
                boater = [[x,y],[x+1,y],[x+2,y],[x+3,y],[x+4,y]]
            elif x + ship -1 <= 10:
                boater = [[x-1,y],[x,y],[x+1,y],[x+2,y],[x+3,y]]
            elif x + ship -2 <= 10:
                boater = [[x-2,y],[x-1,y],[x,y],[x+1,y],[x+2,y]]
            elif x + ship -3 <= 10:
                boater = [[x-3,y],[x-2,y],[x-1,y],[x,y],[x+1,y]]
            else:
                boater = [[x-4,y],[x-3,y],[x-2,y],[x-1,y],[x,y]]
        else:
            if y + ship <= 10:
                boater = [[x,y],[x,y+1],[x,y+2],[x,y+3],[x,y+4]]
            elif y + ship -1 <= 10:
                boater = [[x,y-1],[x,y],[x,y+1],[x,y+2],[x,y+3]]
            elif y + ship -2 <= 10:
                boater = [[x,y-2],[x,y-1],[x,y],[x,y+1],[x,y+2]]
            elif y + ship -3 <= 10:
                boater = [[x,y-3],[x,y-2],[x,y-1],[x,y],[x,y+1]]
            else:
                boater = [[x,y-4],[x,y-3],[x,y-2],[x,y-1],[x,y]]
        while ship < 5:
            del boater[len(boater)-1]
            ship += 1
            for i in range(len(boater)):
                if boater[i] in boatList:
                    j -= 1
                    ship -= 1
        boatList.append(boater)
    print(boatList)
    return boatList
