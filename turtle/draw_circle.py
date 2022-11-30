import turtle
import math
turtle.showturtle()
def drawcircle(pen,x,y,r,color):
    pen.penup()
    pen.goto(x+r,y)
    pen.color(color)
    pen.setheading(-90)
    pen.pendown()
    d=r
    for a in range(d):
        pen.right(360/d)
        pen.forward(2*r*math.pi/360)

drawcircle(turtle,0,0,200,"orange")
turtle.done()
