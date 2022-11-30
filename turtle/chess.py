import turtle
turtle.showturtle
from draw_basic_square import *
turtle.setup(800,800,0,0)
  
  
def draw_chessboard():
    draw_basic_square(-400,-400,100,"pink","light green")

    for i in range(4):


        x=x+200
        y=y+0
    draw_basic_square(x,y,100,"pink","light green")

draw_chessboard()

turtle.done()










turtle.done()