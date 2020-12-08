import sys
sys.path.append('./')
import Helper
import re
import copy

input_for_testing = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

class Acc():
    value = 0

def execute_command(command, parameter):
    # print(f'execute {command} {parameter}')
    if command == "nop":
        pass
    elif command == "jmp":
        return int(parameter)
    elif command == "acc":
        Acc.value += int(parameter)
    return 1

def answer_one(lines):
    Acc.value = 0
    done = []
    index = 0
    while True:
        done.append(index)
        match = re.search(r'(acc|jmp|nop) ([-+]\d+)', lines[index])
        if match is not None:
            command = match.group(1)
            parameter = match.group(2)
            index += execute_command(command, parameter)
            if index in done:
                return Acc.value
            done.append(index)

def run_code(code):
    # print(code)
    Acc.value = 0
    done = []
    index = 0
    while True:
        done.append(index)
        index += execute_command(code[index][0], code[index][1])
        if index in done:
            return None
        elif index >= len(code):
            return Acc.value
        done.append(index)

def answer_two(lines):
    code = []
    for line in lines:
        match = re.search(r'(acc|jmp|nop) ([-+]\d+)', line)
        if match is not None:
            command = match.group(1)
            parameter = match.group(2)
            code.append([command, parameter])

    for index in range(len(code)):
        if code[index][0] != "acc":
            copy_of_code = copy.deepcopy(code)
            # print(f"flip index {index}")
            if copy_of_code[index][0] == "jmp":
                copy_of_code[index][0] = "nop"
            else:
                copy_of_code[index][0] = "jmp"
            retVal = run_code(copy_of_code)
            if retVal is not None:
                return retVal

if __name__ == "__main__":
    lines = Helper.read_input_with_delimiter('08/input', "\n")

    print('Answer one: {}'.format(answer_one(lines)))
    print('Answer two: {}'.format(answer_two(lines)))

