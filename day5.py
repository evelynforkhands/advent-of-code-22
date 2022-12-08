from helper import read_input
#find the first empty line in crates and split the list into 2 lists
crates_input = read_input()
# flatten the list


crates = crates_input[:crates_input.index('')]
# crates = [item for sublist in crates for item in sublist]

instructions = [crates_input[crates_input.index('') + 1:]]
print(crates, instructions)