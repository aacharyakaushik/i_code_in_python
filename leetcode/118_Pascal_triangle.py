"""
@author: Kaushik Acharya
"""
from typing import List


def generate(self, numRows: int) -> List[List[int]]:
    if numRows == 0:
        return 0

    arr = [[1]]
    i = 1

    while len(arr) < numRows:
        row_arr = [1]
        prev_row = arr[i - 1]
        for j in range(1, len(prev_row)):
            row_arr.append(prev_row[j] + prev_row[j - 1])

        row_arr.append(1)
        # print(row_arr)
        i += 1
        arr.append(row_arr)
        # print(len(arr))

    return arr


p = generate(generate, 0)
print(p)
