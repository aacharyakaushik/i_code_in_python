"""
@author: Kaushik Acharya
"""
from typing import List

import sys


def maxProfit(self, prices: List[int]) -> int:
    min_val = sys.maxsize
    sum_profit = 0

    for i in range(len(prices)):
        if prices[i] < min_val:
            min_val = prices[i]

        profit = prices[i] - min_val

        if profit > sum_profit:
            sum_profit = profit

    return sum_profit


p = maxProfit(maxProfit, [7, 1, 5, 3, 6, 4])
print(p)
