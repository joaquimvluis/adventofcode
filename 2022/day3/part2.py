def range_char(start, stop):
    characters = []
    for num in range(ord(start), ord(stop) + 1):
        characters.append(chr(num))
    return characters

file = "input.txt"
all_items = range_char('a', 'z') + range_char('A', 'Z')
sum = 0

with open(file) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    i = 0
    while(i < len(lines)):
        print("group " + str(i/3+1))
        for item in lines[i]:
            if item in lines[i+1] and item in lines[i+2]:
                priority = all_items.index(item) + 1
                sum += priority
                print("item " + item + " prioriy " + str(priority))
                break
        i += 3

print(sum)

