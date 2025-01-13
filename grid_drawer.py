from turtle import *

# Takes a 3x3 grid and draws lines with Turtle along it

class GridDrawer:

    pos_dict = {
        0:[0, 0],
        1:[0.5, 0],
        2:[1, 0],
        3:[0, 0.5],
        4:[0.5, 0.5],
        5:[1, 0.5],
        6:[0, 1],
        7:[0.5, 1],
        8:[1, 1]
    }

    size = 0

    startX = 0
    startY = 0

    program_dict = {} # Connections. Index A -> Index B


    def __init__(self, size):
        self.size = size

    def set_start_position(self, x : int, y : int):
        self.startX, self.startY = x, y
    
    def set_program(self, p_dict : dict):
        self.program_dict = p_dict
    
    def add_to_program(self, startPos : int, endPos : int):
        """
        startPos and endPos represents index

        0 1 2
        3 4 5
        6 7 8
        """
        
        self.program_dict[startPos] = endPos

    def __get_position_for_point(self, i : int) -> tuple[int, int]:
        """
        i represents index

        0 1 2
        3 4 5
        6 7 8
        """
        
        self.modifier = GridDrawer.pos_dict[i]

        return [self.startX + self.size * self.modifier[0], self.startY + self.size * self.modifier[1]]


    def draw(self, turtle : Turtle):
        turtle.setpos(self.startX, self.startY)

        for route in self.program_dict.items():
            
            self.startPos = self.__get_position_for_point(route[0])
            self.endPos = self.__get_position_for_point(route[1])
            
            turtle.penup()
            turtle.setpos(self.startPos[0], -self.startPos[1])
            turtle.pendown()
            turtle.goto(self.endPos[0], -self.endPos[1])



    
