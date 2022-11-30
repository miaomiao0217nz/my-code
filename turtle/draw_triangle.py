import turtle
import math 
turtle.showturtle()

def draw_triangle(x,y,l,color):
    turtle.color(color)
    rad=math.radians(60)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+l*math.cos(rad),y+l*math.sin(rad))
    turtle.setheading(-60)
    turtle.goto(x+l,y)
    turtle.goto(x,y)
draw_triangle(40,50,100,"green")
turtle.done()