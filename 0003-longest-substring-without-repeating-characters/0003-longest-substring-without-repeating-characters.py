class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        counter = 0
        self.best = 0

        l = 0
        r = 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                counter = len(seen)
                r += 1
                self.best = max(self.best, counter)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1

        return self.best

