import sys
sys.path.append('./')
import Helper
import re

def answer_one(groups):
    total_chars_in_groups = 0

    for group in groups:
        chars = [0] * 256
        for char in group:
            chars[ord(char)] = 1

        total_chars_in_groups += sum(chars[97:123])
    
    return total_chars_in_groups
    
def answer_two(lines):
    total_chars_in_groups = 0

    for group in groups:
        persons_in_group = len(group.split("\n"))
        chars = [0] * 256

        for char in group:
            chars[ord(char)] += 1

        for count in chars[97:123]:
            if count == persons_in_group:
                total_chars_in_groups += 1

    return total_chars_in_groups

if __name__ == "__main__":
    groups = Helper.read_input_with_delimiter('06/input', "\n\n")

    print('Answer one: {}'.format(answer_one(groups)))
    print('Answer two: {}'.format(answer_two(groups)))