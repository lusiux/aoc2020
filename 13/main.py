import sys
sys.path.append('./')
import Helper
import copy

input_for_testing = """939
7,13,x,x,59,x,31,19"""

class Bus:
    def __init__(self, id):
        self.id = id

    def offset_to_depart_time(self, time):
        # print(f"{self.id}: {self.id - (time % self.id)} after {time} at {(self.id - (time % self.id)) + time}")
        return self.id - (time % self.id)

    def __str__(self):
        return str(self.id)

def answer_one(lines):
    depart_time = int(lines[0])
    busses = []
    for num in lines[1].split(','):
        if num != 'x':
            busses.append(Bus(int(num)))

    busses.sort(key=lambda bus: bus.offset_to_depart_time(depart_time))
    bus = busses.pop(0)
    return bus.id * bus.offset_to_depart_time(depart_time)

def answer_two(lines):
    pass

def to_int(lines):
    return [ int(x) for x in lines ]

if __name__ == "__main__":
    lines = Helper.read_input_with_delimiter('13/input', "\n")

    print('Answer one: {}'.format(answer_one(lines)))
    print('Answer two: {}'.format(answer_two(lines)))
