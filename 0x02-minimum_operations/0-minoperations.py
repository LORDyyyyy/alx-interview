#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """
    Read the README file.
    """
    op = 0
    main_h = z = 1

    while n > main_h:
        if n % main_h == 0:
            z = main_h
            main_h += main_h
            op += 2
        else:
            main_h += z
            op += 1

    return op
