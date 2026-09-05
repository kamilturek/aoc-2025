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
    43
    >>> solve(open('input2.txt'))
    9397
    """
    grid = {
        x + y * 1j: cell for y, row in enumerate(input) for x, cell in enumerate(row)
    }
    result = 0

    while True:
        removed = 0
        next_grid = grid.copy()

        for pos, cell in grid.items():
            if cell != PAPER:
                continue

            if count_paper_neighbours(grid, pos) < 4:
                next_grid[pos] = "x"
                removed += 1

        if removed == 0:
            break

        result += removed
        grid = next_grid

    return result


def get_neighbours(pos):
    return (pos + move for move in NEIGHBOURS)


def count_paper_neighbours(grid, pos):
    return sum(1 for neighbour in get_neighbours(pos) if grid.get(neighbour) == PAPER)


if __name__ == "__main__":
    print(solve(sys.stdin))
