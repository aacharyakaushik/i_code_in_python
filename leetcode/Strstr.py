# -*- coding: utf-8 -*-
"""
@author: Kaushik Acharya
"""


def strStr(self, haystack: str, needle: str) -> int:
    # print(haystack[0])
    # print(needle[0])
    # print(len(haystack))

    if not needle:
        return 0
    short = len(haystack)
    for i in range(len(haystack)):
        for j in range(len(needle)):
            print(i, j)
            if i + j >= len(haystack):
                break
            if haystack[j + i] != needle[j]:
                break
        else:
            return i

    return -1
    # return haystack.find(needle)


p = strStr(strStr, "hello", "ll")
print(p)

q = strStr(strStr, "aaaaa", "bba")
print(q)

r = strStr(strStr, "a", "a")
print(r)
