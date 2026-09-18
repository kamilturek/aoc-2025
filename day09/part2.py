import itertools
import sys


def area(rect):
    (rx1, ry1), (rx2, ry2) = rect

    width = abs(rx1 - rx2) + 1
    height = abs(ry1 - ry2) + 1

    return width * height


def intersect(rect, edge):
    (rx1, ry1), (rx2, ry2) = rect
    (ex1, ey1), (ex2, ey2) = edge

    return (
        max(ex1, ex2) > min(rx1, rx2)
        and min(ex1, ex2) < max(rx1, rx2)
        and max(ey1, ey2) > min(ry1, ry2)
        and min(ey1, ey2) < max(ry1, ry2)
    )


def solve(input):
    """
    >>> solve(open('input1.txt'))
    24
    >>> solve(open('input2.txt'))
    1637556834
    """
    red_tiles = [tuple(map(int, line.split(","))) for line in input]
    rectangles = itertools.combinations(red_tiles, 2)

    edges = [
        (red_tiles[idx], red_tiles[((idx + 1) % len(red_tiles))])
        for idx in range(len(red_tiles))
    ]

    return next(
        area(rect)
        for rect in sorted(rectangles, key=lambda rect: area(rect), reverse=True)
        if all(not intersect(rect, edge) for edge in edges)
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
