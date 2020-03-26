"""
@author: Kaushik Acharya
"""

from typing import List


def isValidSudoku(self, board: List[List[str]]) -> bool:
    valid_set = set()
    # flag =0

    for i in range(9):
        for j in range(9):
            curr = board[i][j]
            # print(curr)
            if curr != '.':
                # if valid_set.add(str(curr) + "found in row" + str(i)) not in :
                # valid_set.add(curr)
                if (str(curr) + "found in row" + str(i)) in valid_set:
                    # print(str(curr) + "found in row" + str(i))
                    return False
                else:
                    valid_set.add(str(curr) + "found in row" + str(i))

                if (str(curr) + "found in column" + str(j)) in valid_set:
                    # print(str(curr) + "found in column" + str(j))
                    # print(i,j)
                    return False
                else:
                    valid_set.add(str(curr) + "found in column" + str(j))

                k = (i // 3) * 3 + j // 3
                # print(k)
                if (str(curr) + "found in box" + str(k)) in valid_set:
                    # print(str(curr) + "found in box" + str(k))
                    # print(i,j)
                    return False
                else:
                    valid_set.add(str(curr) + "found in box" + str(k))


                # print (board[i][j]
    # print(valid_set)
    # print(flag)
    return True


input_1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
p = isValidSudoku(isValidSudoku, input_1)
print(p)

input_2 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
q = isValidSudoku(isValidSudoku, input_2)
print(q)

input_3 = [[".",".",".",".","5",".",".","1","."],
           [".","4",".","3",".",".",".",".","."],
           [".",".",".",".",".","3",".",".","1"],
           ["8",".",".",".",".",".",".","2","."],
           [".",".","2",".","7",".",".",".","."],
           [".","1","5",".",".",".",".",".","."],
           [".",".",".",".",".","2",".",".","."],
           [".","2",".","9",".",".",".",".","."],
           [".",".","4",".",".",".",".",".","."]]
r = isValidSudoku(isValidSudoku, input_3)
print(r)