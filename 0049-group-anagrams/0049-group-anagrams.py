'''
U: given a list of strings group all the strings with the same letters together

M: we could use a hashmap to store all the letters we see

P: we use the hashmap and the sorted version on the string as a key, then we keep looping through the list and sorting all the strings and adding them to the hashmap, this would make it so all strings with the same letters exactly are groupped together

'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))

            seen[sorted_word].append(word)

        return list(seen.values())
