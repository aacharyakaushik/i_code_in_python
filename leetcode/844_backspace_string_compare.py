"""
@author: Kaushik Acharya
"""


def backspaceCompare(self, S: str, T: str) -> bool:
    s_arr = []
    t_arr = []

    for char in S:
        if char != '#':
            s_arr.append(char)
        elif s_arr:
            s_arr.pop()

    for char in T:
        if char != '#':
            t_arr.append(char)
        elif t_arr:
            t_arr.pop()

    return s_arr == t_arr


p = backspaceCompare(backspaceCompare, "ab#c", "ad#c")
print(p)
