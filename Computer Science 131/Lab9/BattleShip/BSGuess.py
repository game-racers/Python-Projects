import fileWriter

guessList = []

turtle = False

def guess(BattleBoard, EnemyShips, shipz):
    guessList = shipz
    oK = False
    turtle = False
    while oK == False:
        userInput = str(input('Where shall we shoot Captain? '))
        oK = guessChecker(userInput, EnemyShips, BattleBoard, shipz)
    if turtle == False:
        didItHit(userInput, BattleBoard, EnemyShips, shipz)

def guessChecker(userInput, EnemyShips, BattleBoard, shipz):
    guessList = shipz
    if userInput == 'save' or userInput == 'Save':
        fileWriter.save(guessList, EnemyShips, BattleBoard, shipz)
        print('saving...')
        turtle = True
        return False
    if [ord(userInput[0])-65,int(userInput[1:])-1] in guessList:
        print('Where ye be Captain? We shot thur only a mo\' ago!')
        return False
    if ord(userInput[0]) >= ord('A') and ord(userInput[0]) <= ord('J'):
        if int(userInput[1:]) <= 10:
            return True
    return False

def didItHit(userInput, board, EnemyShips, shipz):
    guessList = shipz
    x = ord(userInput[0]) - 65
    y = int(userInput[1:]) - 1
    guessList.append([x,y])
    Lego = False
    for i in range(0,5):
        for j in range(len(EnemyShips[i])):
            if EnemyShips[i][j] == [x,y]:
                m = i
                n = j
                Lego = True
    if Lego == True:
        board[x][y] = 'O'
        print('Twas a hit Captain!')
        del EnemyShips[m][n]
        if EnemyShips[m] == []:
            print('You sunk a Ship!')
    else:
        board[x][y] = 'X'
        print('Ye mist Captain!')
