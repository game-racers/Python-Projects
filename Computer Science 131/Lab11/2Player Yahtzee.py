import turtle
import random

class Dice(object):       
                
    def diceX(self):
        print(dVal)

    def roll(self, dVal, idx):
        print("roll started")
        if len(idx) != 0:
            for i in range(len(idx)):
                k = int(idx[i])
                print(k)
                val = random.randint(1,6)
                dVal[i] = val

    def drawDice(self, idx, coords, color, turtle, dVal):
        print('Draw Dice Started')
        for i in idx:
            if i == 1:
                drawFilledRectangle(turtle, coords[0], coords[5], 100, 100, "black", color)
                dotLoc(i, coords, turtle, dVal)
            elif i == 2:
                drawFilledRectangle(turtle, coords[1], coords[5], 100, 100, "black", color)
                dotLoc(i,coords, turtle, dVal)
            elif i == 3:
                drawFilledRectangle(turtle, coords[2], coords[5], 100, 100, "black", color)
                dotLoc(i,coords, turtle, dVal)
            elif i == 4:
                drawFilledRectangle(turtle, coords[3], coords[5], 100, 100, "black", color)
                dotLoc(i,coords, turtle, dVal)
            elif i == 5:
                drawFilledRectangle(turtle, coords[4], coords[5], 100, 100, "black", color)
                dotLoc(i,coords, turtle, dVal)

def dotLoc(i, coords, turtle, dVal):
    if dVal[i] == 1:
        i -= 1
        drawDot(turtle, +50+coords[i], +50+coords[5], 20, "Navy")
    elif dVal[i] == 2:
        i -= 1
        drawDot(turtle, +75+coords[i], +75+coords[5], 20, "Navy")
        drawDot(turtle, +25+coords[i], +25+coords[5], 20, "Navy")
    elif dVal[i] == 3:
        i -= 1
        drawDot(turtle, +50+coords[i], +50+coords[5], 20, "Navy")
        drawDot(turtle, +25+coords[i], +25+coords[5], 20, "Navy")
        drawDot(turtle, +75+coords[i], +75+coords[5], 20, "Navy")
    elif dVal[i] == 4:
        i -= 1
        drawDot(turtle, +25+coords[i], +25+coords[5], 20, "Navy")
        drawDot(turtle, +25+coords[i], +75+coords[5], 20, "Navy")
        drawDot(turtle, +75+coords[i], +25+coords[5], 20, "Navy")
        drawDot(turtle, +75+coords[i], +75+coords[5], 20, "Navy")
    elif dVal[i] == 5:
        i -= 1
        drawDot(turtle, +25+coords[i], +75+coords[5], 20, "Navy")
        drawDot(turtle, +25+coords[i], +25+coords[5], 20, "Navy")
        drawDot(turtle, +75+coords[i], +25+coords[5], 20, "Navy")
        drawDot(turtle, +75+coords[i], +75+coords[5], 20, "Navy")
        drawDot(turtle, +25+coords[i], +25+coords[5], 20, "Navy")
    elif dVal[i] == 6:
        i -= 1
        drawDot(turtle, +75+coords[i], +75+coords[5], 20, "Navy")
        drawDot(turtle, +75+coords[i], +25+coords[5], 20, "Navy")
        drawDot(turtle, +25+coords[i], +50+coords[5], 20, "Navy")
        drawDot(turtle, +75+coords[i], +50+coords[5], 20, "Navy")
        drawDot(turtle, +25+coords[i], +75+coords[5], 20, "Navy")
        drawDot(turtle, +25+coords[i], +25+coords[5], 20, "Navy")
            
def drawFilledRectangle(t, x, y, w, h, colorP="black", colorF="white"):
    t.pencolor(colorP)
    t.fillcolor(colorF)
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.goto(x+w, y)
    t.goto(x+w, y+h)
    t.goto(x, y+h)
    t.goto(x, y)
    t.end_fill()

def drawDot(t, x, y, diameter, colorP):
    t.up()
    t.goto(x, y)
    t.pencolor(colorP)
    t.dot(diameter)

##pn1 = str(input('What is Player 1\'s name: '))
##p1Color = str(input('What color: '))
##pn2 = str(input('What is Player 2\'s name: '))
##p2Color = str(input('What color: '))
pn1 = "Eric"
p1Color = 'Green'
pn2 = 'Paul'
p2Color = 'Red'
t1 = turtle.Turtle()
t1.speed = 0
t1.penup()
t1.goto( -350, 300)
t1.pendown()
t1.write(pn1, font = ("Arial", 18, "normal"))
t2 = turtle.Turtle()
t2.speed = 0
t2.speed = 0
t2.penup()
t2.goto( -350, -200)
t2.pendown()
t2.write(pn2, font = ("Arial", 18, "normal"))
idx = [1,2,3,4,5]
upper = [-275, -150, -25, 100, 225, 250]
lower = [-275, -150, -25, 100, 225, -250]
dVal1 = {}
for i in range(5):
    val = random.randint(1,6)
    dVal1[i+1] = val
print(dVal1)
dVal2 = {}
for i in range(5):
    val = random.randint(1,6)
    dVal2[i+1] = val
print(dVal2)
p1Dice = Dice()
p2Dice = Dice()

p1Dice.drawDice(idx, upper, p1Color, t1, dVal1)
p2Dice.drawDice(idx, lower, p2Color, t2, dVal2)
