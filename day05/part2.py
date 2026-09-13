import sys
from collections import deque


def solve(input):
    """
    >>> solve(open('input1.txt'))
    14
    >>> solve(open('input2.txt'))
    344260049617193
    """
    raw_fresh_ranges = input.read().split("\n\n")[0].splitlines()
    ranges = deque(
        sorted([tuple(map(int, range_.split("-"))) for range_ in raw_fresh_ranges])
    )

    while True:
        merged = False
        next_ranges = deque()

        r1_start, r1_end = ranges.popleft()

        while ranges:
            r2_start, r2_end = ranges.popleft()

            if r1_start <= r2_start <= r1_end or r2_start <= r2_end <= r1_end:
                r1_start = min(r1_start, r2_start)
                r1_end = max(r1_end, r2_end)
                merged = True
            else:
                next_ranges.append((r1_start, r1_end))
                r1_start, r1_end = r2_start, r2_end

        next_ranges.append((r1_start, r1_end))
        ranges = next_ranges

        if not merged:
            break

    return sum((r_end - r_start) + 1 for r_start, r_end in ranges)


if __name__ == "__main__":
    print(solve(sys.stdin))
