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

        # if they are not the same length they cant be the same word
        if len(s) != len(t):
            return False

        count = defaultdict(int)

        # loop through the s string and add the values to a hashmap and their frequencies
        for x in s:
            count[x] = count.get(x, 0) + 1

        # loop through the t string and subtract 1 from the hashmap everytime it sees a letter they have in common
        for x in t:
            count[x] -= 1

        # if there are any values still in the hashmap it means they are different words
        # because same words would have had the same letters thus the hashmap wouldn't have any values
        for val in count.values():
            if val != 0:
                return False

        # true if it passes the previous test
        return True
