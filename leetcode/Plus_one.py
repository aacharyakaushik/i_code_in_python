# -*- coding: utf-8 -*-
"""
@author: Kaushik Acharya
"""
from typing import List


def plusOne(self, digits: List[int]) -> List[int]:
    # print(digits[-1])
    # print(digits[:-1])
    # print(set(digits))

    if digits[-1] != 9:
        digits[-1] += 1
    elif set(digits) == {9}:
        digits = [1] + [0] * len(digits)
    else:
        digits[-1], digits[:-1] = 0, self.plusOne(digits[:-1])
    return digits


input_1 = [1, 2, 3]
p = plusOne(plusOne,input_1)
print(p)
