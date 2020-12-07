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

def read_input_with_delimiter(filename, delim):
    input_data = ''
    with open(filename, 'r') as input_file:
        input_data = input_file.read()

    return input_data.split(delim)
