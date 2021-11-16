shopper = []
print("Type Help if you need it.")
pineapples = True
job = str(input("What is the next mission Master? "))
while pineapples == True:
    if job == "help" or job == "Help":
        print("Type Help to get to the Help Screen.")
        print("Type Add to add an item to your list.")
        print("Type Insert to add an item to a particular")
        print("spot in the list.")
        print("Type Replace to replace a certain item within")
        print("the list with a different item.")
        print("Type Delete to delete an item from the list.")
        print("Type Display to see the list you are making.")
        print("Type Done to finish the program.")
        print("If prompted what item you want to replace,")
        print("use the Display function to see what spot")
        print("the item is in.")
        print("Ex. With the List [Apple, Pear, Tissues],")
        print("The number would be [1, 2, 3] corresponding")
        print("to the respective Items location")
        job = str(input("What is the next mission Master? "))
    elif job == "Add" or job == "add":
        word = str(input("What do you wish to add? "))
        shopper.append(word)
        job = str(input("What is the next mission Master? "))
    elif job == "Insert" or job == "insert":
        word = str(input("What do you wish to add? "))
        location = int(input("Now where do you want the Item added? "))
        shopper.insert(location - 1, word)
        job = str(input("What is the next mission Master? "))
    elif job == "Replace" or job == "replace":
        word = str(input("What do you wish to add? "))
        location = int(input("Now which item do you wish to change? (Insert the Number)"))
        shopper[location-1] = word
        job = str(input("What is the next mission Master? "))
    elif job == "Delete" or job == "delete":
        location = int(input("Which item do you wish to delete? (Insert the Number)"))
        del shopper[location-1]
        job = str(input("What is the next mission Master? "))
    elif job == "Display" or job == "display":
        print(shopper)
        job = str(input("What is the next mission Master? "))
    elif job == "Done" or job == "done":
        pineapples = False
print(shopper)
print("Exited Loop")
