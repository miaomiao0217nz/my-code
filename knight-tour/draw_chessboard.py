import turtle
turtle.showturtle
from draw_single_square import *

screen_size=800
grid_count=8

turtle.setup(screen_size,screen_size,0,0)

x_start=-screen_size/2
y_start=-screen_size/2
l=screen_size/grid_count

def draw_chessboard():
    for j in range (grid_count):
        for i in range(grid_count):
            if (i+j)%2 ==0:
                draw_single_square(x_start+i*l,y_start+j*l,l,"sky blue")            
            if (i+j)%2 !=0:
                draw_single_square(x_start+i*l,y_start+j*l,l,"ivory") 
draw_chessboard()




turtle.done()