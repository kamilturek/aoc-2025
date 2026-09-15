import functools
import sys


def solve(input):
    """
    >>> solve(open('input1.txt'))
    40
    >>> solve(open('input1.txt'))
    23607984027985
    """
    manifold = frozendict(
        {x + y * 1j: cell for y, row in enumerate(input) for x, cell in enumerate(row)}
    )
    tachyon_pos = next(pos for pos, cell in manifold.items() if cell == "S")

    return get_timelines(manifold, tachyon_pos)


@functools.cache
def get_timelines(manifold, tachyon_pos):
    while True:
        if tachyon_pos not in manifold:
            return 1

        if manifold[tachyon_pos] == "^":
            return get_timelines(manifold, tachyon_pos - 1) + get_timelines(
                manifold, tachyon_pos + 1
            )

        tachyon_pos += 1j


if __name__ == "__main__":
    print(solve(sys.stdin))
