'''
find the longest substring without duplicates

use a sliding window 
use a set to make sure there are no duplicates
increase the window and add the element to the set
if a duplicate is found, shrink the window until the duplicate is removed
have a max length variable to keep track of the longest sub string
compare max length with the current length of the set on each iteration
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0
        current_length = len(seen)
        l = 0

        for right in range(len(s)):
            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[l])
                    l += 1

            seen.add(s[right])
            current_length = len(seen)

            max_length = max(current_length, max_length)

        return max_length
