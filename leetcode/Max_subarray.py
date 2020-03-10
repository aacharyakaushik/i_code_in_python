# -*- coding: utf-8 -*-
"""
@author: Kaushik Acharya
"""
from typing import List


# BRUTE FORCE, Gives TIME OUT
# def maxSubArray(self, nums: List[int]) -> int:
#     # print(nums[0])
#     # print(len(nums))
#     # start = 0
#     max_sum = nums[0]
#     # print(max_sum)
#
#     for i in range(len(nums)):
#         sum = nums[i]
#         if sum >= max_sum :
#             max_sum = sum
#         # print("first loop sum :", sum)
#         for j in range(i + 1, len(nums)):
#             sum += nums[j]
#             # print("Second loop sum :", sum)
#             if sum >= max_sum:
#                 max_sum = sum
#         if sum >= max_sum :
#             max_sum = sum
#         # else:
#         #     start +=1
#         #     break
#     return max_sum

# Kadanes Algorithm O(n) solution
def maxSubArray(self, nums: List[int]) -> int:
    # print(nums[0])
    # print(len(nums))
    # start = 0
    max_sum = nums[0]
    # print(max(nums[0], nums[1]))
    # print(max_sum)
    arr = [int]
    arr[0] = nums[0]
    # print(arr[0])

    for i in range(1, len(nums)):
        sum_prev = nums[i] + arr[i - 1]
        # print(sum_prev)
        arr.append(max(nums[i], sum_prev))
        # print(arr[i])
        if arr[i] > max_sum:
            max_sum = arr[i]
    print(arr)
    return max_sum


input_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
p = maxSubArray(maxSubArray, input_1)
print(p)

input_2 = [-2, 1]
q = maxSubArray(maxSubArray, input_2)
print(q)

input_3 = [-1, 0, -2]
r = maxSubArray(maxSubArray, input_3)
print(r)
