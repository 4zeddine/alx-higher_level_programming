#!/usr/bin/python3
"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints/floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size
        ZeroDivisionError: If div is zero.
    Returns:
        A new matrix representing the result of the division.

    """
    if (matrix == [] or not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)
            or not all((isinstance(elem, int) or isinstance(elem, float))
                for elem in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("ach row of the m(elem, floa)
        for elem in matrixtrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
