import operator
import re
import sys

OPERATORS = {
    "+": operator.add,
    "*": operator.mul,
}


def solve(input):
    """
    >>> solve(open('input1.txt'))
    4277556
    >>> solve(open('input2.txt'))
    5171061464548
    """
    matrix = []
    result = 0

    for line in input:
        line = re.sub(r" +", " ", line).strip().split(" ")
        matrix.append([int(value) if value.isdigit() else value for value in line])

    rows = len(matrix)
    cols = len(matrix[0])

    for col in range(cols):
        col_result = matrix[0][col]
        op = OPERATORS[matrix[-1][col]]

        for row in range(1, rows - 1):
            col_result = op(col_result, matrix[row][col])

        result += col_result

    return result


if __name__ == "__main__":
    print(solve(sys.stdin))
