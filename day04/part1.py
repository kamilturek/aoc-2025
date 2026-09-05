import sys

UP_LEFT = -1 - 1j
UP = -1j
UP_RIGHT = 1 - 1j
RIGHT = 1
DOWN_RIGHT = 1 + 1j
DOWN = 1j
DOWN_LEFT = -1 + 1j
LEFT = -1

NEIGHBOURS = (
    UP_LEFT,
    UP,
    UP_RIGHT,
    RIGHT,
    DOWN_RIGHT,
    DOWN,
    DOWN_LEFT,
    LEFT,
)

PAPER = "@"


def solve(input):
    """
    >>> solve(open('input1.txt'))
    13
    >>> solve(open('input2.txt'))
    1604
    """
    grid = {
        x + y * 1j: cell for y, row in enumerate(input) for x, cell in enumerate(row)
    }

    return sum(
        1
        for pos, cell in grid.items()
        if cell == PAPER and count_paper_neighbours(grid, pos) < 4
    )


def get_neighbours(pos):
    return (pos + move for move in NEIGHBOURS)


def count_paper_neighbours(grid, pos):
    return sum(1 for neighbour in get_neighbours(pos) if grid.get(neighbour) == PAPER)


if __name__ == "__main__":
    print(solve(sys.stdin))
