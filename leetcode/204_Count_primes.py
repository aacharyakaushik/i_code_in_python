"""
@author: Kaushik Acharya
"""


def countPrimes(self, n: int) -> int:
    return isPrime(isPrime, n)


def isPrime(self, num: int) -> int:
    if num <= 2:
        return 0

    prime_arr = [True for _ in range(num)]

    prime_arr[0] = False
    prime_arr[1] = False

    bound = int(num ** 0.5)
    for i in range(2, bound + 1):
        if not prime_arr[i]:
            continue

        for j in range(i * i, num, i):
            prime_arr[j] = False

    return sum(prime_arr)


p = countPrimes(countPrimes, 10)
print(p)
