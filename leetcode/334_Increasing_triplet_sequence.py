"""
@author: Kaushik Acharya
"""
from typing import List


def increasingTriplet(self, nums: List[int]) -> bool:
    if len(nums) < 3:
        return False
    # nums.sort()

    arr = [1] * len(nums)
    # arr.append(nums[0])
    # print(arr)

    i = 0
    j = 1

    while j < len(nums):
        while i < j:
            if nums[j] > nums[i]:
                arr[j] = max(arr[i]+1, arr[j])
            i += 1
            if arr[j] == 3:
                return True

        j += 1
        i = 0
    return False

    # print(arr)


p = increasingTriplet(increasingTriplet, [2,1,5,0,3])
print(p)