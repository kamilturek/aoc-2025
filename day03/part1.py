import sys

BATTERIES_COUNT = 2


def solve(input):
    """
    >>> solve(open('input1.txt'))
    357
    >>> solve(open('input2.txt'))
    17179
    """
    total = 0

    for bank in input:
        batteries = list(bank.strip())
        remaining = BATTERIES_COUNT
        joltage = ""

        while remaining > 0:
            remaining -= 1
            battery = max(batteries[: len(batteries) - remaining])
            batteries = batteries[batteries.index(battery) + 1 :]
            joltage += battery

        total += int(joltage)

    return total


if __name__ == "__main__":
    print(solve(sys.stdin))
