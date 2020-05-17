"""
Created on Sat May 14 08:56:46 2020

@author: Kaushik Acharya
"""
from typing import List


def firstMissingPositive(self, nums: List[int]) -> int:

    # smallest = 0

    nums.sort()
    # print(nums)

    for i in range(1, len(nums)):
        if nums[i] < 1:
            continue
        else:
            diff = nums[i] - nums[i - 1]
            # print(diff)
            if diff != 1 and nums[i-1] > 0:
                smallest = nums[i-1] + 1
                return smallest
    return nums[-1] + 1


p = firstMissingPositive(firstMissingPositive, [3,4,-1,1])
print(p)
