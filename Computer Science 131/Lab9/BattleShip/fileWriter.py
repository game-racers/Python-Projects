def save(guesses, locations, BattleBoard, Shipz):
    myFile = open('battleShip.txt','w')
    for i in range(len(locations)):
        line = str(locations[i])
        myFile.write(line)
    myFile.write('\n')
    line = str(guesses)
    myFile.write(line)
    myFile.write('\n')
    for j in range(len(BattleBoard)):
        for k in range(len(BattleBoard[j])):
            a = str(BattleBoard[j][k])
            myFile.write(a)
        myFile.write('\n')
    myFile.write('\n')
    myFile.close()


def load():
    board = []
    num = ['0','1','2','3','4','5','6','7','8','9']
    myFile = open('battleShip.txt','r')
    line = myFile.readline()
    loc = [[]]
    jerk = 1
    b = 0
    c = 0
    for n in range(len(line)):
        if line[n] in num:
            if jerk == 1:
                loc[c].append([]) #adds location
                loc[c][b].append(int(line[n]))
                jerk = 2
            else:
                loc[c][b].append(int(line[n]))
                jerk = 1
                b += 1
        elif line[n:n+4] == ']][[':
            loc.append([]) # adds ship
            c += 1
            b = 0
        elif line[n:n+1] == '[]':
            loc.append([]) # adds empty ship
            c += 2
            b = 0
    locations = loc
    nerd = []
    jerk = 1
    line = myFile.readline()
    l = 0
    for m in line:
        if m in num:
            if jerk == 1:
                nerd.append([])
                nerd[l].append(int(m))
                jerk = 2
            else:
                nerd[l].append(int(m))
                jerk = 1
                l += 1
    guesses = nerd
    for i in range(10):
        line = myFile.readline()
        board.append([])
        for j in line:
            if j == 0:
                board[i].append(0)
            else:
                board[i].append(j)
    myFile.close()
    return [locations, guesses, board]
