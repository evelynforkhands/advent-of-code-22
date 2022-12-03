input = open("input1.txt", "r")
input = input.read()
input = input.split("\n\n")
input = [sum([int(n) for n in i.split("\n") if n!= '']) for i in input]
# get the top 3 numbers of input
input = sorted(input, reverse=True)[:3]
print(sum(input))