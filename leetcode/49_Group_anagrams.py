"""
@author: Kaushik Acharya
"""
from typing import List


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    if len(strs) == 0:
        return 0

    anagram_list = {}
    full_list = []

    for items in strs:
        item_sort = ''.join(sorted(items))
        if item_sort in anagram_list:
            anagram_list[item_sort].append(items)
        else:
            anagram_list[item_sort] = [items]

    for item in anagram_list:
        full_list.append(anagram_list[item])
    print(anagram_list)
    print(full_list)

    return full_list


        # print(''.join(sorted(strs[i])))



input_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
p = groupAnagrams(groupAnagrams, input_1)
print(p)

