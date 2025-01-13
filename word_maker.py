from grid_drawer import *

# Get list for letters

letter_file = open('wordFormat.txt', 'r')    

letter_dict = {}

def add_line_to_dict(line : str):

    letter = ""
    program_list = []
    
    line_list = str.split(line) # split by whitespace

    for element in enumerate(line_list):

        if element[0] == 0: # first position
            letter = element[1] # value at first position
        else:
            borders_removed = (element[1])[1:-1]
            pos_one = int(borders_removed[0])
            pos_two = int(borders_removed[-1])
            program_list.append((pos_one, pos_two))
    
    letter_dict[letter] = program_list

for line in letter_file:
    add_line_to_dict(line)


class DrawLetter(GridDrawer):

    def __init__(self, size : int, letter : str):
        super().__init__(size)
        self.letter_list = letter_dict[letter]

        for element in self.letter_list:
            self.add_to_program(element[0], element[1])


def draw_word(word : str, size : int, turtle : Turtle, word_spacing = 0.2):

    position = turtle.position()
    xPos, yPos = int(position[0]), int(position[1])

    for letter in word:

        turtle.penup()
        turtle.goto(xPos, yPos)
        turtle.pendown()

        letter_drawer = DrawLetter(size, letter)
        letter_drawer.set_start_position(xPos, yPos)
        letter_drawer.draw(turtle)

        xPos = xPos + size + (size * word_spacing)
        yPos = yPos
