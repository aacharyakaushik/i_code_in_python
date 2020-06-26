"""
@author: Kaushik Acharya
"""
from typing import List


def longestPalindrome(self, s: str) -> str:
    def helper(l,r):
        while (l >= 0 and r < len(s) and s[l]==s[r]):
            l -= 1
            r += 1
        return s[l + 1 : r]

    res = []

    for i in range(len(s)):
        temp = helper(i,i)
        res = temp if len(temp) > len(res) else res
        
        temp = helper(i,i+1)
        res = temp if len(temp) > len(res) else res


    return res

p = longestPalindrome(longestPalindrome, 'babad')
print(p)