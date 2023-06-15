import turtle
t=turtle.Turtle()

def RecursionP(t,length):
    if length>0:
        t.forward(length)
        t.right(90)
        RecursionP(t,length-5)
    else:
        pass
RecursionP(t,300)