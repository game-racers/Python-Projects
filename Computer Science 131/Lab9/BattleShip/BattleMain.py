import BattleShip
import BSGuess
import fileWriter

loaded = False
game = True
userInput = str(input('Wanna Load your game? (Y/N)'))
try:
    if userInput == 'y' or userInput == 'Y' or userInput == 'yes' or userInput == 'Yes':
        a = fileWriter.load()
        EnemyShips = a[0]
        guessList = a[1]
        #print(EnemyShips)
        BattleBoard = list(a[2])
        for m in range(0,10):
            for n in range(0,10):
                if BattleBoard[m][n] == 0 or BattleBoard[m][n] == '0':
                    BattleBoard[m][n] = 0
        loaded = True
    else:        
        BattleBoard = BattleShip.firstBoard()
        EnemyShips = BattleShip.placeShips()
        guessList = []
except FileNotFoundError:
    BattleBoard = BattleShip.firstBoard()
    EnemyShips = BattleShip.placeShips()
    guessList = []

while game == True:
    BattleShip.buildBoard(BattleBoard)
    BSGuess.guess(BattleBoard, EnemyShips, guessList)
    if EnemyShips == [[],[],[],[],[]]:
        cont = str(input('You Sunk em All! Good Job, Wanna Play Again? Y/N '))
        if cont == 'y' or cont == 'Y':
            BattleBoard = BattleShip.firstBoard()
            EnemyShips = BattleShip.placeShips()
        else:
            game == False
