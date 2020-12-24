from .context import advent_of_code_2020
from advent_of_code_2020.day24 import *


def test_move_to_tile():
    moves = parse_moves("esew")
    assert moves == ["e", "se", "w"]
    moves = parse_moves("nwwswee")
    assert move_to_tile(moves) == (0,0)


test_input = """
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
    """.strip()


def test_flip_tiles():
    moves_list = [parse_moves(line) for line in test_input.splitlines()]
    flipped = flip_tiles(moves_list)
    assert len(flipped) == 10
    for i in range(1, 101):
        flipped = flip_tiles_daily(flipped)
        if i == 1:
            assert len(flipped) == 15
        elif i == 2:
            assert len(flipped) == 12
        elif i == 3:
            assert len(flipped) == 25
        elif i == 4:
            assert len(flipped) == 14
        elif i == 5:
            assert len(flipped) == 23
        elif i == 6:
            assert len(flipped) == 28
        elif i == 7:
            assert len(flipped) == 41
        elif i == 8:
            assert len(flipped) == 37
        elif i == 9:
            assert len(flipped) == 49
        elif i == 10:
            assert len(flipped) == 37
        elif i == 20:
            assert len(flipped) == 132
        elif i == 30:
            assert len(flipped) == 259
        elif i == 40:
            assert len(flipped) == 406
        elif i == 50:
            assert len(flipped) == 566
        elif i == 60:
            assert len(flipped) == 788
        elif i == 70:
            assert len(flipped) == 1106
        elif i == 80:
            assert len(flipped) == 1373
        elif i == 90:
            assert len(flipped) == 1844
        elif i == 100:
            assert len(flipped) == 2208
