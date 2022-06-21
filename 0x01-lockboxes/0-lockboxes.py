'''Module 0-Lockboxes
Contains function canUnlockAll'''

from time import clock_getres


def canUnlockAll(boxes):
  '''
  boxes is a list of lists
  A key with the same number as a box opens that box
  You can assume all keys will be positive integers
  There can be keys that do not have boxes
  The first box boxes[0] is unlocked

  Args:
    boxes: (list) List of lists containing the indexes of the higher class
    lists, acting as keys to them
  Returns:
    True if all boxes can be opened, False otherwise
  '''
  unlocked_boxes_indicies = [0]

  for i in unlocked_boxes_indicies:
    for j in boxes[i]:
      if j not in unlocked_boxes_indicies:
        # print("New key found: {}".format(j))
        unlocked_boxes_indicies.append(j)
  unlocked_boxes_indicies = sorted(unlocked_boxes_indicies)
  required_keys = [*range(1, len(boxes), 1)]

  # print("Box size: " + str(len(boxes)))
  # print("Found keys:   ", unlocked_boxes_indicies, "\nRequired keys:", required_keys)

  if set(required_keys) <= set(unlocked_boxes_indicies):
    return True
  return False

  # for i in boxes:
  #   for j in i:
  #     if j not in unlocked_boxes_indicies and j != 0:
  #       unlocked_boxes_indicies.append(j)
  # unlocked_boxes_indicies = sorted(unlocked_boxes_indicies)
  # required_keys = [*range(1, len(boxes), 1)]

  # print("Box size: " + str(len(boxes)))
  # print("Found keys:   ", unlocked_boxes_indicies, "\nRequired keys:", required_keys)
  # if all(x in unlocked_boxes_indicies for x in required_keys):
  #   return True
  # return False