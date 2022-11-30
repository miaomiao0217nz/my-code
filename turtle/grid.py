import turtle
from g import *
turtle.showturtle()



def draw_line_of_circles(x, y, count):
    section_list = get_horizontal_sections(count)
    radius = section_list[0][1] / 2
    for section in section_list:
        turtle.penup()
        turtle.goto(section[0], y)
        turtle.pendown()
        turtle.circle(radius)
        turtle.penup()

def draw_horizontal_line_of_arcs(x, y, count):
    section_list = get_horizontal_sections(count)
    radius = section_list[0][1] / 2
    for section in section_list:
        # turtle.penup()
        turtle.goto(section[0], y)
        turtle.pendown()
        turtle.circle(radius, 90)

def draw_horizontal_line_of_arcs(x, y, count):
    section_list = get_horizontal_sections(count)
    radius = section_list[0][1] / 2
    for section in section_list:
        # turtle.penup()
        turtle.goto(section[0], y)
        turtle.pendown()
        turtle.circle(radius, 90)
        # turtle.penup()

def draw_vertical_line_of_arcs(x, y, count):
    section_list = get_vertical_sections(count)
    radius = section_list[0][1] / 2
    for section in section_list:
        # turtle.penup()
        turtle.goto(x, section[0])
        turtle.pendown()
        turtle.circle(radius, 90)
        # turtle.penup()

def draw_arched_grid_without_lifting_pen(sections):
    section_list = get_vertical_sections(sections+1)
    for section in section_list:
        draw_horizontal_line_of_arcs(-500, section[0], sections+1)
    section_list = get_horizontal_sections(sections+1)
    for section in section_list:
        draw_vertical_line_of_arcs(section[0], -500, sections+1)




turtle.done()

