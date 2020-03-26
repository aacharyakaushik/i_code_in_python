"""
@author: Kaushik Acharya
"""
from typing import List


def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):

            # temp = matrix[i][j]
            # matrix[i][j] = matrix[j][i]
            # matrix[j][i] = temp
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # this takes advantage of the cache, rather than another loop
        matrix[i] = matrix[i][::-1]



    # for i in range(len(matrix)):
    #     # temp = matrix[i]
    #     matrix[i] = matrix[i][::-1]

    return matrix

input_1 = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

p = rotate(rotate, input_1)
print(p)