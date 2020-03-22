"""
@author: Kaushik Acharya
"""
from typing import List


def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    hash_set = {}
    arr = []

    if len(nums1) == 0 or len(nums2) == 0:
        return arr

    for item in nums1:
        if item in hash_set:
            hash_set[item] += 1
        else:
            hash_set[item] = 1
    # print(hash_set)
    for item in nums2:
        if item in hash_set:
            hash_set[item] -= 1
            if hash_set[item] == 0:
                del hash_set[item]
            arr.append(item)

    return arr


input_1 = [1, 2, 2, 1]
input_2 = [2, 2]
p = intersect(intersect, input_1, input_2)
print(p)

input_3 = [4,9,5]
input_4 = [9,4,9,8,4]
q = intersect(intersect, input_3, input_4)
print(q)
