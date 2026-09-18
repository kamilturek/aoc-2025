import itertools
import sys


def area(rect):
    (rx1, ry1), (rx2, ry2) = rect

    width = abs(rx1 - rx2) + 1
    height = abs(ry1 - ry2) + 1

    return width * height


def solve(input):
    """
    >>> solve(open('input1.txt'))
    50
    >>> solve(open('input2.txt'))
    4725826296
    """
    red_tiles = [tuple(map(int, line.split(","))) for line in input]
    rectangles = itertools.combinations(red_tiles, 2)

    return max(area(rect) for rect in rectangles)


if __name__ == "__main__":
    print(solve(sys.stdin))
