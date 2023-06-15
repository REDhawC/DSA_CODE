import turtle 
turtle.speed(10)
t=turtle.Turtle()
t.pencolor('purple')
def drawSquare(points,color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['lefttop'])
    t.pendown()
    t.begin_fill()
    t.goto(points['righttop'])
    t.goto(points['rightbottom'])
    t.goto(points['leftbottom'])
    t.end_fill()

def get_1third(p1,p2):
    if p1[1]>p2[1]:
        return (p1[0]+(abs(p1[0]-p2[0]))/3,p1[1]-(abs(p1[1]-p2[1]))/3)
    elif p1[1]<=p2[1]:
        return (p1[0]+(abs(p1[0]-p2[0]))/3,p1[1]+(abs(p1[1]-p2[1]))/3)



def get_2third(p1,p2):
    if p1[1]>p2[1]:
        return (p1[0]+(abs(p1[0]-p2[0]))/3*2,p1[1]-(abs(p1[1]-p2[1]))/3*2)
    elif p1[1]<=p2[1]:
        return (p1[0]+(abs(p1[0]-p2[0]))/3*2,p1[1]+(abs(p1[1]-p2[1]))/3*2)

def get_triRT(p1,p2):
    if p1[1]>p2[1]:
        return (p1[0]+(abs(p1[0]-p2[0]))/3*2,p1[1]-(abs(p1[1]-p2[1]))/3)
    elif p1[1]<=p2[1]:
        return (p1[0]+(abs(p1[0]-p2[0]))/3*2,p1[1]+(abs(p1[1]-p2[1]))/3)

def get_triLB(p1,p2):
    if p1[1]>p2[1]:
        return (p1[0]+(abs(p1[0]-p2[0]))/3,p1[1]-(abs(p1[1]-p2[1]))/3*2)
    elif p1[1]<=p2[1]:
        return (p1[0]+(abs(p1[0]-p2[0]))/3,p1[1]+(abs(p1[1]-p2[1]))/3*2)
    


points={'leftbottom':(-250,-250),
'lefttop':(-250,250),
'righttop':(250,250),
'rightbottom':(250,-250)
}

def sierpinski(degree,points):
    colormap=['purple','white','purple','white','purple','white','purple','white','purple','white','purple','white']

    drawSquare(points,colormap[degree])

    drawSquare({'lefttop':get_1third(points['lefttop'],points['rightbottom']),
            'righttop':get_triRT(points['lefttop'],points['rightbottom']),
            'rightbottom':get_2third(points['lefttop'],points['rightbottom']),
            'leftbottom':get_triLB(points['lefttop'],points['rightbottom'])
                },colormap[degree-1])
    if degree%2==1:
            drawSquare({'lefttop':get_1third(points['lefttop'],points['rightbottom']),
            'righttop':get_triRT(points['lefttop'],points['rightbottom']),
            'rightbottom':get_2third(points['lefttop'],points['rightbottom']),
            'leftbottom':get_triLB(points['lefttop'],points['rightbottom'])
                },colormap[degree])
    if degree>0:
        sierpinski(degree-1,
                    {'lefttop':points['lefttop'],
                    'righttop':get_1third(points['lefttop'],points['righttop']),
                    'rightbottom':get_1third(points['lefttop'],points['rightbottom']),
                    'leftbottom':get_1third(points['lefttop'],points['leftbottom'])
                    })
        sierpinski(degree-1,
                    {'lefttop':get_1third(points['lefttop'],points['righttop']),
                    'righttop':get_2third(points['lefttop'],points['righttop']),
                    'rightbottom':get_triRT(points['lefttop'],points['rightbottom']),
                    'leftbottom':get_1third(points['lefttop'],points['rightbottom'])
                    })
        sierpinski(degree-1,
                    {'lefttop':get_2third(points['lefttop'],points['righttop']),
                    'righttop':points['righttop'],
                    'rightbottom':get_1third(points['righttop'],points['rightbottom']),
                    'leftbottom':get_triRT(points['lefttop'],points['rightbottom'])
                    })
        sierpinski(degree-1,
                    {'lefttop':get_1third(points['lefttop'],points['leftbottom']),
                    'righttop':get_1third(points['lefttop'],points['rightbottom']),
                    'rightbottom':get_triLB(points['lefttop'],points['rightbottom']),
                    'leftbottom':get_2third(points['lefttop'],points['leftbottom'])
                    })
        sierpinski(degree-1,
                    {'lefttop':get_triRT(points['lefttop'],points['rightbottom']),
                    'righttop':get_1third(points['righttop'],points['rightbottom']),
                    'rightbottom':get_2third(points['righttop'],points['rightbottom']),
                    'leftbottom':get_2third(points['lefttop'],points['rightbottom'])
                    })
        sierpinski(degree-1,
                    {'lefttop':get_2third(points['lefttop'],points['leftbottom']),
                    'righttop':get_triLB(points['lefttop'],points['rightbottom']),
                    'rightbottom':get_1third(points['leftbottom'],points['rightbottom']),
                    'leftbottom':points['leftbottom']
                    })
        sierpinski(degree-1,
                    {'lefttop':get_triLB(points['lefttop'],points['rightbottom']),
                    'righttop':get_2third(points['lefttop'],points['rightbottom']),
                    'rightbottom':get_2third(points['leftbottom'],points['rightbottom']),
                    'leftbottom':get_1third(points['leftbottom'],points['rightbottom']),
                    })
        sierpinski(degree-1,
                    {'lefttop':get_2third(points['lefttop'],points['rightbottom']),
                    'righttop':get_2third(points['righttop'],points['rightbottom']),
                    'rightbottom':points['rightbottom'],
                    'leftbottom':get_2third(points['leftbottom'],points['rightbottom'])
                    })
    # drawSquare({'lefttop':get_1third(points['lefttop'],points['rightbottom']),
    #     'righttop':get_triRT(points['lefttop'],points['rightbottom']),
    #     'rightbottom':get_2third(points['lefttop'],points['rightbottom']),
    #     'leftbottom':get_triLB(points['lefttop'],points['rightbottom'])
    #         },colormap[degree])


# drawSquare(points,'blue')
sierpinski(3,points)