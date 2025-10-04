class Solution:
    '''
    make the longest sub string of the same character if you were able to 
    change k characters in the string and return the length of that sub
    string

    algorithm:
    keep a hashmap of each character and its frequency
    keep a variable that keeps track of the highest frequency character 
    keep a variable that keeps track of the current length of our window
    compute if current_length - max_frequency > k
    this will tell us if the current window we are in can replace k chars to create a larger sub string

    why this works?
    this works because it keeps track of how big the current window is while
    taking into account how many of the same letter there is in that window 
    and the "> k" part of the algorithm insures that the window will never 
    contain more elements than k that can be changed so the entire sub string
    is the same character
    '''
    from collections import defaultdict
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = defaultdict(int)
        max_length = 0
        left = 0

        for right in range(len(s)):
            frequency[s[right]] = frequency.get(s[right], 0) + 1
            max_frequency = max(frequency.values())
            current_length = right - left + 1

            if current_length - max_frequency > k:
                frequency[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length
