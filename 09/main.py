import sys
sys.path.append('./')
import Helper
import re
import copy

input_for_testing = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

def answer_one(lines):
    numbers = to_int(lines)

    preamble_length = 25

    for index in range(len(numbers)-(preamble_length)):
        if check_input(numbers[index:index+preamble_length], numbers[index+preamble_length]) == False:
            return numbers[index+preamble_length]

def check_input(preamble, number):
    # print(sorted(preamble), number)
    for num in sorted(preamble):
        diff = number - num
        # print(f'Looking for {diff}')
        if diff in preamble:
            return True
    return False

def find_range(numbers, number):
    # print(numbers, number)
    nums = []
    for num in numbers:
        nums.append(num)
        number -= num
        if number == 0:
            return nums
        elif number < 0:
            return None

def answer_two(lines):
    numbers = to_int(lines)

    ran = []
    while True:
        ran = find_range(numbers, 1721308972)
        if ran is not None:
            # print(ran)
            break
        numbers.pop(0)
    ran = sorted(ran)
    return ran[0] + ran[len(ran)-1]


def to_int(lines):
    return [ int(x) for x in lines ]


if __name__ == "__main__":
    lines = Helper.read_input_with_delimiter('09/input', "\n")

    print('Answer one: {}'.format(answer_one(lines)))
    print('Answer two: {}'.format(answer_two(lines)))

