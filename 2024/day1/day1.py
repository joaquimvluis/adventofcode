# Historian Hysteria
def read_input(file_name):
    with open(file_name, "r") as fd:
        lines = fd.readlines()
        clean = [line.rstrip("\n\r").split() for line in lines]
        clean = list(filter(None, clean))
        return clean


def split_lists(lines):
    """Split in two lists"""
    left = [int(line[0]) for line in lines]
    right = [int(line[1]) for line in lines]

    return left, right


def total_distance(left, right):
    """Part1"""

    left.sort()
    right.sort()

    distances = [abs(int(l) - int(r)) for l, r in zip(left,right)]

    return sum(distances)

def similarity_score(left, right):
    """Part 2"""
    scores = [item * right.count(item) for item in left]

    return sum(scores)


if __name__ == "__main__":
    test_input = read_input("test.txt")
    left, right = split_lists(test_input)

    test_result = total_distance(left, right)
    print("Test")
    print("11 == ", test_result, 11 == test_result)

    test_result = similarity_score(left, right)
    print("Test")
    print("31 == ", test_result, 31 == test_result)

    in_data = read_input("input.txt")
    left, right = split_lists(in_data)

    print('total distance: ', total_distance(left, right))
    print('similarity score: ', similarity_score(left, right))
