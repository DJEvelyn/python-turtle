from turtle import *

main_turtle = Turtle()
main_turtle.color('blue')

def __draw_shape(turtle : Turtle, side_length : int, sides : int):

    turtle.pendown()

    turn_angle = 360 / sides

    for _ in range(0, sides):
        turtle.forward(side_length)
        turtle.right(turn_angle)

    turtle.penup()

def __draw_star(turtle : Turtle, side_length : int):
    pass

    
def draw_shape(turtle : Turtle, side_length: int, shape_name : str):

    try:
        shape_name = str.lower(shape_name)
    except:
        print("String was not provided")

    shape_dict = {
        'triangle':3,
        'square':4,
        'pentagon':5,
        'hexagon':6,
        'octagon':8
    }

    print(f'Given shape name is {shape_name}')

    if shape_name == 'circle':
        turtle.circle(side_length / 2)
    if shape_name == 'star':
        __draw_star(turtle, side_length)
    elif shape_name in shape_dict:
        __draw_shape(turtle, side_length, shape_dict[shape_name])
    else:
        print("Shape is not in dictionary")

shape = input("Draw a shape: ")
size = input("Add a number for size: ")

try:
    draw_shape(main_turtle, int(size), shape)
except:
    print("Invalid inputs ")


pos = main_turtle.pos()
print(f'main_turtle position = ({int(pos[0])}, {int(pos[1])})')


done()


