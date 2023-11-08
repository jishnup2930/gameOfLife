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

def test_neighbours_count():
    grid = [['*','.','*'],
            ['.','*','.'],
            ['*','.','*']]
    assert count_neighbours(grid,1,1) == 4
    assert count_neighbours(grid,0,0) == 1
    assert count_neighbours(grid,2,0) == 1
    assert count_neighbours(grid,0,2) == 1
    assert count_neighbours(grid,2,2) == 1
    assert count_neighbours(grid,1,0) == 3
    assert count_neighbours(grid,0,1) == 3
    assert count_neighbours(grid,1,2) == 3
    assert count_neighbours(grid,2,1) == 3
