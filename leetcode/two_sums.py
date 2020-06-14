# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 08:56:46 2020

@author: Kaushik Acharya
"""


def twoSum(self, nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    myList = nums
    #        myList.sort(reverse = False)
    #        print(myList)

    #        [i for (i,target-i) in enumerate(myList) if (target-i) in myList]
    #        foundList = [i for i, x in enumerate(myList) if x == (target-i)]
    #        print(foundList)

    for i in myList:
        x = target - i
        foundList = [j for j, val in enumerate(myList) if val == x]
        print(foundList)

        for k in foundList:
            if myList.index(i) != k:
                return myList.index(i), k


#        for i = 0; i

# trying to use a map to solve
# def twoSum(self, nums, target):
#     arr = []
#     for i in range (len(nums)):
#       arr.append(target-nums[i])
#     print (arr)
#
#     for item in arr:
#         for item in nums:
#             return nums.index(x,y)


p = twoSum(twoSum, [2,7,11,15], 9)
print(p)
