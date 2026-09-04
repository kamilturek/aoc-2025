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
        lower, upper = map(int, range_.split("-"))

        for number in range(lower, upper + 1):
            number = str(number)

            for seq_size in range(1, len(number) // 2 + 1):
                if len(number) % seq_size != 0:
                    continue

                seq = number[:seq_size]

                for i in range(0, len(number), seq_size):
                    if number[i : i + seq_size] != seq:
                        break
                else:
                    result += int(number)
                    break

    return result


if __name__ == "__main__":
    print(solve(sys.stdin))
