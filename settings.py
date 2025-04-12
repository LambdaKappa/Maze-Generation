import numpy as np

class Data():
    def __init__(self):
        self.path_start = None
        self.path_end = None

data = Data()

RES = (WIDTH, HEIGHT) = 800, 800
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND = BLACK

# MAP = np.array([['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
#                 ['0', '0', '0', 'E', '0', '0', '0', '0', '0', '0'],
#                 ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
#                 ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
#                 ['0', '0', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '0'],
#                 ['0', '0', 'X', '0', '0', '0', '0', '0', 'X', '0'],
#                 ['0', '0', 'X', '0', '0', '0', 'S', '0', '0', '0'],
#                 ['0', '0', '0', 'X', '0', '0', '0', '0', '0', '0'],
#                 ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
#                 ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']], dtype=str)
MAP_SIZE = (MAP_SIZE_Y, MAP_SIZE_X) = (800, 800)

FREE_CELL = 0
WALL = 1
START_CELL = 2
END_CELL = 3
