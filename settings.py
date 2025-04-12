import numpy as np

class Data():
    def __init__(self):
        self.path_start = None
        self.path_end = None

data = Data()

# Change resolution to change the size of the maze
RES = (WIDTH, HEIGHT) = 800, 800
MAP_SIZE = (MAP_SIZE_Y, MAP_SIZE_X) = WIDTH, HEIGHT

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND = BLACK

FREE_CELL = 0
WALL = 1
START_CELL = 2
END_CELL = 3
