"""
@author: Kaushik Acharya
"""

from typing import List


def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0 :
            nums[count], nums[i] = nums[i], nums[count]
            count +=1
        # else:
        #     count +=1
    print(nums)



input_1 = [0, 1, 0, 3, 12]
p = moveZeroes(moveZeroes, input_1)
