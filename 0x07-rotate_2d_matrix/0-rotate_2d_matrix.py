#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix, rotate it 90 degrees clockwise. """
    _len = len(matrix)
    for row in range(int(_len / 2)):
        offset = 0
        i = _len - 1 - row
        for column in range(row, _len - 1 - row):
            top = matrix[row][column]
            matrix[row][column] = matrix[i - offset][row]
            matrix[i - offset][row] = matrix[i][i - offset]
            matrix[i][i - offset] = matrix[column][i]
            matrix[column][i] = top
            offset += 1
