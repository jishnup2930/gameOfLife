import random
import time

def show_display(grid):
    display = ""
    alive = "*"
    dead = " "
    
    for row in grid:
        for col in row:
            if col == 1:
                display +=  alive 
            else:
                display +=  dead 
        display += '\n'
    print("\033c")
    print(display)
    return display

def count_alive_neighbors(grid, x, y):
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[0]):
                if grid[x + i][y + j] == 1:
                    count += 1
    return count

def get_next_generation(grid):
    next_gen = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            live_neighbors = count_alive_neighbors(grid, row, col)
            if grid[row][col]==1:
                if live_neighbors in [2,3]:
                    next_gen[row][col] = 1
                else:
                    next_gen[row][col] = 0
            else:
                if live_neighbors == 3:
                    next_gen [row][col] = 1
                
    return next_gen

def main():

    grid=[[0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    while True:
        show_display(grid)
        time.sleep(0.1)
        grid = get_next_generation(grid)


if __name__ == "__main__":
    main()
