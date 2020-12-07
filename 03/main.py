import sys
sys.path.append('./')
import Helper

class Landscape:
    def __init__(self):
        self.landscape = []

    @staticmethod
    def extract_trees(line):
        return [
            True if char == '#' else False for char in line
        ]

    def append_landscape_line(self, line):
        self.landscape.append(Landscape.extract_trees(line))

    def is_tree_at(self, x, y):
        return self.landscape[y][x % len(self.landscape[0])]

    def number_of_trees_at(self, x, y):
        if self.is_tree_at(x, y):
            return 1
        return 0

    def slope_through(self, diff_x, diff_y):
        trees = 0

        for y in range(0, len(self.landscape), diff_y):
            x = int(y / diff_y * diff_x )
            trees += self.number_of_trees_at(x, y)

        return trees

def landscape_from_lines(lines):
    landscape = Landscape()

    for line in lines:
        landscape.append_landscape_line(line)

    return landscape

def answer_one(lines):
    landscape = landscape_from_lines(lines)
    return landscape.slope_through(3, 1)

def answer_two(lines):
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]

    landscape = landscape_from_lines(lines)

    trees = 1
    for slope in slopes:
        trees *= landscape.slope_through(slope[0], slope[1])

    return trees

if __name__ == "__main__":
    lines = Helper.read_input('03/input')

    print('Answer one: {}'.format(answer_one(lines)))
    print('Answer two: {}'.format(answer_two(lines)))