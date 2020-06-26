"""
@author: Kaushik Acharya
"""
from typing import List

def subsets(self, nums: List[int]) -> List[List[int]]:

    def backtrack(first = 0, curr =[] ):
        if len(curr) == k:
            # print(curr[:])
            # print(curr)
            output.append(curr[:])

        for i in range(first, n):

            curr.append(nums[i])

            backtrack(i + 1, curr)

            curr.pop()

    output =[]
    n = len(nums)

    for k in range(n+1):
        backtrack()
    
    return output



input_1 = [1,2,3]
p = subsets(subsets, input_1)
print(p)