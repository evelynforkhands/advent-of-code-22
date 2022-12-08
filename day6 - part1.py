from helper import read_input
today_input = read_input()[0]

today_input = [today_input[i:i+4] for i in range(0, len(list(today_input)))]

today_input = [len(list(row)) == len(set(list(row))) for row in today_input]
print(today_input.index(True) + 4)

    