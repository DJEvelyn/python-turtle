from turtle import *

def draw_word(turtle : Turtle, word : str):
    # Define 'bottom' of word
    # Draw from bottom up

    position = turtle.position
    xPos = int(position[0])
    yPos = int(position[1])

    word_spacing = 100

    for char in word:
        #draw
        turtle.setposition(x = xPos, y = yPos)


def draw_I(turtle : Turtle, size : int):
    pass



