from helper import read_input


def get_ranking(item):
    return ord(item) - 38 if item.isupper() else ord(item) - 96


# part 2
rucksacks = read_input()
# print every 3 strings together
groups = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]
# find the intersection of the 3 strings
groups = [(set(groups[0]).intersection(set(groups[1]), set(groups[2]))) for groups in groups]
groups = [item for sublist in groups for item in sublist]
print(sum([get_ranking(item) for item in groups]))