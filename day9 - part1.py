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


head_position = [0, 0]
tail_position = [0, 0]
tail_visited = set()
tail_visited.add((tail_position[0], tail_position[1]))
for move_command in today_input:
    direction, distance = move_command[0], int(move_command[1:])
    if direction == 'R':
        for step in range(distance):
            head_position[0] += 1
            tail_position = move_tail(tail_position, head_position)
            tail_visited.add((tail_position[0], tail_position[1]))
    elif direction == 'L':
        for step in range(distance):
            head_position[0] -= 1
            tail_position = move_tail(tail_position, head_position)
            tail_visited.add((tail_position[0], tail_position[1]))
    elif direction == 'U':
        for step in range(distance):
            head_position[1] -= 1
            tail_position = move_tail(tail_position, head_position)
            tail_visited.add((tail_position[0], tail_position[1]))
    elif direction == 'D':
        for step in range(distance):
            head_position[1] += 1
            tail_position = move_tail(tail_position, head_position)
            tail_visited.add((tail_position[0], tail_position[1]))
print(len(tail_visited))

print(tail_visited)
