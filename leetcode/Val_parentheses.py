# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 23:58:26 2019

@author: Kaushik Acharya
"""

def isValid(self, s: str) -> bool:
    stack =[]
    mapping = {
            ")":"(",
            "}":"{",
            "]":"["
            }
    if len(s)!=0:
        for i in s:
            if i in mapping:
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop()
                    if top != mapping[i]:
                        return False
            else:
                stack.append(i)
        return len(stack) == 0
    return True

# Test Cases
E1 = isValid(isValid,"()")          
print(E1)
E2 = isValid(isValid, "()[]{}")    
print(E2)
E3 = isValid(isValid,"(]")
print(E3)
E4 = isValid(isValid,"([)]")
print(E4) 
E5 = isValid(isValid,"{[]}")
print(E5)         

                    