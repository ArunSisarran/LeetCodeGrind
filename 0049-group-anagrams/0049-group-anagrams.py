'''
goal : given an array of strings group all the words with the same letters

use a hashmap
loop through the strings
use the sorted string as the hashmap key
add all strings of that same sorted key together
return list of strings
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for words in strs:
            key = "".join(sorted(words))
            seen[key].append(words)

        return list(seen.values())