import sys

BATTERIES_COUNT = 12


def solve(input):
    """
    >>> solve(open('input1.txt'))
    3121910778619
    >>> solve(open('input2.txt'))
    170025781683941
    """
    total = 0

    for bank in input:
        batteries = list(bank.strip())
        remaining = BATTERIES_COUNT
        joltage = ""

        while remaining > 0:
            remaining -= 1
            max_battery = max(batteries[: len(batteries) - remaining])
            batteries = batteries[batteries.index(max_battery) + 1 :]
            joltage += max_battery

        total += int(joltage)

    return total


if __name__ == "__main__":
    print(solve(sys.stdin))
