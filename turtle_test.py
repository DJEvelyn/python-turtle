from grid_drawer import *
from word_maker import *

turtle = Turtle()
turtle.color('black')

'''
plus_drawer = GridDrawer(100)
plus_drawer.add_to_program(1, 7)
plus_drawer.add_to_program(3, 5)

plus_drawer.draw(turtle)
'''

'''
l_drawer = GridDrawer(50)
l_drawer.add_to_program(0, 3)
l_drawer.add_to_program(3, 7)
l_drawer.add_to_program(7, 8)


l_drawer.draw(turtle)
'''

'''
e_drawer = GridDrawer(100)
e_drawer.add_to_program(0, 1)
e_drawer.add_to_program(0, 2)
e_drawer.add_to_program(3, 5)
e_drawer.add_to_program(6, 8)

e_drawer.draw(turtle)
'''

#letter_drawer = DrawLetter(25, 'B')
#letter_drawer.draw(turtle)

draw_word("HELLO", 25, turtle)

input('Press Enter to close')
