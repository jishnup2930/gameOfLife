from gameoflife import *

def test_diplay_board_all_dead():
    input_board = {"dimensions":(3,3),
                   "alive":[]}
    op = display_board(input_board)
    assert op =="""...
...
..."""

def test_display_board_one_alive():
    input_board = {'dimensions':(3,3),
                   'alive':[(1,1)]}
    op = display_board(input_board)
    assert op == """...
.*.
..."""

def test_one_column_alive_pattern():
    input_board = {'dimensions':(3,3),
                  'alive':[(1,0),(1,1),(1,2)]}
    assert display_board(input_board) == """.*.
.*.
.*."""

def test_neighbors_count():
    grid = [['*','.','*'],
            ['.','*','.'],
            ['*','.','*']]
    assert count_alive_neighbors(grid,1,1) == 4
    assert count_alive_neighbors(grid,0,0) == 1
    assert count_alive_neighbors(grid,2,0) == 1
    assert count_alive_neighbors(grid,0,2) == 1
    assert count_alive_neighbors(grid,2,2) == 1
    assert count_alive_neighbors(grid,1,0) == 3
    assert count_alive_neighbors(grid,0,1) == 3
    assert count_alive_neighbors(grid,1,2) == 3
    assert count_alive_neighbors(grid,2,1) == 3

def test_next_generation_single_alive():
    grid = [['.', '.', '.'],
            ['.', '*', '.'],
            ['.', '.', '.']]
    expected_grid = [['.', '.', '.'],
                     ['.', '.', '.'],
                     ['.', '.', '.']]

    next_gen = get_next_generation(grid)
    assert next_gen == expected_grid

def test_next_generation_four_alive_cells():
    initial_grid = [['*', '*'],
                    ['*', '*']]
    next_generation = get_next_generation(initial_grid)
    assert next_generation == [['*', '*'],
                               ['*', '*']]