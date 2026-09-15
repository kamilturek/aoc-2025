import functools
import itertools
import math
import operator
import sys
from collections import defaultdict


def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def solve(input, limit):
    """
    >>> solve(open('input1.txt'), 10)
    40
    >>> solve(open('input2.txt'), 1000)
    42315
    """
    boxes = {tuple(map(int, line.split(","))) for line in input}
    pairs = sorted(itertools.combinations(boxes, 2), key=lambda pair: distance(*pair))

    connections = defaultdict(set)

    for box1, box2 in pairs[:limit]:
        connections[box1].add(box2)
        connections[box2].add(box1)

    circuit_sizes = set()
    visited = set()

    for box in boxes:
        if box in visited:
            continue

        circuit_size = 1
        visited.add(box)

        queue = list(connections[box])

        while queue:
            connected = queue.pop()

            if connected in visited:
                continue

            visited.add(connected)
            queue.extend(list(connections[connected]))
            circuit_size += 1

        circuit_sizes.add(circuit_size)

    return functools.reduce(operator.mul, sorted(circuit_sizes, reverse=True)[:3], 1)


if __name__ == "__main__":
    print(solve(sys.stdin, int(sys.argv[1])))
