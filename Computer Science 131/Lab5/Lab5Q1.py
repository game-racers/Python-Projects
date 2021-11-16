word1 = str(input("Input the first word M'Lord: "))
mario = [word1]
cont = str(input("Do you wish to continue inputing words? "))
while cont == "yes" or cont == "Yes":
    word = str(input("Now another one: "))
    mario.append(word)
    cont = str(input("Do you wish to continue inputing words? "))
mario.sort()
print(mario)
