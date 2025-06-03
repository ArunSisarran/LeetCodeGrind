class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for letters in s:
            if letters.isalnum():
                newStr += letters.lower()

        l = 0
        r = len(newStr) - 1

        while l < r:
            if newStr[l] == newStr[r]:
                l += 1
                r -= 1
            else:
                return False
        return True