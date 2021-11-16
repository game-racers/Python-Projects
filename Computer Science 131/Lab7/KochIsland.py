import turtle

turtle.setup(1200,1000)

window = turtle.Screen()
window.title("Koch Island Program")
window.bgcolor("white")

t1 = turtle.Turtle()

colour = str(input('Which color? '))
t1.pencolor(colour)
shape = str(input('Which shape? (ex- Circle, Turtle, Arrow, Square, Triangle) '))
t1.shape(shape)
num = int(input('How many iterations? '))
t1.speed('fastest')

axiom = 'F-F-F-F'
i = 0
j = 0 #Iteration count
for j in range(num):
    while i < len(axiom):
        if axiom[i] == 'F':
            axiom = axiom[0:i] + 'F+FF-FF-F-F+F+F' + axiom[i+1:]
            i += 14
        i += 1
    i = 0

#print(axiom)
for i in range(len(axiom)):
    if axiom[i] == 'F':
        t1.forward(1)
    elif axiom[i] == '-':
        t1.left(90)
    else:
        t1.right(90)
t1.ht()


