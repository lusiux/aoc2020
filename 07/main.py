import sys
sys.path.append('./')
import Helper
import re
    
test_input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

test_input_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

def find_bag_in_rules(rules, bag):
    # print(f'find {bag}')
    matches = []
    for key in rules.keys():
        if bag in rules[key]:
            matches.append(key)
    # print(f'found {matches}')
    return matches

def count_contained_bags(rules, bag):
    count = 0
    for match in rules[bag]:
        if match[0] != '':
            local_count = count_contained_bags(rules, match[1])
            if local_count > 0:
                count += (int(match[0]) * local_count)
            count += int(match[0])

    # print(f'{bag} contains {count} bags')
    return count

def answer_two(lines):
    rules = {}
    for line in lines:
        match = re.findall(r'(?:(\d+) )?(\w+ \w+) bags?', line)
        rules[match[0][1]] = match[1:]

    # print(rules)

    return count_contained_bags(rules, 'shiny gold')

def answer_one(lines):
    rules = {}
    for line in lines:
        match = re.findall(r'(?:(?:\d+) )?(\w+ \w+) bags?', line)
        rules[match[0]] = match[1:]

    done = []
    todo = [ 'shiny gold' ]
    matches = {}
    while len(todo) > 0:
        temp = []
        for bag in todo:
            if bag not in done:
                match = find_bag_in_rules(rules, bag)
                temp += match

                for ma in match:
                    matches[ma] = 1

                done.append(bag)
        if len(temp) > 0:
            todo = temp
        else:
            todo = []

    # print(f'total matches: {matches.keys()}')
    return len(matches.keys())


if __name__ == "__main__":
    lines = Helper.read_input_with_delimiter('07/input', "\n")

    print('Answer one: {}'.format(answer_one(lines)))
    print('Answer two: {}'.format(answer_two(lines)))

