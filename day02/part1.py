import sys


def solve(input):
    """
    >>> solve(open('input1.txt'))
    1227775554
    >>> solve(open('input2.txt'))
    34826702005
    """
    ranges = input.read().split(",")
    result = 0

    for range_ in ranges:
        lower, upper = map(int, range_.split("-"))

        for number in range(lower, upper + 1):
            if is_invalid(number):
                result += number

    return result


def is_invalid(number):
    number = str(number)

    return (
        len(number) % 2 == 0
        and number[: len(number) // 2] == number[len(number) // 2 :]
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
