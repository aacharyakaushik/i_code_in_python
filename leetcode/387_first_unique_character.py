"""
@author: Kaushik Acharya
"""
from collections import Counter

def firstUniqChar(self, s: str) -> int:
    char_count = {}

    if not s:
        return -1
    if len(s) == 1:
        return 0

    for i in  range (len(s)):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    print(char_count)

    for char in char_count:
        if char_count[char] == 1:
            return s.index(char)

    return -1

    # # solution using counter from collections
    c = Counter(s)
    print (c)

    for idx,char in enumerate(s):
        if c[char] == 1:
            return idx
    return -1

p = firstUniqChar(firstUniqChar, "z")
print(p)
