# -*- coding: utf-8 -*-
"""
@author: Kaushik Acharya
"""


def lengthOfLastWord(self, s: str) -> int:
    # print(s)
    # if the input is zero
    if not s:
        return 0

    split_word = s.split()
    print(split_word)
    # print(split_word[-1])

    # if not split_word[-1]:
    #     return 0
    # This when the input is space " " as input
    try:
        return len(split_word[-1])
    except IndexError:
        return 0


p = lengthOfLastWord(lengthOfLastWord, " ")
print(p)

q = lengthOfLastWord(lengthOfLastWord, "Hello World")
print(q)