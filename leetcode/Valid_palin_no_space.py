# -*- coding: utf-8 -*-
"""
@author: Kaushik Acharya
"""


# This solution is O(n^2), because on eloop to replace character and another to reverse
# def isPalindrome(self, s: str) -> bool:
#     s2 = ""
#     for char in s:
#         if char.isalnum():
#             s2 = "".join([s2, char])
#
#     if s2.lower() == s2[::-1].lower():
#         # print("we are here")
#         return True
#     else:
#         return False


# This is a solution using pointers and iterating over the loop once, hence O(n)
# solution

def isPalindrome(self, s: str) -> bool:
    s_last = len(s) - 1
    s_start = 0

    while s_start < s_last:
        print(s[s_start])
        print(s[s_last])

        try:
            while not s[s_start].isalnum():
                s_start += 1
            while s[s_last].isalnum():
                s_last -= 1
        except IndexError :
            return False

        if s[s_start].lower() != s[s_last].lower():
            return False

        s_start +=1
        s_last -=1

    return True


p = isPalindrome(isPalindrome, ".,")
print(p)
