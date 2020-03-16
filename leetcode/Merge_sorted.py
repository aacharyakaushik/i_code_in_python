# -*- coding: utf-8 -*-
"""
@author: Kaushik Acharya
"""
from typing import List


def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # print(len(nums1))
    # print(m)
    # print(nums2)
    # print(n)

    for i in range(n):
        nums1[m+i] = nums2[i]

    nums1.sort()


    # print(nums1)


input1 = [1,2,3,0,0,0]
input2 = [2,5,6]
p= merge(merge, input1, 3, input2, 3)
print(p)