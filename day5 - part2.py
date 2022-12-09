from helper import read_input
today_input = read_input()
cranes= """
            [C]         [N] [R]    
[J] [T]     [H]         [P] [L]    
[F] [S] [T] [B]         [M] [D]    
[C] [L] [J] [Z] [S]     [L] [B]    
[N] [Q] [G] [J] [J]     [F] [F] [R]
[D] [V] [B] [L] [B] [Q] [D] [M] [T]
[B] [Z] [Z] [T] [V] [S] [V] [S] [D]
[W] [P] [P] [D] [G] [P] [B] [P] [V]
 1   2   3   4   5   6   7   8   9
 """


cranes = cranes.splitlines()
cranes = [cranes[i] for cranes in cranes for i in range(1, len(cranes), 4)]
# split the cranes into arrays and put every 9 elements in a new array
cranes = [crane.split() for crane in cranes]
cranes = [cranes[i:i + 9] for i in range(0, len(cranes), 9)]

# transpose the arrays
cranes = [[cranes[j][i] for j in range(len(cranes))][:-1] for i in range(len(cranes[0]))]
# remove empty arrays
cranes = [[a[0] for a in crane if a!= []] for crane in cranes if crane != []]
# reverse the cranes
cranes = [crane[::-1] for crane in cranes]


# parse the today_input as commands for moving strings in the cranes
for comm in today_input:
    etc, number_of_blocks, etc2, from_, etc3, to_ = comm.split()
    to_be_moved = cranes[int(from_) - 1][-int(number_of_blocks):]
    cranes[int(from_) - 1] = cranes[int(from_) - 1][:-int(number_of_blocks)]
    cranes[int(to_) - 1] = cranes[int(to_) - 1] + to_be_moved


# put the first blocks of every crane order 1 to 9 in a string
first = [crane[-1] for crane in cranes]
first = ''.join(first)
print(first)




    