import re # regex module

def range_subset(range1, range2):
    if not range1:
        return True # empty range is subset of anything
    if not range2:
        return False # non empty range cannot be subset of empty range"
    if len(range1) > 1 and range1.step % range2.step:
        return False # must have a single value or integer multiple step
    if len(range1) == 1:
        return range1.start in range2
    else:
        return range1.start in range2 or range1[-1] in range2

def range_overlap(range1, range2):
    return range_subset(range1, range2) or range_subset(range2, range1)

def print_section(section):
    text = "." * (section.start - 1)
    for element in section:
        text += 'X' 
    text += "." * (100 - section[-1])
    print(text)

file = "input.txt"
# file = "test.txt"

sum = 0
with open(file) as f:
    for line in f.readlines():
        pairs = re.findall("\d+", line)
        print("\n")
        # print(line.strip())
        section1 = range(int(pairs[0]), int(pairs[1]) + 1)
        section2 = range(int(pairs[2]), int(pairs[3]) + 1)
        print_section(section1)
        print_section(section2)
        if range_overlap(section1, section2):
            print("!!!!!")
            sum += 1
        print("\n")

print(sum)
