from helper import read_input

compartments = read_input()
compartments = [[[int(y) for y in x.split('-')] for x in compartment.split(',')] for compartment in compartments]
# flatten the list
compartments = [compartment for compartment in compartments]


# f[[[1, 1], [2, 93]], [[1, 1], [9, 64]]]

# check if the first compartment contains the second
def contains(compartment1, compartment2):
    return (compartment1[0] <= compartment2[0] and compartment1[1] >= compartment2[1]) or compartment1[0] >= \
           compartment2[0] and compartment1[1] <= compartment2[1]


# check if the first compartment is contained in the second
def segment_contains(segment1, segment2):
    return (segment1[0] >= segment2[0]) and (segment1[1] <= segment2[1])


def segment_overlaps(segment1, segment2):
    intersection = [max(segment1[0], segment2[0]), min(segment1[1], segment2[1])]
    return intersection[0] <= intersection[1]


compartments = [1 for pair in compartments if
                segment_overlaps(pair[0], pair[1]) or segment_overlaps(pair[1], pair[0])]

print(sum(compartments))
