#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened.

    Args
        boxes: is a list of lists
    """
    uni = set()
    counter = 0
    uni, counter = rec(boxes, uni, counter)

    return (len(uni) == len(boxes))


def rec(boxes, uni, counter):
    """
    Traverse through the boxes
    """

    if counter >= len(boxes):
        return uni, counter
    uni.add(counter)
    for k in boxes[counter]:
        if k not in uni:
            uni, counter = rec(boxes, uni, k)

    return uni, counter
