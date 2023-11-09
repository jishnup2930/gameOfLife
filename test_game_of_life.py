from gameoflife import *


def test_diplay_board_all_dead():
    grid = [[0,0,0],
            [0,1,0],
            [0,0,0]]
    assert show_display (grid)== """   
 * 
   
"""

def test_neighbors_count():
    grid = [[0,1,0],
            [0,1,0],
            [0,1,0]]
    assert count_alive_neighbors(grid,1,1) == 2
    assert count_alive_neighbors(grid,0,0) == 2
    assert count_alive_neighbors(grid,2,0) == 2
    assert count_alive_neighbors(grid,0,2) == 2
    assert count_alive_neighbors(grid,2,2) == 2
    assert count_alive_neighbors(grid,1,0) == 3
    assert count_alive_neighbors(grid,0,1) == 1
    assert count_alive_neighbors(grid,1,2) == 3
    assert count_alive_neighbors(grid,2,1) == 1

def test_next_generation_single_alive():
    grid = [[0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]]
    expected_grid = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]

    next_gen = get_next_generation(grid)
    assert next_gen == expected_grid

def test_next_generation_four_alive_cells():
    initial_grid = [[1, 1],
                    [1, 1]]
    next_generation = get_next_generation(initial_grid)
    assert next_generation == [[1, 1],
                               [1, 1]]
def test_next_generation_three_alive_cell():
    initial_grid =[[0,1, 0],
                   [0,1, 0],
                   [0,1, 0]]
    next_generation = get_next_generation(initial_grid)
    assert next_generation == [[0,0,0],
                               [1,1,1],
                               [0,0,0]]