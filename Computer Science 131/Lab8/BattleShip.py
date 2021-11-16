import turtle
import random

def buildBoard():
    print('HEY')
    board = []
    for j in range(10):
        tempRow = [0,0,0,0,0,0,0,0,0,0]
        board.append(tempRow)
#  |2
#-3 -1 #COMPASS
#  |4
#one 2 wide ship, two 3 wide ships, one 4 wide ship, and one 5 wide ship
def placeShips():
    print('Hello')
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
        boatList.append(boater)
    print(boatList)
        
                
