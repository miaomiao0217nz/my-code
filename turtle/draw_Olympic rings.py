# draw the Olympic Rings
import turtle
import math
turtle.showturtle()
def drawCircle(pen,x,y,r,color):
    pen.penup()
    pen.goto(x,y+r)
    pen.color(color)
    pen.setheading(0)
    pen.pendown()
    d=r
    for a in range(d):
        pen.right(360/d)
        pen.forward(2*r*math.pi/d)

def olympic(turtle,r):
    turtle.width(r/12)
    drawCircle(turtle,-2*r-r/5,0,r,"blue")
    drawCircle(turtle,0,0,r,"black")
    drawCircle(turtle,2*r+r/5,0,r,"red")
    drawCircle(turtle,-r-r/10,-r,r,"orange")
    drawCircle(turtle,r+r/10,-r,r,"green")


olympic(turtle, 100)
turtle.done()


















turtle.done()

