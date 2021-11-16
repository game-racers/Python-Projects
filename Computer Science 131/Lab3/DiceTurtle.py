import random
import turtle

def main():
    t = turtle.Turtle()
    drawFilledRectangle(t, -50, -50, 100, 100, "black", "yellow")

    #Write code in space below to roll dice and determine which side to draw 
    val = random.randint(1,6)
    if val == 1:
        drawDot(t, 0, 0, 20, "Navy")
    elif val == 2:
        drawDot(t, -25, -25, 20, "Navy")
        drawDot(t,  25, 25, 20, "Navy")
    elif val == 3:
        drawDot(t, -25, -25, 20, "Navy")
        drawDot(t, 0, 0, 20, "Navy")
        drawDot(t, 25, 25, 20, "Navy")
    elif val == 4:
        drawDot(t, -25, -25, 20, "Navy")
        drawDot(t, -25, 25, 20, "Navy")
        drawDot(t, 25, 25, 20, "Navy")
        drawDot(t, 25, -25, 20, "Navy")
    elif val == 5:
        drawDot(t, 25, 25, 20, "Navy")
        drawDot(t, 25, -25, 20, "Navy")
        drawDot(t, -25, -25, 20, "Navy")
        drawDot(t, -25, 25, 20, "Navy")
        drawDot(t, 0, 0, 20, "Navy")
    elif val == 6:
        drawDot(t, -25, 25, 20, "Navy")
        drawDot(t, 25, 25, 20, "Navy")
        drawDot(t, 25, 0, 20, "Navy")
        drawDot(t, -25, 0, 20, "Navy")
        drawDot(t, -25, -25, 20, "Navy")
        drawDot(t, 25, -25, 20, "Navy")


    #######################################



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

