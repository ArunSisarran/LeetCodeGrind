import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Strip all non-alphanumeric characters from the strig
        # Make it lowercase and removes spaces
        newStr = re.sub(r'[\W+_]', '', s).lower()
        newStr = newStr.replace(" ", "")

        # Set the indicies of the two pointer algo
        L = 0
        R = len(newStr) - 1

        # Two pointer Algo
        # if the string at L index and R index are the same letter continue
        while L < R:
            if (newStr[L] == newStr[R]):
                L += 1
                R -= 1
            # if they are different return false
            else:
                return False
        # otherwise return true
        return True
