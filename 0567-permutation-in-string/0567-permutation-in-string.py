'''
idea: 
make the window the size of the s1 string
traverse along the s1 string with that fixed window length and check if within
that window contains the characters of s1 in any order
'''
from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needed = defaultdict(int)
        for char in s1:
            needed[char] = needed.get(char, 0) + 1

        l = 0
        r = len(s1) - 1

        while r <= len(s2) - 1:
            window_count = needed.copy()

            for i in range(l, r + 1):
                if s2[i] in needed:
                    window_count[s2[i]] -= 1
            
            if all(count == 0 for count in window_count.values()):
                return True
            
            l += 1
            r += 1
        
        return False


        