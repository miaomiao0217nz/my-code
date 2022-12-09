import turtle
turtle.showturtle()

def draw_single_square(x,y,l,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
            turtle.forward(l)
            turtle.left(90)
    turtle.end_fill()


#draw_single_square(0,0,100,"pink")
#turtle.done()