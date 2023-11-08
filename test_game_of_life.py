from gameOfLife import *

def test_diplay_board_all_dead():
    input_board = {"dimensions":(3,3),
                   "alive":[]}
    op = display_board(input_board)
    assert op =="""...
...
..."""