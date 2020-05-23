"""
@author: Kaushik Acharya
"""
from typing import List

def compress(self, chars: List[str]) -> int:
        
        i = 0
        j = 0
        idx = 0
        
        if len(chars) == 1:
            return 1
    
        
        while i < len(chars):
    
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            
            
            chars[idx] = chars[i]
            idx += 1
            if j-i > 1:
                for char in str(j-i):
                    print(char)
                    chars[idx] = char
                    idx += 1

            
            i = j

        print(chars)
                
        return idx
            

# p = compress(compress, ["a","a","b","b","c","c","c"])
# print(p)


# q = compress(compress, ["a","b","b","b","b","b","b","b","b","b","b","b","b"])
# print(q)


r = compress(compress, ["a","a","a","b","b","a","a"])
print(r)
