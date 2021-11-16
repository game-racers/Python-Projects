address = dict()
Address = dict()
lastList = []
cont = str(input('Would you like to add a new Entry to the AddressBook? '))
while cont == 'yes' or cont == 'Yes' or cont == 'y':
    nName = str(input('What is the nickname? '))
    name = str(input('What is their full name? '))
    FirstName = name[0: name.index(" ")]
    LastName = name[name.index(" ") + 1: ]
    lastList.append([LastName, nName])
    number = str(input('Input their Phone Number: '))
    home = str(input('What is their Address? '))
    email = str(input('What is their email? '))

    address[nName] = [[FirstName, LastName], number, home, email]
    Address[nName] = [[LastName, FirstName], number, home, email]

    cont = str(input('Would you like to add a new Entry to the AddressBook? '))
    
#this is the save area
myFile = open('addressBook.txt', 'w')
lastList.sort()
for i in range(len(lastList)):
    myFile.write(str(Address[lastList[i][1]]))
    myFile.write('\n')
myFile.close()

over = str(input('Do you want to look up anyone? '))
while over == 'yes' or over == 'Yes' or over == 'y':
    who = str(input('Who do you wish to look up? '))
    what = str(input('What do you want to see? (Name, Number, Address, or Email) '))
    if what == 'Name' or what == 'name':
        print(address[who][0])
    elif what == 'Number' or what == 'number':
        print(address[who][1])
    elif what == 'Address' or what == 'address':
        print(address[who][2])
    elif what == 'Email' or what == 'email':
        print(address[who][3])
    else:
        print('Error: Please input coorect input')
    over = str(input('Do you want to look up anyone? '))
    
