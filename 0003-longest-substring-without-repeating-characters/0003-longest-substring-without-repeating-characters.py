class Solution:
    '''
    given a string return the amount of consecutive characters that
    do not repeat

    "abcabcbb" = 3 because abc
    "bbbbb" = 1 because b
    "pwwkew" = 3 because wke

    use a set because a set cannot contain duplicates
    keep a variable with the largest sub string seen 
    loop through the string and if you see a char that is already
    in the set, delete n amount of elements from the set depending on
    where the element is
    use the sliding window technique

    why is it sliding window?
    it is sliding window because we are looking for the longest substring of
    something this means that we have a pointer at the beginning and then another
    pointer that continues along the string as long as the condition is true,
    hence the window part
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_value = 0
        left = 0

        # the right pointer is just a variable that iterates from the start
        # of the string till the end of the string
        for right in range(len(s)):
            # if a duplicate char is found in the set, then delete each 
            # element in the set until the duplicate char is removed
            # this is what we use the left pointer for, its to remove the
            # chars starting at the beginning of the string until the duplicate is found
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            max_value = max(len(seen), max_value)

        return max_value
