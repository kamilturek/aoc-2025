import functools
import operator
import sys

OPERATORS = {
    "+": operator.add,
    "*": operator.mul,
}


def solve(input):
    """
    >>> solve(open('input1.txt'))
    3263827
    >>> solve(open('input2.txt'))
    10189959087258
    """
    matrix = transpose([list(line.replace("\n", "")) for line in input])
    operators = [row.pop() for row in matrix if row[-1] != " "]
    problems = [[]]

    for row in matrix:
        row = "".join(row).strip()

        if row.isdigit():
            problems[-1].append(int(row))
        else:
            problems.append([])

    return sum(
        functools.reduce(OPERATORS[op], problem[1:], problem[0])
        for problem, op in zip(problems, operators)
    )


def transpose(matrix):
    return [[row[col] for row in matrix] for col in range(len(matrix[0]))]


if __name__ == "__main__":
    print(solve(sys.stdin))
