from turtle import *

spider = Turtle()
spider.color('black')

# Draw lines outwards from center

def draw_to_center(turtle : Turtle, amount : int, size : int):
    rotation = 360 / amount

    for _ in range(0, amount):
        turtle.right(rotation)
        turtle.forward(size)
        turtle.back(size)

def draw_circles(turtle : Turtle, amount : int, size : int):

    size = size * 2

    position = turtle.pos()
    xPos = int(position[0])
    yPos = int(position[1])

    for i in range(0, amount):

        circle_size = (size / 2) * (1 - (i / amount))

        turtle.setpos(xPos, yPos - circle_size)

        turtle.circle(circle_size)


def draw_circles_broken(turtle : Turtle, amount : int, size : int):

    for i in range(0, amount):

        circle_size = (size / 2) * i / amount

        turtle.circle(circle_size)

        position = turtle.pos()
        xPos = int(position[0])
        yPos = int(position[1])

        turtle.setpos(xPos, yPos + circle_size)



draw_to_center(spider, 10, 150)
draw_circles(spider, 10, 150)

input('Press Enter to close')



# Draw smaller circles within lines