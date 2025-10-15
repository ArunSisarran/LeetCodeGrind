'''
idea:
use a set to check that the characters are not duplicates
use a sliding window to help find the largest substring
if a duplicate is found, delete all letters until that duplicate letter if found from the set
keep a longest value variable
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        max_length = 0
        l = 0

        for right in range(len(s)):
            if s[right] in chars:
                while s[right] in chars:
                    chars.remove(s[l])
                    l += 1

            chars.add(s[right])
            max_length = max(max_length, len(chars))

        return max_length
        