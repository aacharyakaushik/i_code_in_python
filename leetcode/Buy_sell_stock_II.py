# -*- coding: utf-8 -*-
"""
@author: Kaushik Acharya
"""
from typing import List


# BRUTE FORCE Method
# def maxProfit(self, prices: List[int]) -> int:
#     print(prices)
#     start = prices[0]
#     total = 0
#     high = 0
#     for i in range(1, len(prices)):
#         print(prices[i])
#         if prices[i] < prices[i - 1]:
#             high = prices[i - 1]
#             # print(start, high)
#             total += (high - start)
#             print('Total - ', total)
#             start = prices[i]
#             print('start - ', start)
#             print('high - ', high)
#         else:
#             high = prices[i]
#             if prices[-1] == prices[i]:
#                 total += (high - start)
#
#             print('high - ', high)
#
#     print('Total -', total)
#     return total


# BETTER Solution i guess
def maxProfit(self, prices: List[int]) -> int:
    arr = []
    if not prices:
        return 0
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1] :
            arr.append(prices[i] - prices[i-1])
    print(arr)
    return sum(arr)


input_1 = [7,1,5,3,6,4]
p = maxProfit(maxProfit, input_1)
print(p)

input_2 = [1,2,3,4,5]
q = maxProfit(maxProfit, input_2)
print(q)

input_3 = [7,6,4,3,1]
r = maxProfit(maxProfit, input_3)
print(r)

input_4 = [2, 1, 2, 1, 0, 1, 2]
s = maxProfit(maxProfit, input_4)
print(s)

input_5 = []
t = maxProfit(maxProfit, input_5)
print(t)
