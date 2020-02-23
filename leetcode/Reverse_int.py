# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:22:46 2020

@author: Kaushik Acharya
"""

# Straight forward solution
def reverse(self, x: int) -> int:
   
    neg = False

    if x < 0:
        neg = True
        x = x * -1

    y = str(x)[::-1]
    
    if (abs(int(y)) > (2 ** 31 - 1)) :
        return 0
    else:
        if neg:
            return int(y) * -1
        else:
            return int(y)
        
        
# Solution using pop and push
def reverse_pop(self, x: int) -> int:
    neg = False
    pop = 0

    if x < 0:
        neg = True
        x = x * -1
    
    while (x!=0):
        pop = s
        
        
p = reverse(reverse,123)
print(p)
q = reverse(reverse, -123)
print(q)
r = reverse(reverse, 1534236469)
print(r)

        
        