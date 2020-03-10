# -*- coding: utf-8 -*-
"""
@author: Kaushik Acharya
"""


def addBinary(self, a: str, b: str) -> str:
    print(a)
    print(b)

    bin_sum = bin(int(a, 2) + int(b, 2))
    print(bin_sum)
    return bin_sum[2:]


p = addBinary(addBinary, "11", "1")
print(p)
