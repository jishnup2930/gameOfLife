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