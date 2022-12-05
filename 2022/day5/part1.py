import re

def print_stacks(stacks):
    for stack in stacks:
        print(stack)

file = "input.txt"
file = "test.txt"

# each stack is 3 chars on the string
# they are separated by 1 space
# line[0:2] - 1st stack, line[3:6] - 2nd stack, line[7:11] - 3rd stack
# 9 stacks in total

stacks = [[] for i in range(9)] 
with open(file) as f:
    for line in f.readlines():
        if line[0:4] == 'move':
            print(line.strip())
            instructions = re.findall('\d+', line)
            moves = int(instructions[0])
            from_stack = int(instructions[1])
            to_stack = int(instructions[2])
            for i in range(moves):
                print(">>> " + str(i+1))
                print(stacks[from_stack-1])
                print(stacks[to_stack-1])
                item = stacks[from_stack-1].pop(-1)
                stacks[to_stack-1].append(item)
                print(stacks[from_stack-1])
                print(stacks[to_stack-1])
        else:
            line = re.findall('\[(\w)\]\s|.{3}\s', line)
            i = 0
            for stack in line:
                if stack:
                    stacks[i].insert(0, stack)
                i += 1
            # print_stacks(stacks)
print("FINAL")
print_stacks(stacks)