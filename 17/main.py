import sys
sys.path.append('./')
import Helper
import copy
from pprint import pprint

input_for_testing = """.#.
..#
###"""

class Point:
    def __init__(self, coords):
        self.coords = coords

    def __str__(self):
        return f"({','.join(str(x) for x in self.coords)})"

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        for index in range(len(self.coords)):
            if self.coords[index] != other.coords[index]:
                return False
        return True

class World:
    def __init__(self, dimensions):
        self.map = {}
        self.dimensions = dimensions

    def make_active_at(self, coords):
        self.map[coords] = str(coords)

    def make_inactive_at(self, coords):
        del self.map[coords]

    def neighbors_in_dimemsions(self, neighbors, dimension):
        if self.dimensions == dimension:
            return

        local_neighbors = []
        for diff in range(-1, 2):
            for coords in neighbors.keys():
                coord_list = coords.coords.copy()
                coord_list[dimension] += diff
                local_neighbors.append(Point(coord_list))

        for neighbor in local_neighbors:
            neighbors[neighbor] = str(neighbor)

        self.neighbors_in_dimemsions(neighbors, dimension+1)

    def get_neighbors_of(self, coords):
        neighbors = {
            coords: str(coords)
        }

        self.neighbors_in_dimemsions(neighbors, 0)
        del neighbors[coords]
        # pprint(neighbors)
        return neighbors

    def number_of_active_neighbors(self, coords):
        neighbors = self.get_neighbors_of( coords )

        actives = 0
        for neighbor in neighbors.keys():
            if self.is_active_at(neighbor):
                actives += 1

        return actives

    def is_active_at(self, coords):
        if coords in self.map:
            return True
        return False

    def is_inactive_at(self, coords):
        if coords in self.map:
            return False
        return True
    
    def number_of_active_cells(self):
        return len(self.map.keys())

def do(world):
    points_to_check = {}
    for coords in world.map.keys():
        points_to_check[coords] = world.map[coords]
        neighbors = world.get_neighbors_of(coords)
        for neighbor in neighbors:
            points_to_check[neighbor] = str(neighbor)

    activate = []
    deactivate = []
    for point in points_to_check:
        actives = world.number_of_active_neighbors(point)
        if world.is_active_at(point):
            if actives == 2 or actives == 3:
                pass
            else:
                deactivate.append(point)
        elif actives == 3:
            activate.append(point)

    for point in activate:
        world.make_active_at(point)
    for point in deactivate:
        world.make_inactive_at(point)

def answer_one(lines):
    world = World(3)

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                world.make_active_at( Point( [ x, y, 0] ) )

    for _ in range(6):
        # pprint(world.map)
        do(world)
    # pprint(world.map)
    return world.number_of_active_cells()

def answer_two(lines):
    world = World(4)

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                world.make_active_at( Point( [ x, y, 0, 0] ) )

    for _ in range(6):
        # pprint(world.map)
        do(world)
    # pprint(world.map)
    return world.number_of_active_cells()

if __name__ == "__main__":
    lines = Helper.read_input_with_delimiter('17/input', "\n")

    print('Answer one: {}'.format(answer_one(lines)))
    print('Answer two: {}'.format(answer_two(lines)))