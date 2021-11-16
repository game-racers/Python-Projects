print("This program will convert base 10 to binary.")

dig = int(input("Input a base 10 value: "))
baseStanding = 1
halp = 0
while dig > 0:
    print(dig, "% 2")
    binary = dig % 2
    if binary == 1:
        print("There is a remainder so I multiply 1 by the base it")
        print("will be placed in")
        print(halp, "= 1 *", baseStanding, "+", halp)
        halp = 1 * baseStanding + halp
        print("Binary is now equal to", halp)
    print(dig, "// 2")
    dig = dig // 2
    baseStanding = baseStanding * 10

print("Binary value: ", halp)
    
