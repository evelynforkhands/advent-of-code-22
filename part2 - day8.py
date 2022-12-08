import itertools

from helper import read_input


def get_scenic_view(visibility):
    score = len(list(itertools.takewhile(lambda x: x, visibility)))
    if score == len(visibility):
        return score
    else:
        return score + 1




grid = read_input()
grid = [list(row) for row in grid]
# the numbers are tree heights all the edge trees are visible the trees in the middle are visible if they are higher
# than the trees on the left or right, or if they are higher than all the top or bottom trees find the number of
# visible trees
scenic_scores = []
for row in range(0, len(grid)):
    for column in range(0, len(grid[row])):
        left_view = [grid[row][column] > grid[row][column - i] for i in range(1, column + 1)]

        rigt_view = [grid[row][column] > grid[row][column + i] for i in range(1, len(grid[row]) - column)]

        top_view = [grid[row][column] > grid[row - i][column] for i in range(1, row + 1)]

        bottom_view = [grid[row][column] > grid[row + i][column] for i in range(1, len(grid) - row)]

        scenic_score = 1
        for view in [left_view, rigt_view, top_view, bottom_view]:
            scenic_score *= get_scenic_view(view)
        scenic_scores.append(scenic_score)

print(max(scenic_scores))
