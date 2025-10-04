'''
idea: 
make the window the size of the s1 string
traverse along the s1 string with that fixed window length and check if within
that window contains the characters of s1 in any order
'''
from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case so we can early stop if finding the permutation is impossible
        if len(s1) > len(s2):
            return False
        
        # creating the hashmaps
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)

        # populate the hashmap with the current window size (s1) from both
        # strings
        for i in range(len(s1)):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1

        left = 0

        # check if on the first window we found the permutation
        if s1_count == s2_count:
            return True

        # loop through the s2 string starting from the len(s1) because
        # we already populated the hashmap with 0 to the len(s1) in the first for loop
        for right in range(len(s1), len(s2)):

            # add the right most element in the window to the hashmap
            s2_count[s2[right]] = s2_count.get(s2[right], 0) + 1
            # remove the leftmost element in the window 
            s2_count[s2[left]] -= 1

            # if any element becomes 0 remove it from the hashmap
            # this is done so the equality operator between hashmaps works correctly
            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]

            # increment left to move the window
            left += 1

            # if the s1 and s2 hashmap are the same we have found a valid 
            if s1_count == s2_count:
                return True
            
        return False


        