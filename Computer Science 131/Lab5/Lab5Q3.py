word = float(input("Select your first number: "))
mario = [word]
print(mario)
print("Average:", word)
cont = str(input("Do you wish to continue inputing numbers? "))
while cont == "yes" or cont == "Yes":
    val = float(input("Now another number: "))
    length = len(mario)
    n = 0
    while n < length:
        if val < mario[n]:
            mario.insert(n,val)
            n = length
        elif val >= mario[length - 1]:
            mario.append(val)
            n = length
        n += 1
    print(mario)
    Sum = sum(mario)
    avg = Sum / (length + 1)
    print("Average:", avg)
    cont = str(input("Do you wish to continue inputing numbers? "))
