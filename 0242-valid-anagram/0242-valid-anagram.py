'''
hashmap:
    [key] : [value]
    letter   # of times the letter is seen
    a          4 
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap for the s string
        letters_in_s = defaultdict(int)

        # loop through the string and add all letters to the hashmap
        for char in s:
            letters_in_s[char] = letters_in_s.get(char, 0) + 1

        letters_in_t = defaultdict(int)

        for char in t:
            letters_in_t[char] = letters_in_t.get(char, 0) + 1

        if letters_in_s == letters_in_t:
            return True
        else:
            return False

