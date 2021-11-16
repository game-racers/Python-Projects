from BankAccount import *


accounts = []
file = open("accounts.txt", "r")
for line in file:
    tokens = line.split()
    lastName = tokens[0]
    lastName = lastName[0:-1]
    firstName = tokens[1]
    balance = tokens[2]
    balance = balance[1:]
    bal = float(balance)
    acct = BankAccount(firstName, lastName, bal)
    accounts.append(acct)

print("The number of accounts: ", len(accounts))
for a in accounts:
    print(a)


min = accounts[0]
for a in accounts:
    if a.balance < min.balance:
        min = a
print("The account with the smallest balance: ", min)