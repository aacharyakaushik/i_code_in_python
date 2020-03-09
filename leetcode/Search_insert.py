# -*- coding: utf-8 -*-
"""
@author: Kaushik Acharya
"""
from typing import List


# BRUTE FORCE
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         # print(nums[0])
#         # print(target)

#         for i in range(len(nums)):
#             if target <= nums[i]:
#                 return i

#         return len(nums)


# BINARY SEARCH
# class Solution:
def searchInsert(self, nums: List[int], target: int) -> int:
    # print(nums[0])
    # print(target)

    low = 0
    high = len(nums) - 1
    # print (high)

    while low <= high:
        mid = (low + high) // 2
        # print (mid)

        if target <= nums[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return low


p = searchInsert(searchInsert, '1,3,5,6', '5')
print(p)
