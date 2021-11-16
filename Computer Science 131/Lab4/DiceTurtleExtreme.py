import random
import turtle

def main():
    t = turtle.Turtle()
    rolls = 0
    oX = 0
    oY = 0
    drawFilledRectangle(t, -50, -50, 100, 100, "black", "yellow")
    for rolls in range(5):
        val = random.randint(1,6)
        if rolls == 1:
            oX = -150
            oY = -150
            drawFilledRectangle(t, -50-oX, -50-oY, 100, 100, "black", "yellow")
        elif rolls == 1:
            oX = -150
            oY = -150
            drawFilledRectangle(t, -50-oX, -50-oY, 100, 100, "black", "yellow")
        elif rolls == 2:
            oX = 150
            oY = 150
            drawFilledRectangle(t, -50-oX, -50-oY, 100, 100, "black", "yellow")
        elif rolls == 3:
            oX = 150
            oY = -150
            drawFilledRectangle(t, -50-oX, -50-oY, 100, 100, "black", "yellow")
        elif rolls == 4:
            oX = -150
            oY = 150
            drawFilledRectangle(t, -50-oX, -50-oY, 100, 100, "black", "yellow")
            
        if val == 1:
            drawDot(t, 0-oX, 0-oY, 20, "red")
        elif val == 2:
            drawDot(t, -25-oX, -25-oY, 20, "Navy")
            drawDot(t,  25-oX, 25-oY, 20, "Navy")
        elif val == 3:
            drawDot(t, -25-oX, -25-oY, 20, "Navy")
            drawDot(t, 0-oX, 0-oY, 20, "Navy")
            drawDot(t, 25-oX, 25-oY, 20, "Navy")
        elif val == 4:
            drawDot(t, -25-oX, -25-oY, 20, "Navy")
            drawDot(t, -25-oX, 25-oY, 20, "Navy")
            drawDot(t, 25-oX, 25-oY, 20, "Navy")
            drawDot(t, 25-oX, -25-oY, 20, "Navy")
        elif val == 5:
            drawDot(t, -25-oX, -25-oY, 20, "Navy")
            drawDot(t, -25-oX, 25-oY, 20, "Navy")
            drawDot(t, 25-oX, 25-oY, 20, "Navy")
            drawDot(t, 25-oX, -25-oY, 20, "Navy")
            drawDot(t, 0-oX, 0-oY, 20, "Navy")
        elif val == 6:
            drawDot(t, -25-oX, 25-oY, 20, "green")
            drawDot(t, 25-oX, 25-oY, 20, "green")
            drawDot(t, 25-oX, 0-oY, 20, "green")
            drawDot(t, -25-oX, 0-oY, 20, "green")
            drawDot(t, -25-oX, -25-oY, 20, "green")
            drawDot(t, 25-oX, -25-oY, 20, "green")
    
    



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
    

main()    

