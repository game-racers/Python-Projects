import random

rolls = 1
while rolls <= 5:
    val = random.randint(1,6)
    if rolls == 1:
        print("On your first roll, you got a", val)
    elif rolls == 2:
        print("On your second roll, you got a", val)
    elif rolls == 3:
        print("On your third roll, you got a", val)
    elif rolls == 4:
        print("On your fourth roll, you got a", val)
    elif rolls == 5:
        print("On your fifth roll, you got a", val)
    rolls = rolls + 1
    

