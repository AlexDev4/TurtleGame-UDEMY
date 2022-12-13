import turtle

t = turtle.Turtle()

def stairs(height, numberOfSteps):
    for i in range(0, numberOfSteps):
        t.forward(height)
        t.left(90)
        t.forward(height)
        t.right(90)
    t.forward(height)

stairs(30, 5)


turtle.done()