# -*- coding: utf-8 -*-
"""
Created on the day i felt like coding this

@author: Kaushik Acharya
"""

from typing import List

def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    curr = strs[0]
    # print(len(strs))
    # print(curr)
    for i in range(1, len(strs)):
        s = ""
        if len(curr) == 0:
            break
        for j in range(len(strs[i])):
            if j < len(curr) and curr[j] == strs[i][j]:
                s += curr[j]
                # print(s)
            else:
                break
        curr = s
    return curr


p = longestCommonPrefix(longestCommonPrefix, ["dog", "racecar", "car"])
print(p)

q = longestCommonPrefix(longestCommonPrefix, ["flower","flow","flight"])
print(q)
