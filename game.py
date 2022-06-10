import itertools
from typing import Tuple, Iterator, Set

Cell = Tuple[int, int]


def advance(board: Set[Cell]) -> Set[Cell]:
    neighbours_of_existing_points = set(itertools.chain(*map(neighbours, board)))
    points_to_check = board | neighbours_of_existing_points

    new_board = set()
    for point in points_to_check:
        is_alive = point in board

        existing_neighbours = [p for p in neighbours(point) if p in board]
        num_neighbours = len(existing_neighbours)
        if not is_alive and (num_neighbours == 3):
            new_board.add(point)
        elif is_alive and num_neighbours in [2, 3]:
            new_board.add(point)
    return new_board


def neighbours(point: Cell) -> Iterator[Cell]:
    x, y = point
    # going clockwise, starting at 12'o clock
    yield x, y + 1
    yield x + 1, y + 1
    yield x + 1, y
    yield x + 1, y - 1
    yield x, y - 1
    yield x - 1, y - 1
    yield x - 1, y
    yield x - 1, y + 1


if __name__ == '__main__':
    board_with_blinker = {
        (0, 0),
        (1, 0),
        (2, 0),
    }
    print(sorted(board_with_blinker))
    for _ in range(10):
        board_with_blinker = advance(board_with_blinker)
        print(sorted(board_with_blinker))
