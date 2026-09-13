import sys


def solve(input):
    """
    >>> solve(open('input1.txt'))
    3
    >>> solve(open('input2.txt'))
    529
    """
    raw_fresh_ranges, raw_ids = map(str.splitlines, input.read().split("\n\n"))
    fresh_ranges = [tuple(map(int, range_.split("-"))) for range_ in raw_fresh_ranges]

    return sum(
        1
        for id_ in map(int, raw_ids)
        if any(start <= id_ <= end for start, end in fresh_ranges)
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
