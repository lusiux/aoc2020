import sys
sys.path.append('./')
import Helper
import copy
import re

input_for_testing = """F10
N3
F7
R90
F11"""

class Ship():
    def __init__(self):
        self.direction = 0
        self.x = 0
        self.y = 0

    def go_north(self, steps):
        self.y += steps
    def go_south(self, steps):
        self.y -= steps
    def go_east(self, steps):
        self.x += steps
    def go_west(self, steps):
        self.x -= steps
    def rotate_left(self, degrees):
        self.direction -= degrees
        self.direction = ( self.direction + 360 ) % 360
    def rotate_right(self, degrees):
        self.direction += degrees
        self.direction = ( self.direction + 360 ) % 360
    def go_forward(self, steps):
        if self.direction == 0:
            self.go_east(steps)
        elif self.direction == 90:
            self.go_south(steps)
        elif self.direction == 180:
            self.go_west(steps)
        elif self.direction == 270:
            self.go_north(steps)
    def print(self):
        print(f"Ship at ({self.x}, {self.y}) facing {self.direction}")

class ShipWithWaypoint():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint_x = 10
        self.waypoint_y = 1

    def go_north(self, steps):
        self.waypoint_y += steps
    def go_south(self, steps):
        self.waypoint_y -= steps
    def go_east(self, steps):
        self.waypoint_x += steps
    def go_west(self, steps):
        self.waypoint_x -= steps
    def rotate_left(self, degrees):
        self.rotate_right(360 - degrees)

    def rotate_right(self, degrees):
        x = self.waypoint_x
        y = self.waypoint_y
        if degrees == 90:
            self.waypoint_x = y
            self.waypoint_y = -x
        elif degrees == 180:
            self.waypoint_x = -x
            self.waypoint_y = -y
        elif degrees == 270:
            self.waypoint_x = -y
            self.waypoint_y = x
    def go_forward(self, steps):
        self.x += (self.waypoint_x * steps)
        self.y += (self.waypoint_y * steps)
    def print(self):
        print(f"Ship at ({self.x}, {self.y}) with waypoint ({self.waypoint_x}, {self.waypoint_y})")


def parse_command(line, table):
    match = re.search(r'(N|S|E|W|L|R|F)(\d+)', line)
    if match:
        return table[match.group(1)], int(match.group(2))
    else:
        print(line)

def answer_one(lines):
    table = {
        'N': Ship.go_north,
        'S': Ship.go_south,
        'E': Ship.go_east,
        'W': Ship.go_west,
        'L': Ship.rotate_left,
        'R': Ship.rotate_right,
        'F': Ship.go_forward
    }

    ship = Ship()
    for line in lines:
        fn, param = parse_command(line, table)
        fn(ship, param)
        # ship.print()
    return abs(ship.x) + abs(ship.y)

def answer_two(lines):
    table = {
        'N': ShipWithWaypoint.go_north,
        'S': ShipWithWaypoint.go_south,
        'E': ShipWithWaypoint.go_east,
        'W': ShipWithWaypoint.go_west,
        'L': ShipWithWaypoint.rotate_left,
        'R': ShipWithWaypoint.rotate_right,
        'F': ShipWithWaypoint.go_forward
    }

    ship = ShipWithWaypoint()
    # ship.print()
    for line in lines:
        # print(line)
        fn, param = parse_command(line, table)
        fn(ship, param)
        # ship.print()
    return abs(ship.x) + abs(ship.y)

if __name__ == "__main__":
    lines = Helper.read_input_with_delimiter('12/input', "\n")

    print('Answer one: {}'.format(answer_one(lines)))
    print('Answer two: {}'.format(answer_two(lines)))
