"""
@author: Kaushik Acharya
"""


def myAtoi(self, str: str) -> int:
    s_final = ""
    # print(numbers)

    str = str.lstrip()
    negative = False
    # flag = False

    if not str:
        return 0

    if len(str) == 1:
        if str[0].isdigit():
            return str[0]
        else:
            return 0

    first_char = str[0]

    if str[0] == '-':
        negative = True
        # flag = True
    elif str[0] == '+':
        negative = False
        # flag = True
    elif not str[0].isdigit():
        return 0

    for i in range(len(str)):
        # print(str[i])
        if str[i].isdigit():
            # print('We are here')
            s_final += str[i]
        else:
            if i == 0:
                s_final += str[i]
                continue
            else:
                break

    print(s_final)
    try:
        s_final = int(s_final)
        # print(s_final)
    except ValueError:
        return 0

    s_final = abs(s_final)
    if negative:
        s_final = min(s_final, 2147483648)
    else:
        s_final = min(s_final, 2147483647)

    if negative:
        return s_final * -1
    else:
        return s_final
    # return s_final


p = myAtoi(myAtoi, "  -42")
print(p)
