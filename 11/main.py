import sys
sys.path.append('./')
import Helper
import copy

input_for_testing = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

class Seatmap():
    def __init__(self, lines):
        self._read_input(lines)

    def _read_input(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])
        self.map = [['.' for i in range(self.height+2)] for j in range(self.width+2)]

        for index, line in enumerate(lines):
            self._parse_line(line, index)

    def _parse_line(self, line, index):
        for char_index, char in enumerate(line):
            self.map[char_index+1][index+1] = char

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_adjacent_seats(self, x, y):
        x += 1
        y += 1
        return [
            self.map[x][y-1], # north
            self.map[x+1][y-1], # north east
            self.map[x+1][y], # east
            self.map[x+1][y+1], # south east
            self.map[x][y+1], # south
            self.map[x-1][y+1], # south west
            self.map[x-1][y], # west
            self.map[x-1][y-1], # north west
        ]

    def look_around_seat_at(self, x, y):
        x += 1
        y += 1
        return [
            self.get_next_seat_in_direction(x, y, 0, -1), # north
            self.get_next_seat_in_direction(x, y, 1, -1), # north east
            self.get_next_seat_in_direction(x, y, 1, 0), # east
            self.get_next_seat_in_direction(x, y, 1, 1), # south east
            self.get_next_seat_in_direction(x, y, 0, 1), # south
            self.get_next_seat_in_direction(x, y, -1, 1), # south west
            self.get_next_seat_in_direction(x, y, -1, 0), # west
            self.get_next_seat_in_direction(x, y, -1, -1), # north west
        ]
    
    def get_next_seat_in_direction(self, start_x, start_y, dx, dy):
        next_x = start_x+dx
        next_y = start_y+dy
        # print(f"next in dir: ({start_x}, {start_y}): d({dx}, {dy}) = n({next_x}, {next_y})")
        if (next_x < 0) or (next_x >= self.width+2) or (next_y < 0) or (next_y >= self.height+2):
            return None
        if self.map[next_x][next_y] == '.':
            next_seat = self.get_next_seat_in_direction(next_x, next_y, dx, dy)
            if next_seat == None:
                return '.'
            return next_seat
        return self.map[next_x][next_y]

    def get_seats_occupied_around_seat(self, x, y):
        occupied = 0
        seats = self.get_adjacent_seats(x, y)
        for seat in seats:
            if seat == '#':
                occupied += 1
        return occupied

    def get_seats_occupied_around_seat_looking(self, x, y):
        occupied = 0
        seats = self.look_around_seat_at(x, y)
        # print(f"({x},{y}: {seats}")
        for seat in seats:
            if seat == '#':
                occupied += 1
        return occupied
    
    def get_seat_at(self, x, y):
        return self.map[x+1][y+1]

    def get_seats_free_around_seat(self, x, y):
        occupied = 0
        seats = self.get_adjacent_seats(x, y)
        for seat in seats:
            if seat == 'L':
                occupied += 1
        return occupied

    def occupy_seat_at(self, x, y):
        self.map[x+1][y+1] = "#"
    def free_seat_at(self, x, y):
        self.map[x+1][y+1] = "L"
    def is_seat_free(self, x, y):
        return self.map[x+1][y+1] == 'L'
    def is_seat_occupied(self, x, y):
        return self.map[x+1][y+1] == '#'
    def print(self):
        for x in range(1, self.width):
            print(''.join(self.map[x]))
        print()
    def number_of_seats_occupied(self):
        occupied = 0
        for x in range(self.width+2):
            occupied += self.map[x].count('#')
        return occupied

def apply_rules(seats):
    new_seats = copy.deepcopy(seats)
    for x in range(seats.width):
        for y in range(seats.height):
            if seats.is_seat_free(x, y) and seats.get_seats_occupied_around_seat(x,y) == 0:
                new_seats.occupy_seat_at(x, y)
            elif seats.is_seat_occupied(x, y) and seats.get_seats_occupied_around_seat(x,y) >= 4:
                new_seats.free_seat_at(x, y)
    return new_seats

def apply_new_rules(seats):
    new_seats = copy.deepcopy(seats)
    for x in range(seats.width):
        for y in range(seats.height):
            occupied = seats.get_seats_occupied_around_seat_looking(x,y)
            if seats.is_seat_free(x, y) and occupied == 0:
                new_seats.occupy_seat_at(x, y)
            elif seats.is_seat_occupied(x, y) and occupied >= 5:
                new_seats.free_seat_at(x, y)
    return new_seats

def answer_one(lines):
    seats = Seatmap(lines)
    while True:
        new_seats = apply_rules(seats)
        if new_seats.map == seats.map:
            break
        seats = new_seats
        # seats.print()
    return seats.number_of_seats_occupied()

def answer_two(lines):
    seats = Seatmap(lines)
    while True:
        new_seats = apply_new_rules(seats)
        if new_seats.map == seats.map:
            break
        seats = new_seats
        # seats.print()
    return seats.number_of_seats_occupied()

if __name__ == "__main__":
    lines = Helper.read_input_with_delimiter('11/input', "\n")

    print('Answer one: {}'.format(answer_one(lines)))
    print('Answer two: {}'.format(answer_two(lines)))
