class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for words in strs:
            key = "".join(sorted(words))
            map[key].append(words)

        return list(map.values())