Alive = '*'
Dead = '.'

def display_board(board):
    rows = []
    crow = []
    x_max,y_max=board['dimensions']
    for y  in range(y_max):
        crow = []
        for x in range(x_max):
            cpos = (x,y)
            if cpos in board['alive']:
                crow.append(Alive)
            else:
                crow.append(Dead)
        rows.append("".join(crow))
    return "\n".join(rows)

def count_alive_neighbors(grid, x, y):
    count = 0
    row = len(grid)
    col = len(grid[0])
    for i in range(max(0, x - 1), min(row, x + 2)):
        for j in range(max(0, y - 1), min(col, y + 2)):
            if not (i == x and j == y) and grid[i][j] == Alive:
                count += 1
    return count

def get_next_generation(grid):
    next_gen = [['.' for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            alive = grid[row][col]
            live_neighbors = count_neighbors(grid, row, col)

            if (alive and 2 <= live_neighbors <= 3) or (not alive and live_neighbors == 3):
                next_gen[row][col] = '*'

    return next_gen
