from helper import read_input

grid = read_input()
grid = [list(row) for row in grid]
# the numbers are tree heights all the edge trees are visible the trees in the middle are visible if they are higher
# than the trees on the left or right, or if they are higher than all the top or bottom trees find the number of
# visible trees
visible_trees = 0
for row in range(1, len(grid) - 1):
    for column in range(1, len(grid[row]) - 1):
        if all([grid[row][column] > grid[row][column - i] for i in range(1, column + 1)]):
            visible_trees += 1
            # print('left tree', row, column, grid[row][column])
        # check if the tree is higher than all trees on the right
        elif all([grid[row][column] > grid[row][column + i] for i in range(1, len(grid[row]) - column)]):
            visible_trees += 1
            # print('right tree', row, column, grid[row][column])
        # check if the tree is higher than all trees on the top
        elif all([grid[row][column] > grid[row - i][column] for i in range(1, row + 1)]):
            visible_trees += 1
            # print('top tree', row, column, grid[row][column])
        # check if the tree is higher than all trees on the bottom
        elif all([grid[row][column] > grid[row + i][column] for i in range(1, len(grid) - row)]):
            visible_trees += 1
            # print('bottom tree', row, column, grid[row][column])

visible_trees += len(grid) * 4 - 4
print(visible_trees)
