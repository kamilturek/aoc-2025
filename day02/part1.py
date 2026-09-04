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
        invalid_ids = set()
        lower, upper = map(int, range_.split("-"))

        for seed in map(str, (lower, upper)):
            sequence = seed[: max(len(seed) // 2, 1)]
            candidate = int(sequence + sequence)

            while candidate <= upper:
                if lower <= candidate <= upper:
                    invalid_ids.add(candidate)

                sequence = str(int(sequence) + 1)
                candidate = int(sequence + sequence)

        result += sum(invalid_ids)

    return result


if __name__ == "__main__":
    print(solve(sys.stdin))
