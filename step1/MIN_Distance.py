import numpy as np


def min_edit_distance(str1, str2):
    row = len(str1) + 1
    col = len(str2) + 1

    matrix = np.zeros((row, col), dtype=np.int32)
    matrix[:, 0] = 1
    matrix[0, :] = 1

    r = 1
    c = 1

    while r < row:
        while c < col:
            right = matrix[r - 1][c] + 1
            left = matrix[r][c - 1] + 1
            sub = matrix[r - 1][c - 1]

            if str1[r - 1] != str2[c - 1]:
                sub += 8
            matrix[r][c] = min(right, left, sub)
            c += 1
        c = 1
        r += 1

    return matrix[row-1][col-1]


print(min_edit_distance("execution", "intention"))

# print(min_edit_distance(max1, max2))
