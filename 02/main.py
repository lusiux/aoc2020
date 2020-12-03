import sys
sys.path.append('./')

import fileinput
import Helper

def count_character(character, string):
    count = 0
    for char in string:
        if character == char:
            count += 1
    return count

def is_char_count_between_min_and_max(count, min, max):
    if count < min:
        return False
    if count > max:
        return False
    return True

def answer_one(lines):
    valids = 0
    for line in lines:
        data = Helper.parse_line(line, r'(\d+)-(\d+) (\w): (\w+)')
        if is_char_count_between_min_and_max(count_character(data[2], data[3]), int(data[0]), int(data[1])):
            valids += 1

    print(f'Answer one: {valids}')

def count_characters_at_positions(char, line, positions):
    count = 0
    for pos in positions:
        if line[pos-1] == char:
            count += 1
    
    return count

def answer_two(lines):
    valids = 0
    for line in lines:
        data = Helper.parse_line(line, r'(\d+)-(\d+) (\w): (\w+)')
        if count_characters_at_positions(data[2], data[3], [int(data[0]), int(data[1])]) == 1:
            valids += 1

    print(f'Answer two: {valids}')


if __name__ == "__main__":
    lines = Helper.read_input('02/input')

    answer_one(lines)
    answer_two(lines)