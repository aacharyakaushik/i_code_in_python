"""
@author: Kaushik Acharya
"""
from typing import List

def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        # i = 0
        j = 0
        first_occurence = False
        start_idx = -1
        end_idx = -1
        
        while j < len(nums):
            # print(j, nums[j])

            # Two Sceniors 
            # 1. number is equla to target

            if nums[j] == target:
                # is it the first ocuurence, Yes
                if not first_occurence:
                    start_idx = j
                    first_occurence = True
                # is it the last element
                if j == len(nums)-1:
                    end_idx = j

            # number is not equal to target
            else:
                if first_occurence and nums[j] != nums[j-1]:
                    end_idx = j-1
                    break
           
            # increment j
            j += 1
                    
        return [start_idx, end_idx]


p,q = searchRange(searchRange,[1,2,3],1)
print(p,q)