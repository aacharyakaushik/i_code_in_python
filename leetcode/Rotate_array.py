# -*- coding: utf-8 -*-
"""
@author: Kaushik Acharya
"""
from typing import List


def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # this is for the edge case
    if k == 0:
        return

    nums[:-k], nums[-k:] = nums[-k:], nums[:-k]


input_1 = [1, 2, 3, 4, 5, 6, 7]
rotate(rotate, input_1, 3)

# input_2
