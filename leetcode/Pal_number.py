# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 12:10:50 2020

@author: Kaushik Acharya
"""

def isPalindrome(self, x: int) -> bool:
    if x < 0 :
        return False
    else:
        if str(x)== str(x)[::-1]:
            return True
        else :
            return False
        
p = isPalindrome(isPalindrome,121)
print(p)

q = isPalindrome(isPalindrome,-121)
print(q)

r = isPalindrome(isPalindrome,10)
print(r)