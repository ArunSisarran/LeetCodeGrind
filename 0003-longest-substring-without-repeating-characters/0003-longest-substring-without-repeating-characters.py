class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using a set because a set cannot have duplicates
        seen = set()
        l = 0
        result = 0

        # loop through the string
        for i in range(len(s)):
            # if a char is already in seen, remove the char from seen
            while s[i] in seen:
                seen.remove(s[l])
                # increment l to keep the sliding window moving 
                l += 1
            
            # add the char to seen, and update result as the length of the set
            seen.add(s[i])
            result = max(result, len(seen))

        return result