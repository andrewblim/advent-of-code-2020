from .context import advent_of_code_2020
from advent_of_code_2020.day17 import *


test_board = """
.#.
..#
###
""".strip()


def test_initial_board():
    board = initial_board(test_board)
    assert set(board.keys()) == {(1,0,0), (2,1,0), (0,2,0), (1,2,0), (2,2,0)}


def test_update_board():
    board = initial_board(test_board)
    board = updated_board(board)
    assert len(board.keys()) == 11
    board = updated_board(board)
    assert len(board.keys()) == 21
    board = updated_board(board)
    assert len(board.keys()) == 38
    board = updated_board(board)
    board = updated_board(board)
    board = updated_board(board)
    assert len(board.keys()) == 112


def test_initial_board2():
    board = initial_board2(test_board)
    assert set(board.keys()) == {(1,0,0,0), (2,1,0,0), (0,2,0,0), (1,2,0,0), (2,2,0,0)}


def test_update_board2():
    board = initial_board2(test_board)
    board = updated_board2(board)
    assert len(board.keys()) == 29
    board = updated_board2(board)
    assert len(board.keys()) == 60
    board = updated_board2(board)
    board = updated_board2(board)
    board = updated_board2(board)
    board = updated_board2(board)
    assert len(board.keys()) == 848
