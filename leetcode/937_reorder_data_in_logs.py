"""
@author: Kaushik Acharya
"""
from typing import List

def reorderLogFiles(self, logs: List[str]) -> List[str]:

    digit_arr = []
    letter_arr = []

    for log in logs:
        if (log.split()[1]).isdigit():
            digit_arr.append(log)
        else:
            letter_arr.append(log.split())
    letter_arr.sort(key = lambda x:x[0])
    letter_arr.sort(key = lambda x:x[1:])

    for i in range(len(letter_arr)):
        letter_arr[i] = (" ".join(letter_arr[i]))

    # print(digit_arr)
    # print(letter_arr)
    
    letter_arr.extend(digit_arr)

    return letter_arr

input_1 = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
p = reorderLogFiles(reorderLogFiles, input_1)
print(p)