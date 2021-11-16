row = int(input("Pyramid Size O' Holy One: "))
col = 2*(row-1)+1
cCount = 0
cRow = row
spaces = 0
first = 0
while cRow >= 0:
    spaces = row - cRow
    if first == 0:
        while spaces > 0:
            print(" ", end = "")
            spaces -= 1
        first = 1
    while cCount < col:
        print(cRow, end = "")
        cCount += 1
    print("")
    col -= 2
    cCount = 0
    cRow -= 1
    first = 0
print("End of Loop")
