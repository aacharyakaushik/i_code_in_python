"""
@author: Kaushik Acharya
"""
from collections import Counter


def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_counter = {}

    for i in range(len(s)):
        if s[i] in s_counter:
            s_counter[s[i]] += 1
        else:
            s_counter[s[i]] = 1
    print(s_counter)

    for idx, char in enumerate(t):
        # print(char)
        if char not in s_counter:
            return False
        else:
            s_counter[char] -= 1
            if s_counter[char] == 0:
                del s_counter[char]

    return True


p = isAnagram(isAnagram, "rat", "car")
print(p)
