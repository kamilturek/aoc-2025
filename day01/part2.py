import sys


def solve(input):
    """
    >>> solve(open('input1.txt'))
    6
    >>> solve(open('input2.txt'))
    6358
    """
    dial = 50
    count = 0

    for instruction in input:
        direction = instruction[:1]
        rotation = int(instruction[1:])

        next_dial = dial + rotation * (1 if direction == "R" else -1)

        if next_dial == 0:
            count += 1
        elif next_dial < 0:
            while next_dial < 0:
                next_dial += 100
                count += 1

            if next_dial == 0:
                count += 1

            if dial == 0:
                count -= 1
        elif next_dial > 99:
            while next_dial > 99:
                next_dial -= 100
                count += 1

        dial = next_dial

    return count


if __name__ == "__main__":
    print(solve(sys.stdin))
