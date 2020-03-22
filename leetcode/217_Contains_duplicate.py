"""
@author: Kaushik Acharya
"""
from typing import List


def containsDuplicate(self, nums: List[int]) -> bool:
    if len(nums) in (0, 1):
        return False
    nums.sort()
    # print(nums)
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True

    return False


input_1 = [1, 2, 3, 1]
p = containsDuplicate(containsDuplicate, input_1)
