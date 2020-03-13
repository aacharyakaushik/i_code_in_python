# -*- coding: utf-8 -*-
"""
@author: Kaushik Acharya
"""


def climbStairs(self, n: int) -> int:
    arr = [1]

    for i in range(1, n + 1):
        # print(i)
        if i == 1:
            arr.append(1)
            # print(arr)
            # return arr[i]
        else:
            # print(type(arr[i-1]))
            arr.append(arr[i - 2] + arr[i - 1])

    return arr[n]


p = climbStairs(climbStairs, 5)
print(p)
