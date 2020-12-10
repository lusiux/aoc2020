import sys
sys.path.append('./')
import Helper

input_for_testing = """16
10
15
5
1
11
7
19
6
12
4"""

larger_input_for_testing = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

def answer_one(lines):
    jolts = to_int(lines)
    jolts.append(0)
    jolts.append(max(jolts)+3)
    jolts = sorted(jolts)

    diffs = [0,0,0,0]

    for index in range(len(jolts)-1):
        diff = jolts[index+1] - jolts[index]
        diffs[diff] += 1
    
    return diffs[1] * diffs[3]

def calculate_diffs(jolts):
    diffs = []
    for index in range(len(jolts)-1):
        diffs.append(jolts[index+1] - jolts[index])
    return diffs

doubles = []
def answer_two(lines):
    jolts = to_int(lines)
    jolts.append(0)
    jolts.append(max(jolts)+3)
    jolts = sorted(jolts)

    diffs = calculate_diffs(jolts)
    seq = 0
    product = 1
    while True:
        if len(diffs) == 0:
            break
        diff = diffs.pop(0)
        if diff == 1:
            seq += 1
        else:
            if seq == 4:
                product *= 7
            elif seq > 0:
                product *= pow(2, seq-1)
            seq = 0
    return product

def to_int(lines):
    return [ int(x) for x in lines ]

if __name__ == "__main__":
    lines = Helper.read_input_with_delimiter('10/input', "\n")

    print('Answer one: {}'.format(answer_one(lines)))
    print('Answer two: {}'.format(answer_two(lines)))

