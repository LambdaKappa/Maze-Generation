import numpy as np
from collections import deque
from typing import List, Tuple
import random
from settings import START_CELL, END_CELL, WALL, FREE_CELL

class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.left = True
        self.right = True
        self.top = True
        self.bottom = True

    def get_position(self) -> Tuple[int, int]:
        return self.x, self.y

    def __repr__(self) -> str:
        return f"Cell({self.x}, {self.y})"


def get_cell_position_1d(x: int, y: int, columns: int) -> int:
    """Calculate the 1D index of a cell in a grid based on its 2D position."""
    return x + columns * y


def generate_maze(rows, columns):
    """Generate a perfect maze using depth-first search."""
    cells = [Cell(x, y) for y in range(rows) for x in range(columns)]

    directions = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0),
    }

    # Function to remove walls between two cells.
    def remove_wall(current, neighbor, direction):
        if direction == "up":
            current.top = False
            neighbor.bottom = False
        elif direction == "down":
            current.bottom = False
            neighbor.top = False
        elif direction == "left":
            current.left = False
            neighbor.right = False
        elif direction == "right":
            current.right = False
            neighbor.left = False

    stack = []
    visited = set()
    start_cell = cells[0]
    stack.append(start_cell)
    visited.add(start_cell.get_position())

    while stack:
        current_cell = stack.pop()

        neighbors = []
        for direction, (dx, dy) in directions.items():
            nx, ny = current_cell.x + dx, current_cell.y + dy
            if 0 <= nx < columns and 0 <= ny < rows:
                neighbor = cells[get_cell_position_1d(nx, ny, columns)]
                if neighbor.get_position() not in visited:
                    neighbors.append((neighbor, direction))

        if neighbors:
            stack.append(current_cell)

            neighbor, direction = random.choice(neighbors)

            remove_wall(current_cell, neighbor, direction)

            visited.add(neighbor.get_position())
            stack.append(neighbor)


    maze = _maze_to_numpy_array(cells, rows, columns)
    maze[1, 1] = START_CELL
    maze[-1 - 1, -1 -1] = END_CELL

    return maze


def _maze_to_numpy_array(cells, rows, columns):
    maze_array = np.ones((rows * 3, columns * 3), dtype=int)

    for n, cell in enumerate(cells):
        x, y = n % columns, n // columns

        X, Y = x * 3, y * 3

        maze_array[Y + 1, X + 1] = 0

        # Remove walls based on the cell's attributes
        if not cell.top:
            maze_array[Y, X + 1] = 0
            maze_array[Y - 1, X + 1] = 0

        if not cell.bottom:
            maze_array[Y + 2, X + 1] = 0
            maze_array[Y + 3, X + 1] = 0
        if not cell.left:
            maze_array[Y + 1, X] = 0
            maze_array[Y + 1, X - 1] = 0

        if not cell.right:
            maze_array[Y + 1, X + 2] = 0
            maze_array[Y + 1, X + 3] = 0

    return maze_array
