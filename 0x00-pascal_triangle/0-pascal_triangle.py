#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n

    Args:
        n (int): the size
    """
    if n <= 0:
        return ([])
    pascal = [[1]]

    for i in range(n - 1):
        row_size = len(pascal) + 1
        row = []
        for j in range(0, row_size):
            if j == 0 or j == row_size - 1:
                row.append(1)
            else:
                row.append(pascal[i][j] + pascal[i][j - 1])
        pascal.append(row)
    return (pascal)
