import itertools
import math
import sys
from collections import defaultdict


def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def max_circuit_size(boxes, connections):
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

    return max(circuit_sizes)


def solve(input):
    """
    >>> solve(open('input1.txt'))
    25272
    >>> solve(open('input2.txt'))
    8079278220
    """
    boxes = {tuple(map(int, line.split(","))) for line in input}
    pairs = sorted(itertools.combinations(boxes, 2), key=lambda pair: distance(*pair))

    connections = defaultdict(set)

    for limit in range(len(pairs)):
        for box1, box2 in pairs[:limit]:
            connections[box1].add(box2)
            connections[box2].add(box1)

        if max_circuit_size(boxes, connections) == len(boxes):
            return box1[0] * box2[0]


if __name__ == "__main__":
    print(solve(sys.stdin))
