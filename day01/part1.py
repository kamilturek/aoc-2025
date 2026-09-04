import sys


def solve(input):
    """
    >>> solve(open('input1.txt'))
    3
    >>> solve(open('input2.txt'))
    1100
    """
    dial = 50
    count = 0

    for instruction in input:
        direction = instruction[:1]
        rotation = int(instruction[1:])

        dial = (dial + rotation * (1 if direction == "R" else -1)) % 100

        if dial == 0:
            count += 1

    return count


if __name__ == "__main__":
    print(solve(sys.stdin))
