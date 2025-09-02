class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = defaultdict(int)
        length = 0

        for letter in s:
            seen[letter] = seen.get(letter, 0) + 1

        for val in seen.values():
            if val % 2 == 0:
                length += val
            else:
                length += val - 1

        
        return length + 1 if length < len(s) else length