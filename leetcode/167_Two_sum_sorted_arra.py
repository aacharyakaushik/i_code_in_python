"""
@author: Kaushik Acharya
"""
from typing import List

def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        map = {}
        found = []
        
        for idx, item in enumerate(numbers):
            x = target - item
            map[idx] = item,x
            
        print(map)
        
        for key, value in map.items():
            if value[1] in numbers:
                if numbers.index(value[1]) != key:
                    found.append(key+1)
                    found.append(numbers.index(value[1])+1)
                    return sorted(found)
            
        
p = twoSum(twoSum, [0,0,3,4],0)
print(p)
                
        