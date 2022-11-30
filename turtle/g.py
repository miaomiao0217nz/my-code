import turtle
def get_vertical_sections(sections):
    screen_height = turtle.window_height()
    section_height = screen_height / sections
    section_y = -screen_height / 2
    section_list = []
    for i in range(sections):
        section_list.append((section_y, section_height))
        section_y += section_height
    # print(section_list)
    return section_list

def get_horizontal_sections(sections):
    screen_width = turtle.window_width()
    section_width = screen_width / sections
    section_x = -screen_width / 2
    section_list = []
    for i in range(sections):
        section_list.append((section_x, section_width))
        section_x += section_width
    return section_list

def draw_horizontal_lines(sections):
    section_list = get_vertical_sections(sections+1)
    for section in section_list:
        # make sure the turtle doesn't draw a line when it's moving to the starting point
        turtle.penup()
        # go to the very edge of the screen
        turtle.goto(-500, section[0])
        # turtle.goto(-300, section[0])
        turtle.pendown()
        turtle.goto(500, section[0])
        turtle.penup()

def draw_vertical_lines(lines):
    line_list = get_horizontal_sections(lines+1)
    for line in line_list:
        # make sure the turtle doesn't draw a line when it's moving to the starting point
        turtle.penup()
        turtle.goto(line[0], -500)
        turtle.pendown()
        turtle.goto(line[0], 500)
        turtle.penup()

def draw_grid(sections):
    draw_horizontal_lines(sections)
    draw_vertical_lines(sections)


# def draw_line_of_circles(x: int, y: int, radius: int, count: int): # type hinting
# def draw_line_of_circles(x, y, count):
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