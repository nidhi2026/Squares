import turtle
t = turtle.Turtle()
t.pensize(3)
t.shape('turtle')
t.color('black')
t.speed(5)
r = 50

for j in range(60):
    for i in range(4):
        t.forward(r)
        t.left(90)
    t.left(45)
    r = r*(2**0.5)

turtle.done()