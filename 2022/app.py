def range_char(start, stop):
    characters = []
    for num in range(ord(start), ord(stop) + 1):
        characters.append(chr(num))
    return characters

file = "input.txt"
all_items = range_char('a', 'z') + range_char('A', 'Z')
sum = 0

with open(file) as f:
    for line in f.readlines():
        line = line.strip()
        half = int(len(line) / 2)
        first_compartment = line[0:half]
        second_compartment = line[half:]

        for item in first_compartment:
            if item in second_compartment:
                priority = all_items.index(item) + 1
                sum += priority
                print("item " + item + " prioriy " + str(priority))
                break

print(sum)

