def convertB(dig):
    halp = []
    while dig > 0:
        binary = dig % 2
        halp.append(binary)
        dig = dig // 2
    halp.reverse()
    return halp

def convertH(dig):
    baseStanding = 1
    halp = []
    while dig > 0:
        binary = dig % 16
        if binary >= 10:
            if binary == 10:
                binary = "A"
            elif binary == 11:
                binary = "B"
            elif binary == 12:
                binary = "C"
            elif binary == 13:
                binary = "D"
            elif binary == 14:
                binary = "E"
            elif binary == 15:
                binary = "F"
        halp.append(binary)
        dig = dig // 16
    halp.reverse()
    return halp

digit = int(input("Please input a base 10 value: "))
choice = "no"
while choice != "Binary" and choice != "Hexa":
    choice = str(input("Please input Binary or Hexa: "))
if choice == "Binary":
    finalHalp = convertB(digit)
else:
    finalHalp = convertH(digit)
print(finalHalp)
