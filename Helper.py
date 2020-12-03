import re

def parse_line(line, regexp):
    match = re.search(regexp, line)
    return match.groups()

def read_input(filename):
    input_file = open(filename, 'r') 

    lines = []
    for line in input_file.readlines():
        line = line.rstrip()
        lines.append(line)

    return lines