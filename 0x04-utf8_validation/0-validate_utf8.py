#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding """
    counter = 0
    for d in data:
        if counter == 0:
            counter = countOnes(d)
            if counter == 0:  # a valid byte
                continue
            if counter == 1 or counter > 4:
                # invalid byte, cant be longer that 4.
                # and can't have only one most significant bit
                return False
            counter -= 1
        else:
            counter -= 1
            if countOnes(d) != 1:
                # the next `counter` bytes, it's most significant bit must be 1
                return False
    # make sure that the last int of data also it's most significant bit is 0
    return counter == 0


def countOnes(n):
    """ counts the first ones in a 8-bin integer using the bit-mask"""
    counter = 0
    while n & (1 << (7 - counter)):
        counter += 1
    return counter
