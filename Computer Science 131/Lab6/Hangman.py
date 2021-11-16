import random

def randomWord(listin):
    word = random.randint(1,49)
    return WordList[random.randint(0,49)]

def build(guessinword,userguess,count):
    if len(userguess) == 0:
        k = 0
        for k in range(len(guessinword)):
            print(" _", end = "")
    else:
        halp = len(userguess)
        phone = False
        winner = 0
        for i in range(len(guessinword)):
            unicorn = False
            for j in range(halp):
                if guessinword[i] == userguess[j]:
                    print("", guessinword[i],  end = "")
                    j += 1
                    unicorn = True
                    phone = True
                    j = halp - 1
                    winner += 1
            if unicorn == False:
                print(" _", end = "")
        if phone == False:
            count += 1
        if winner == len(guessinword):
            count = 8
    print("")
    winner = 0
    return count

def lGuesser(leter):
    while ord(leter) < ord("a") or ord(leter) > ord("z") and (leter not in guesses):
        leter = str(input("What is your guess young one? "))
    return leter

WordList = ['word', 'dice', 'running','track','dell','mac','teal','band','eric','programming',\
            'morse','chrome','computer','music','phone','spine','quick','question','help','seahawk',\
            'mouse','chair','bike','skateboard','board','shoes','water','wheel','bag','bookbag',\
            'hand','finger','game','cushion','card','bin','turtle','extreme','paper','monitor',\
            'legs','suit','feet','paint','travis','fire','printer','scanner','money','lights']
game = 'y'
while game != 'no':
    guesses = []
    Rad = randomWord(WordList)
    print(Rad)
    perfect = False
    print("WELCOME TO THE GUESSING GAME")
    wrong = 0
    build(Rad,guesses,wrong)
    while wrong < 7 or wrong == 8:
        letter = "A"
        letter = lGuesser(letter)
        guesses.append(letter)
        wrong = build(Rad,guesses,wrong)
    if wrong == 7:
        Print("You Lose")
    else:
        Print("You Win")
    game = str(input("Try again? "))
