"""
@author: Kaushik Acharya
"""


def lengthOfLongestSubstring(self, s: str) -> int:
    temp_set = []
    high = 0

    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1

    for i in range(len(s)):
        curr = s[i]

        if curr in temp_set:
            high = max(high, len(temp_set))
            temp_set = temp_set[temp_set.index(curr) + 1:]
            temp_set.append(curr)
            # print(temp_set)

        else:
            # print('adding'+ s[i])
            # print('trying to add ' + curr+ ' here')
            temp_set.append(curr)

            high = max(len(temp_set), high)

    return high


# def lengthOfLongestSubstring(self, s: str) -> int:
#
#     if len(s) == 0:
#         return 0
#     if len(s) == 1:
#         return 1
#
#     high = 0
#     start = 0
#     end = 1
#     sub = ""
#     while end < len(s):
#         if s[end] in sub:
#             if len(sub) > high:
#                 high = len(sub)
#
#             end = start+1
#             start =start +1
#             sub = ""+ s[end]
#         else:
#             sub += s[end]
#             if len(sub) > high:
#                 high = len(sub)
#             end +=1
#
#     return high


p = lengthOfLongestSubstring(lengthOfLongestSubstring, 'abcabcbb')
print(p)

q = lengthOfLongestSubstring(lengthOfLongestSubstring, 'pwwkew')
print(q)

r = lengthOfLongestSubstring(lengthOfLongestSubstring, " ")
print(r)

s = lengthOfLongestSubstring(lengthOfLongestSubstring, "dvdf")
print(s)
