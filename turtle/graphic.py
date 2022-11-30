import turtle

turtle.showturtle()
def get_vertical_sections(sections):
    screen_height = turtle.window_height()
    section_height = screen_height / sections
    section_y = -screen_height/2
    section_list = []
    for i in range(sections):
        section_list.append((section_y, section_height))
        section_y += section_height
    print('sectionlist: ', section_list)
    return section_list


def draw_horizontal_lines(sections):
    section_list = get_vertical_sections(sections+1)
    for section in section_list:
        # make sure the turtle doesn't draw a line when it's moving to the starting point
        turtle.penup()
        # go to the very edge of the screen
        turtle.goto(-500, section[0])
        # turtle.goto(-500, -337.5）
        turtle.pendown()
        turtle.goto(500, section[0])
        #turtle.penup()

def draw_c(pensize,color,lines):
    pensize(9)
    turtle.color("green")
    draw_horizontal_lines(4)

draw_c
turtle.done()
