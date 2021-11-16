__author__ = 'guinnc'

'''
Create some random bank accounts.
'''
import random
from BankAccount import *

outfile = open("accounts.txt", "w")

firstNames = []
firstNameFile = open("FirstNames.txt", "r")
for line in firstNameFile:
    firstNames.append(line.strip())

lastNames = []
lastNameFile = open("LastNames.txt", "r")
for line in lastNameFile:
    lastNames.append(line.strip())

for i in range(100):
    first = firstNames[random.randint(0, len(firstNames) - 1)]
    last = lastNames[random.randint(0, len(lastNames) - 1)]
    acct = BankAccount(first, last, random.randint(1, 10000))
    interest = acct.calculateInterest()
    print(acct)
    print("The interest is: ", interest)
    outfile.write(str(acct) + "\n")

print("Done!")