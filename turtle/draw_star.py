import turtle
import math
turtle.showturtle()
def draw_star(x,y,l,color):
    turtle.color(color)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(72)
    turtle.forward(l)
    turtle.setheading(-72)
    turtle.forward(l)
    turtle.setheading(0)
    turtle.forward(l)
    turtle.setheading(-144)
    turtle.forward(l)
    turtle.setheading(-72)
    turtle.forward(l)
    turtle.setheading(144)
    turtle.forward(l)
    turtle.setheading(-144)
    turtle.forward(l)
    turtle.setheading(72)
    turtle.forward(l)
    turtle.setheading(144)
    turtle.forward(l)
    turtle.setheading(0)
    turtle.forward(l)
draw_star(50,50,50,"blue")
turtle.done()


