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
    for i in range(max(0, x-1), min(row, x+2)):
        for j in range(max(0, y-1), min(col, y+2)):
            if (i, j) != (x, y) and grid[i][j] == Alive:
                count += 1
    return count