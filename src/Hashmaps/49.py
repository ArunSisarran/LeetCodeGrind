from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # create an empty hash map
        map = defaultdict(list)

        # loop through the array
        for letters in strs:
            # sort the current words using the sort function
            sorted_words = "".join(sorted(letters))
            # add that sorted word to the hashmap as a key and use the original word as the value
            map[sorted_words].append(letters)

        # return the hash maps values as a list
        return list(map.values())
