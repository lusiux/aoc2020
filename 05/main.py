import sys
sys.path.append('./')
import Helper
import re

def binary_decoder(string, zero, one):
    value = 0
    string = string[::-1]
    for index in range(len(string)):
        if string[index] == one:
            value += pow(2,index)
    return value

class Boarding_Pass:
    def __init__(self, row, col):
        self.fields = {
            'row': row,
            'col': col
        }
        self.allowed_fields = [
            'row',
            'col'
        ]
    
    def set_field(self, key, value):
        if key in self.allowed_fields:
            self.fields[key] = value

    @staticmethod
    def from_string(string):
        fields = re.match(r'^([FB]{7})([LR]{3})$', string)
        if fields:
            return Boarding_Pass(binary_decoder(fields.group(1), 'F', 'B'), binary_decoder(fields.group(0), 'L', 'R'))
        return None

    def id(self):
        return self.fields['row'] * 8 + self.fields['col']

def answer_one(lines):
    passes = []
    for line in lines:
        boarding_pass = Boarding_Pass.from_string(line)
        passes.append(boarding_pass.id())
    
    return max(passes)
    

def answer_two(lines):
    passes = []
    for line in lines:
        boarding_pass = Boarding_Pass.from_string(line)
        passes.append(boarding_pass.id())
    print(passes)

    for row in range(1, 127):
        for col in range(0, 8):
            bp = Boarding_Pass(row, col)
            if bp.id()-1 in passes and bp.id()+1 in passes and bp.id() not in passes:
                return bp.id()


if __name__ == "__main__":
    lines = Helper.read_input('05/input')

    print('Answer one: {}'.format(answer_one(lines)))
    print('Answer two: {}'.format(answer_two(lines)))