class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap to store all the combinations of strings that make a word
        seen = defaultdict(list)

        for letters in strs:
            # sort the letters 
            sorted_letters = "".join(sorted(letters))

            # add the letters to the hashmap
            seen[sorted_letters].append(letters)

        return list(seen.values())