balance = 100
balance = balance * 1.05
balance = balance * 1.05
balance = balance * 1.05
chumpChange = balance % .01
balance = balance - chumpChange
print("The savings account's balance is $", balance, sep = "")


balance = 100
balance = balance * 1.05
balance = balance * 1.05
balance = balance * 1.05
print("The savings account's balance is $", format(balance, ".5f"), sep = "")
