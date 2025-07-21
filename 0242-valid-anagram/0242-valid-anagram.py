'''
hashmap:
    [key] : [value]
    letter   # of times the letter is seen
    a          4 
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

