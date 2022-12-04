from helper import read_input

compartments = read_input()
compartments = [[[int(y) for y in x.split('-')] for x in compartment.split(',')] for compartment in compartments]
# flatten the list
# compartments = [item for sublist in compartments for item in sublist]
# [['51-88', '52-87'], ['41-55', '22-56']]
compartments = [compartment for compartment in compartments]


# f[[[1, 1], [2, 93]], [[1, 1], [9, 64]]]
# compartments = [compartment for compartment in compartments]
# compartments = sorted(compartments, key=lambda x: x[0][0])
# for every pair of compartments, check if one contains the other
# if it does, remove the smaller one
# if it doesn't, add the pair to the list
# if the list is empty, return the number of compartments
# if the list is not empty, repeat the process
# print(compartments)
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
