'''
goal: return a list of strings that group all words that are anagrams

sort the strings
using a hashmap with the key being the sorted string
add all strings of the same sort to that
return the hashmap values
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for words in strs:
            key = "".join(sorted(words))
            seen[key].append(words)

        return list(seen.values())