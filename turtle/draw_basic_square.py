import turtle
turtle.showturtle()
turtle.setup(800,800,0,0)
def draw_basic_square(x,y,n,color1,color2):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color1)
    turtle.begin_fill()
    for i in range(4):
            turtle.forward(n)
            turtle.left(90)
    turtle.end_fill()

    turtle.forward(n)
    turtle.penup()
    turtle.goto(x+n,y)
    turtle.pendown()
    turtle.color(color2)
    turtle.begin_fill()
    for i in range(4):
            turtle.forward(n)
            turtle.left(90)
    turtle.end_fill()
  
