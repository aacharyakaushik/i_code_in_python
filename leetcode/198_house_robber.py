# -*- coding: utf-8 -*-
"""
@author: Kaushik Acharya
"""
from typing import List


def rob(self, nums: List[int]) -> int:
    res = []

    if not nums:
        return 0

    res.append(nums[0])
    if len(nums) == 1:
        return nums[0]

    res.append(max(nums[0], nums[1]))

    for i in range(2, len(nums)):
        max_prev = nums[i] + res[i - 2]
        res.append(max(res[i - 1], max_prev))

    return res[-1]


p = rob(rob, [1, 2, 3, 1])
print(p)
