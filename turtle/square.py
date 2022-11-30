import turtle
import math
turtle.setup(800,800,0,0)
t=turtle.Turtle()
turtle.showturtle()
def draw_left_sections():
    screen_height = turtle.window_height()
    section_height = screen_height / 2
    screen_width = turtle.window_width()
    section_width = -screen_width / 2
    section=(section_width, section_height)
    turtle.penup()

    
    
    t.end_fill()
    turtle.pendown()
    turtle.goto(0,0)
    turtle.goto(0,section[1])
    turtle.goto(section[0],section[1])
    turtle.goto(section[0],0)
    turtle.goto(0,0)



   
def fill_the_square():
    screen_height = turtle.window_height()
    section_height = screen_height / 2
    screen_width = turtle.window_width()
    section_width = screen_width / 2
    section_list=[]
  
    t.color("pink")
    t.begin_fill()
    t.goto(0,0)
    for b in range(20):
        section_width=section_width-20
        for i in range(4):
            t.forward(section_width+20)
            t.left(90)
    t.end_fill()

    t.color("light blue")
    t.begin_fill()
    t.goto(0,0)
    t.setheading(90)
    for v in range(20):
        section_width=section_width-20
        for i in range(4):
            t.forward(section_width)
            t.left(90)
    t.end_fill()

    t.color("light green")
    t.begin_fill()
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.setheading(0)
   

    for c in range(20):
        section_width=section_width-20
        for l in range(4):
            t.forward(section_width)
            t.left(90)
    t.end_fill()
    
def drawcircle(pen,x,y,r):
    pen.penup()
    pen.goto(x+r,y)
    t.color("light blue")
    t.begin_fill()
    t.setheading(-90)
    pen.pendown()
    d=r
    for r in range(400):
            r=r+20
    for c in range(20):
        pen.right(360/d)
        pen.forward(2*r*math.pi/360)
        
    t.end_fill

fill_the_square()


            
    
   

turtle.done()