__author__ = 'guinnc'
from Car import *

myFile = open('cars.txt', 'r')
tCar = 0
Cars = []
for line in myFile:
    tCar += 1
    dog = line.split()
    Cars.append(Car(dog[0], dog[1], dog[2], dog[3]))
print('The number of Cars is', tCar)
print()

for x in Cars:
    print(x)
print()

z = Cars[0]
for m in Cars:
    if z.mpg < m.mpg:
        z = m
print('The car with the best MPG is the', z)

y = Cars[0]
for o in Cars:
    if y.year > o.year:
        y = o
print('The oldest car is the', y)