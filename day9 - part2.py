from helper import read_input

today_input = read_input()


def is_touching(tail, head):
    adjacent_to_head = [
        (head[0] - 1, head[1]),
        (head[0] + 1, head[1]),
        (head[0], head[1] - 1),
        (head[0], head[1] + 1),
        (head[0] - 1, head[1] - 1),
        (head[0] + 1, head[1] + 1),
        (head[0] - 1, head[1] + 1),
        (head[0] + 1, head[1] - 1),
    ]
    return tail in adjacent_to_head


def move_tail(tail, head):
    if is_touching(tail, head):
        return tail
    else:
        move_x = 1 if tail[0] < head[0] else -1 if tail[0] > head[0] else 0
        move_y = 1 if tail[1] < head[1] else -1 if tail[1] > head[1] else 0
        return tail[0] + move_x, tail[1] + move_y


tail_positions = [[0, 0] for _ in range(10)]
tail_visited = [set() for _ in range(10)]
for move_command in today_input:
    direction, distance = move_command.split(' ')
    for step in range(int(distance)):
        move_x = 1 if direction == 'R' else -1 if direction == 'L' else 0
        move_y = 1 if direction == 'U' else -1 if direction == 'D' else 0
        tail_positions[0][0] += move_x
        tail_positions[0][1] += move_y
        for tail in range(1, 10):
            tail_positions[tail] = move_tail(tail_positions[tail], tail_positions[tail - 1])
            tail_visited[tail].add((tail_positions[tail][0], tail_positions[tail][1]))

print(len(tail_visited[9]) + 1)