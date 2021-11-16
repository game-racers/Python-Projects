print("In order to print all integers between two values, you need to tell ")
print("us which 2 values you want. Input a Lower and an Upper bound. ")
print("The two values can be in any (order)")

a = int(input("Input a value: "))
b = int(input("Input a second value: "))

while a < b:
    print(a)
    a = a + 1
while a > b:
    print(b)
    b = b + 1

print(a)

print("That is the range between your two values")
