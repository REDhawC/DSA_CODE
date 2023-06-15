import turtle
t=turtle.Turtle()
def Tree(len):
    if len>5:
        t.forward(len)
        t.right(20)
        Tree(len-15)
        t.left(40)
        Tree(len-15)
        t.right(20)
        t.backward(len)

t.left(90)
t.speed(1)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('yellow')
t.pensize(3)
Tree(75)
t.hideturtle()
turtle.done()