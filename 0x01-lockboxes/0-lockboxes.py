#!/usr/bin/python3
"""
Module 0-Lockboxes
Contains function canUnlockAll
It checks if a list of boxes can be unlocked
"""


def canUnlockAll(boxes):
    """
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked

    Args:
      boxes (list): List of lists containing the indexes of the other class
      lists, acting as keys to opening them
    Returns:
      True if all boxes can be opened, False otherwise
    """

    unlocked_boxes_indicies = [0]

    for i in unlocked_boxes_indicies:
        for j in boxes[i]:
            if j not in unlocked_boxes_indicies:
                unlocked_boxes_indicies.append(j)
    unlocked_boxes_indicies = sorted(unlocked_boxes_indicies)
    required_keys = [*range(1, len(boxes), 1)]

    if set(required_keys) <= set(unlocked_boxes_indicies):
        return True
    return False
