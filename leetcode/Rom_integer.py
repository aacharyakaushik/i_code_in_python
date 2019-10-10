# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 19:14:19 2019

@author: Kaushik Acharya
"""

def romanToInt(self, s: str) -> int:
    d = {"I":1, "V":5, "X":10,"L":50, "C":100,"D":500, "M":1000}
    #print(d)
    #l = len(s)
    #print(l)
    num = 0
    #num = d[s[0]]
    
    
    for i in range(0,len(s)-1):
        if d[s[i]] >= d[s[i+1]]:
            num += d[s[i]]
        else:
            num -= d[s[i]]
    return num+d[s[-1]] 
    
p = romanToInt(romanToInt, "IV")
print (p)