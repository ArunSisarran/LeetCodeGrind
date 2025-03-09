from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        resultS = {}
        resultT = {}

        for letters in s:
            resultS[letters] = resultS.get(letters, 0)+1

        for letters in t:
            resultT[letters] = resultT.get(letters, 0)+1

        if resultS == resultT:
            return True

        return False

# Another way
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = defaultdict(int)

        for x in s:
            count[x] = count.get(x, 0) + 1

        for x in t:
            count[x] -= 1

        for val in count.values():
            if val != 0:
                return False

        return True
