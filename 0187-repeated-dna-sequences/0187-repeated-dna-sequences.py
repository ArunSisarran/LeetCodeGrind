'''
idea:
since we know that it has to return all the 10 letter long sequences our window will
be 10 characters long and for every iteration add that sequence to a hashmap and then
return all the keys in the hashmap that have occurances greater than 1

'''
from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = defaultdict(int)
        left = 0
        # set to avoid duplicate values in the output
        result = set()

        # if the string is less than 10 long we can't return anything
        if len(s) < 10:
            return []

        # loop through the string with a window length of 10
        for right in range(len(s) - 9):
            # grab the string that is within the 10 char limit
            substring = s[left:right+10]

            if substring in seen:
                result.add(substring)
            else:
                seen[substring] = seen.get(substring, 0) + 1

            left += 1

        return list(result)


        