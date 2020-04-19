# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 08:56:46 2020

@author: Kaushik Acharya
"""
from typing import List


def countElements(self, arr: List[int]) -> int:
    # arr.sort()
    count = 0

    arr_map = {}

    for item in arr:
        if item in arr_map:
            arr_map[item] += 1
        else:
            arr_map[item] = 1

    print(arr_map)

    for item in arr:
        if item + 1 in arr_map:
            count += 1
            # arr_map[item+1] -= 1
            # if arr_map[item+1] == 0:
            #     del arr_map[item+1]

    return count
