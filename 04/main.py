import sys
sys.path.append('./')
import Helper
import re

def numeric_min_max(num, min, max):
    if num is not None and num.isnumeric() and int(num) >= min and int(num) <= max:
        return True
    return False

def byr_is_valid(byr):
    return numeric_min_max(byr, 1920, 2002)

def iyr_is_valid(iyr):
    return numeric_min_max(iyr, 2010, 2020)

def eyr_is_valid(iyr):
    return numeric_min_max(iyr, 2020, 2030)

def hgt_is_valid(hgt):
    match = re.search(r'^(\d+)(in|cm)$', hgt)
    if match is None:
        return False
    if match.group(2) == 'in':
        return numeric_min_max(match.group(1), 59, 76)
    elif match.group(2) == 'cm':
        return numeric_min_max(match.group(1), 150, 193)
    else:
        return False

def hcl_is_valid(hcl):
    match = re.search(r'^#([0-9]|[a-f]){6}$', hcl)
    if match is None:
        return False
    return True

def ecl_is_valid(ecl):
    if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False

def pid_is_valid(pid):
    match = re.search(r'^\d{9}$', pid)
    if match is None:
        return False
    return True

def always_valid(value):
    return True

class Passport:
    def __init__(self):
        self.fields = dict()
        self.allowed_fields = {
            'byr': byr_is_valid,
            'iyr': iyr_is_valid,
            'eyr': eyr_is_valid,
            'hgt': hgt_is_valid,
            'hcl': hcl_is_valid,
            'ecl': ecl_is_valid,
            'pid': pid_is_valid,
            'cid': always_valid
        }
    
    def set_field(self, key, value):
        if key in self.allowed_fields.keys():
            self.fields[key] = value

    def are_fields_valid(self):
        if self.is_valid() is False:
            return False

        for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if self.allowed_fields[key](self.fields[key]) is False:
                return False
        return True

    def is_valid(self):
        for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if field not in self.fields:
                return False
        return True

    @staticmethod
    def from_string(string):
        passport = Passport()
        fields = re.split(r'\s+', string)
        for field in fields:
            if field != "":
                key, value = field.split(":")
                passport.set_field(key, value)

        return passport

def answer_one(passports):
    valid_passports = 0
    for passport_string in passports:
        passport = Passport.from_string(passport_string)
        if passport.is_valid():
            valid_passports += 1
    
    return valid_passports
    

def answer_two(lines):
    valid_passports = 0
    for passport_string in passports:
        passport = Passport.from_string(passport_string)
        if passport.are_fields_valid():
            valid_passports += 1
    
    return valid_passports

if __name__ == "__main__":
    input_data = ""
    with open('04/input', 'r') as input_file:
        input_data = input_file.read()

    passports = input_data.split("\n\n")

    print('Answer one: {}'.format(answer_one(passports)))
    print('Answer two: {}'.format(answer_two(passports)))