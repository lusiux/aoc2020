import fileinput

def answer_one():
    for num in numbers:
        diff = 2020 - num
        if diff in numbers:
            print(diff * num)
            return

def answer_two():
    for num in numbers:
        for num2 in numbers:
            diff = 2020 - num - num2
            if diff in numbers:
                print(diff * num * num2)
                return


numbers = []

if __name__ == "__main__":
    for line in fileinput.input():
        line.rstrip()
        numbers.append(int(line))

    answer_one()
    answer_two()
