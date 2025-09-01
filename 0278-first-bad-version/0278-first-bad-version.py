# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

'''
[1 2 3 4 5 6 7 8] bad = 6
 L     M       R

[1 2 3 4 5 6 7 8]
         L M   R

[1 2 3 4 5 6 7 8]
         L R
         M

[1 2 3 4 5 6 7 8]
           L
           R
           M
'''

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n

        while l < r:
            m = (l + r) // 2

            if isBadVersion(m):
                r = m
            else:
                l = m + 1

        return l