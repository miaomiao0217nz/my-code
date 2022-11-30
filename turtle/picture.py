import turtle
turtle.showturtle()
turtle.setup(800,800,0,0)
t=turtle.Turtle()
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
        
        turtle.penup()
    
        turtle.goto(-500, section[0])
        
        turtle.pendown()
        turtle.goto(500, section[0])
        turtle.penup()

def draw_vertical_lines(lines):
    line_list = get_horizontal_sections(lines+1)
    for line in line_list:
    
        turtle.penup()
        turtle.goto(line[0], -500)
        turtle.pendown()
        turtle.goto(line[0], 500)
        turtle.penup()



def draw_grid(sections):
    draw_horizontal_lines(sections ) 
    draw_vertical_lines(sections)

def draw_color_grid():
    draw_grid(7)
    fill_the_square()


draw_color_grid()
l=100
turtle.goto(-3.5*l,-3.5*l)

turtle.done()



