#!/usr/bin/python3
""" Rotate 2D matrix """


def rotate_2d_matrix(matrix):
    """Rotate a 2d matrix in-place by 90 Degrees.
    Transpose then Reverse each column.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
