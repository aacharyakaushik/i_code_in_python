"""
@author: Kaushik Acharya
"""


def isHappy(self, n: int) -> bool:
    seen = set()

    def n_sq(n):
        result = 0
        while n > 0:
            number = n % 10
            # print(number * number)
            result += (number * number)
            n = n // 10
        return result

    while n_sq(n) not in seen:
        n_sum = n_sq(n)
        if n_sum == 1:
            return True
        else:
            seen.add(n_sum)
            # n_sum = n_sq(n)
            n = n_sum
    return False


p = isHappy(isHappy, 2)
print(p)
