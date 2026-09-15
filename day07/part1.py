import sys


def solve(input):
    """
    >>> solve(open('input1.txt'))
    21
    >>> solve(open('input2.txt'))
    1619
    """
    manifold = {
        x + y * 1j: cell for y, row in enumerate(input) for x, cell in enumerate(row)
    }
    tachyons = [pos for pos, cell in manifold.items() if cell == "S"]
    splits = 0

    while tachyons:
        next_tachyons = set()

        for tachyon_pos in tachyons:
            next_tachyon_pos = tachyon_pos + 1j

            if next_tachyon_pos not in manifold:
                continue
            elif manifold[next_tachyon_pos] == ".":
                next_tachyons.add(next_tachyon_pos)
            elif manifold[next_tachyon_pos] == "^":
                next_tachyons.add(next_tachyon_pos - 1)
                next_tachyons.add(next_tachyon_pos + 1)
                splits += 1

        tachyons = next_tachyons

    return splits


if __name__ == "__main__":
    print(solve(sys.stdin))
