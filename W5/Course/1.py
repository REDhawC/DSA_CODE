import turtle
t=turtle.Turtle()
t.speed(1)
def drawTriangle(points,color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['left'])
    t.pendown()
    t.begin_fill()
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()

points={'left':(-200,-100),
'top':(0,200),
'right':(200,-100)
}

drawTriangle(points,'red')