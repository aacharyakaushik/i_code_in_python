# -*- coding: utf-8 -*-
"""
@author: Kaushik Acharya
"""


def countAndSay(self, n: int) -> str:
    # s_final = '1'
    s_new = '1'

    for i in range(1, n):
        temp = ''
        char_comp = s_new[0]
        s_final = ''
        for char in s_new:
            if char == char_comp:
                temp += char
            else:
                s_final += str(len(temp))+char_comp
                temp = char
                char_comp = char

        s_final += str(len(temp)) + char_comp
        s_new = s_final

    return s_new

p = countAndSay(countAndSay, 3)
print(p)
