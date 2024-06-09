#!/usr/bin/python3
""" function that determines
if all the boxes can be opened"""


def canUnlockAll(boxes):
    """ function that determines if all the boxes can be opened"""
    if not boxes:
        return True
    unlocked = [0] * len(boxes)
    unlocked[0] = 1

    for box in boxes[0]:
        if box < len(boxes):
            unlocked[box] = 1

    for i in range(len(boxes)):
        for j in range(len(boxes)):
            if unlocked[j] == 1:
                for box in boxes[j]:
                    if box < len(boxes):
                        unlocked[box] = 1

    if 0 in unlocked:
        return False
    else:
        return True
