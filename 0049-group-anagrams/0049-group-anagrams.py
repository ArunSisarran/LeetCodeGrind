class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    
        map = defaultdict(list)

        for word in strs:
            sorted_word = sorted(word)
            key="".join(sorted_word) 
            map[key].append(word)

        return list(map.values())

