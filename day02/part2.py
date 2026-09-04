import sys


def solve(input):
    """
    >>> solve(open('input1.txt'))
    4174379265
    >>> solve(open('input2.txt'))
    43287141963
    """
    ranges = input.read().split(",")
    result = 0

    for range_ in ranges:
        invalid_ids = set()
        lower, upper = map(int, range_.split("-"))

        for seed in map(str, (lower, upper)): # do we really need both seeds?
            for size in range(1, len(seed)):
                sequence = seed[:size]
                multiplier = 2
                candidate = int(sequence * multiplier)

                while candidate <= upper:
                    inner_candidate = candidate
                    inner_sequence = sequence

                    while inner_candidate <= upper:
                        if lower <= inner_candidate <= upper:
                            invalid_ids.add(inner_candidate)

                        inner_sequence = str(int(inner_sequence) + 1)
                        inner_candidate = int(inner_sequence * multiplier)

                    multiplier += 1
                    candidate = int(sequence * multiplier)

        result += sum(invalid_ids)

    return result


if __name__ == "__main__":
    print(solve(sys.stdin))
