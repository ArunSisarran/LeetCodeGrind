'''
return the length of the longest subtring you can make of the same
characters if you are allowed to replace k characters

use the sliding window technique
use a hashmap to keep track of the frequency of characters
if the current length of the window - most freq char is > k then we have
to make the window smaller, if its < k then we could replace k chars in that string
max variable to keep track of the biggest substring
current_length variable to keep track of current length
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = defaultdict(int)
        l = 0
        max_length = current_length = 0

        for right in range(len(s)):
            frequency[s[right]] += 1
            current_length += 1

            most_frequent = max(frequency.values())

            while current_length - most_frequent > k:
                frequency[s[l]] -= 1
                current_length -= 1
                l += 1

            max_length = max(current_length, max_length)

        return max_length