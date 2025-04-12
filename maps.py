import numpy as np
from settings import *

class PathElement:
    def __init__(self, y, x):
        self.g_cost = 0
        self.f_cost = 1000

        self.y, self.x = y, x

        self.parent = None
        self.traversable = True

    def __repr__(self):
        if not self.traversable: return "WALL"
        return f"{self.f_cost}"

def calculate_h_cost(element, target):
    return np.linalg.norm((element[0] - target[0], element[1] - target[1]))

def get_lowest_f_cost_idx(map, open_set):
    lowest_cost = -1
    lowest_idx = 0
    for i in range(len(open_set)):
        y, x = open_set[i]
        new_cost = map[y, x].f_cost
        if new_cost < lowest_cost:
            lowest_cost = new_cost
            lowest_idx = i
    return lowest_idx

def get_path_indices(target_square):
    result = []
    current = target_square.parent
    while current != None:
        result.append((current.y, current.x))
        current = current.parent

    return result[:-1]

def get_path(map, start, target):
    open_set = []
    closed_set = set()
    # Returns indices of all the map elements that are the part of the shortest path.
    path = []

    open_set.append(start)

    while True:
        if len(open_set) == 0:
            return list()

        current_idx = (c_y, c_x) = open_set[get_lowest_f_cost_idx(map, open_set)]
        if current_idx == target:
            current_element = map[target[0], target[1]]
            break
        open_set.remove(current_idx)
        closed_set.add(current_idx)

        current_element = map[c_y, c_x]

        for y in range(-1, 2):
            for x in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                n_x, n_y = c_x + x, c_y + y
                if n_x < 0 or n_x >= MAP_SIZE_X or n_y < 0 or n_y >= MAP_SIZE_Y:
                    continue

                neighbour = map[n_y, n_x]
                if not neighbour.traversable or (n_y, n_x) in closed_set:
                    continue
                d_path = 2 ** .5 if (x != 0 and y != 0) else 1

                g_cost = current_element.g_cost + d_path
                h_cost = calculate_h_cost((neighbour.y, neighbour.x), target)
                new_f_cost = g_cost + h_cost
                if new_f_cost < neighbour.f_cost or (n_y, n_x) not in open_set:
                    neighbour.parent = current_element
                    neighbour.g_cost = g_cost
                    neighbour.f_cost = new_f_cost

                    if (n_y, n_x) not in open_set:
                        open_set.append((neighbour.y, neighbour.x))

    return get_path_indices(current_element)

def create_map(array, data):
    map = np.ndarray(dtype=PathElement, shape=(array.shape))

    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            map[i, j] = PathElement(i, j)
            if array[i, j] == WALL:
                map[i, j].traversable = False
            elif array[i, j] == START_CELL:
                 data.path_start = (i, j)
            elif array[i, j] == END_CELL:
                data.path_end = (i, j)
    return map
